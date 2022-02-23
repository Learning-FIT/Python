from urllib.error import ContentTooShortError
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import matplotlib
from pyparsing import col
from .models import *
import pandas as pd
import matplotlib.pyplot as plt
import io


@login_required
def index(request):
    stocks = Stock.objects.all()[0:5]
    customers = Customer.objects.all()[0:5]
    context = {
        'stocks': stocks,
        'customers': customers,
    }
    return HttpResponse(render(request, 'analysis/index.html', context=context))


@login_required
def stocks(request):
    if request.method == 'POST':
        stocks = Stock.objects.filter(
            stock_code__contains=request.POST['stock_code']).all()[0:30]
        if len(stocks) < 1:
            messages.error(request, '指定の商品コードは見つかりません')
    else:
        stocks = Stock.objects.all()[0:30]
    context = {
        'stocks': stocks,
    }
    return HttpResponse(render(request, 'analysis/stocks.html', context=context))


@login_required
def stock(request, id):
    stock = get_object_or_404(Stock, pk=id)
    invoices = InvoiceLine.objects.filter(
        stock_code=stock.stock_code).values_list('invoice_date', 'customer_id', 'subtotal')
    df = pd.DataFrame(invoices, columns=[
                      'InvoiceDate', 'CustomerID', 'Subtotal'])
    total = df['Subtotal'].sum()

    context = {
        'stock': stock,
        'total': total,
    }
    return HttpResponse(render(request, 'analysis/stock.html', context=context))


@login_required
def plot_stock_customer(request, id):
    stock = get_object_or_404(Stock, pk=id)
    invoices = InvoiceLine.objects.filter(
        stock_code=stock.stock_code, is_cancel=False).values_list('customer_id', 'subtotal')
    df = pd.DataFrame(invoices, columns=['CustomerID', 'Subtotal'])
    by_customer = df[['CustomerID', 'Subtotal']].groupby(
        ['CustomerID']).sum().sort_values(['Subtotal'], ascending=False)
    matplotlib.use('agg')
    plt.pie(x=by_customer['Subtotal'][0:10], labels=by_customer.index[0:10],
            startangle=90, counterclock=False)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.cla()
    value = buf.getvalue()
    buf.close()
    return HttpResponse(value, content_type='image/png')


@login_required
def customers(request):
    if request.method == 'POST':
        customers = Customer.objects.filter(
            customer_id__contains=request.POST['customer_id']).all()[0:30]
        if len(customers) < 1:
            messages.error(request, '指定の顧客IDは見つかりません')
    else:
        customers = Customer.objects.all()[0:30]
    context = {
        'customers': customers,
    }
    return HttpResponse(render(request, 'analysis/customers.html', context=context))


@login_required
def customer(request, id):
    customer = get_object_or_404(Customer, pk=id)
    invoices = InvoiceLine.objects.filter(
        customer_id=customer.customer_id).values_list('stock_code', 'subtotal')
    print(customer.customer_id, len(invoices))
    df = pd.DataFrame(invoices, columns=['StockCode', 'Subtotal'])
    print(df.head())
    total = df['Subtotal'].sum()

    context = {
        'customer': customer,
        'total': total,
    }
    return HttpResponse(render(request, 'analysis/customer.html', context=context))


@login_required
def plot_customer_stock(request, id):
    customer = get_object_or_404(Customer, pk=id)
    invoices = InvoiceLine.objects.filter(
        customer_id=customer.customer_id, is_cancel=False).values_list('stock_code', 'subtotal')
    df = pd.DataFrame(invoices, columns=['StockCode', 'Subtotal'])
    by_stock = df[['StockCode', 'Subtotal']].groupby(
        ['StockCode']).sum().sort_values(['Subtotal'], ascending=False)
    matplotlib.use('agg')
    plt.pie(x=by_stock['Subtotal'][0:10], labels=by_stock.index[0:10],
            startangle=90, counterclock=False)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.cla()
    value = buf.getvalue()
    buf.close()
    return HttpResponse(value, content_type='image/png')
