from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.utils.timezone import make_aware
from .models import *
from .forms import *


@login_required
def items(request):
    items = Item.objects.all()
    context = {
        'items': items,
    }
    return HttpResponse(render(request, 'calc/items.html', context=context))


@login_required
def item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save()
            messages.success(request, '保存しました')
        else:
            print(form.errors)
            messages.error(request, 'エラーがあります')
    else:
        form = ItemForm(instance=item)
    context = {
        'item_id': item_id,
        'form': form,
        'item': item,
    }
    return HttpResponse(render(request, 'calc/item.html', context=context))


@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('calc:items')
        else:
            message = 'エラーがあります'
    else:
        form = ItemForm()
        message = ''
    context = {
        'form': form,
        'message': message
    }
    return HttpResponse(render(request, 'calc/add_item.html', context=context))


def index(request):
    items = []
    if request.method == 'POST':
        form = ItemSearchForm(request.POST)
        if form.is_valid():
            #items = Item.objects.filter(code=form.cleaned_data['code'])
            if form.cleaned_data['code'] == '' and form.cleaned_data['name'] == '' and form.cleaned_data['price_min'] is None and form.cleaned_data['price_max'] is None:
                messages.error(request, '商品コードか品名か価格のいずれかを入力してください')
            else:
                items = Item.objects
                if form.cleaned_data['condition'] == 'and':
                    if form.cleaned_data['code'] != '':
                        items = items.filter(code=form.cleaned_data['code'])
                    if form.cleaned_data['name'] != '':
                        items = items.filter(name__contains=form.cleaned_data['name'])
                    if form.cleaned_data['price_min'] != None:
                        items = items.filter(price__gte=int(form.cleaned_data['price_min']))
                    if form.cleaned_data['price_max'] != None:
                        items = items.filter(price__lte=int(form.cleaned_data['price_max']))
                else:
                    q_obj = Q()
                    if form.cleaned_data['code'] != '':
                        q_obj.add(Q(code=form.cleaned_data['code']), Q.OR)
                    if form.cleaned_data['name'] != '':
                        q_obj.add(Q(name__contains=form.cleaned_data['name']), Q.OR)
                    q_price = Q()
                    if form.cleaned_data['price_min'] != None:
                        q_price.add(Q(price__gte=int(form.cleaned_data['price_min'])), Q.AND)
                    if form.cleaned_data['price_max'] != None:
                        q_price.add(Q(price__lte=int(form.cleaned_data['price_max'])), Q.AND)
                    q_obj.add(q_price, Q.AND)
                    print(items.filter(q_obj).query)
                    items = items.filter(q_obj)
                if len(items) < 1:
                    messages.info(request, '商品が見つかりません')
        else:
            messages.error(request, '入力エラーがあります')
    else:
        form = ItemSearchForm()
    context = {
        'form': form,
        'items': items,
    }
    return HttpResponse(render(request, 'calc/index.html', context=context))


def line(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = LineForm(request.POST)
        if form.is_valid():
            lines = request.session.get('lines', [])
            lines.append({
                'item_id': item_id,
                'count': form.cleaned_data['count']
            })
            request.session['lines'] = lines
            return redirect('calc:index')
        else:
            print(form.errors)
    else:
        form = LineForm()

    context = {
        'item': item,
        'form': form,
    }
    return HttpResponse(render(request, 'calc/line.html', context=context))


def cart(request):
    order_lines = []
    lines = request.session.get('lines', [])

    total_sum = 0
    for line in lines:
        item = Item.objects.get(pk=line['item_id'])
        order_line = OrderLine()
        order_line.item = item
        order_line.price = item.price
        order_line.count = line['count']
        order_lines.append(order_line)
        total_sum += order_line.sum()

    context = {
        'order_lines': order_lines,
        'total_sum': total_sum,
    }
    return HttpResponse(render(request, 'calc/cart.html', context=context))


def cart_clear(request):
    if 'lines' in request.session:
        del request.session['lines']
    messages.info(request, 'ショッピングカートを空にしました')
    return redirect('calc:index')


def save_order(request):
    order_lines = []
    lines = request.session.get('lines', [])

    if request.method == 'POST':
        order = Order()
        order.order_datetime = make_aware(datetime.datetime.now())
        order.save()
        for line in lines:
            item = Item.objects.get(pk=line['item_id'])
            order_line = OrderLine()
            order_line.order = order
            order_line.item = item
            order_line.price = item.price
            order_line.count = line['count']
            order_line.save()
        del request.session['lines']
        messages.success(request, '注文しました')
        return redirect('calc:index')

    total_sum = 0
    for line in lines:
        item = Item.objects.get(pk=line['item_id'])
        order_line = OrderLine()
        order_line.item = item
        order_line.price = item.price
        order_line.count = line['count']
        order_lines.append(order_line)
        total_sum += order_line.sum()

    context = {
        'order_lines': order_lines,
        'total_sum': total_sum,
    }
    return HttpResponse(render(request, 'calc/save_order.html', context=context))


@login_required
def orders(request):
    orders = Order.objects.all()
    context = {
        'orders': orders,
    }
    return HttpResponse(render(request, 'calc/orders.html', context=context))


@login_required
def order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    context = {
        'order': order,
    }
    return HttpResponse(render(request, 'calc/order.html', context=context))


def items_json(request):
    items = Item.objects.all()
    results = []
    for item in items:
        results.append({
            'id': item.id,
            'code': item.code,
            'name': item.name,
            'price': item.price,
            'image': item.image.url if item.image else '',
        })
    return JsonResponse({'items': results})


def orders_json(request):
    orders = Order.objects.all()
    results = []
    for order in orders:
        order_lines = []
        for order_line in order.orderline_set.all():
            order_lines.append({
                'id': order_line.id,
                'price': order_line.price,
                'count': order_line.count,
                'item_code': order_line.item.code,
                'item_name': order_line.item.name,
                'item_image': order_line.item.image.url if order_line.item.image else '',
                'sum': order_line.sum(),
            })
        results.append({
            'id': order.id,
            'order_datetime': order.order_datetime,
            'total_sum': order.total_sum(),
            'order_lines': order_lines,
        })
    return JsonResponse({'orders': results})
