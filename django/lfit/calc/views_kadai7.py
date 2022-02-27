from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from .models import *
from .forms import *


def items(request):
    items = Item.objects.all()
    context = {
        'items': items,
    }
    return HttpResponse(render(request, 'calc/items.html', context=context))


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


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('calc:items')
        else:
            messages.error(request, 'エラーがあります')
    else:
        form = ItemForm()
    context = {
        'form': form,
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
                items = Item.objects.all()
                if form.cleaned_data['condition'] == 'and':
                    if form.cleaned_data['code'] != '':
                        items = items.filter(code=form.cleaned_data['code'])
                    if form.cleaned_data['name'] != '':
                        items = items.filter(
                            name__contains=form.cleaned_data['name'])
                    if form.cleaned_data['price_min'] != None:
                        items = items.filter(price__gte=int(
                            form.cleaned_data['price_min']))
                    if form.cleaned_data['price_max'] != None:
                        items = items.filter(price__lte=int(
                            form.cleaned_data['price_max']))
                else:
                    q_obj = Q()
                    if form.cleaned_data['code'] != '':
                        q_obj.add(Q(code=form.cleaned_data['code']), Q.OR)
                    if form.cleaned_data['name'] != '':
                        q_obj.add(
                            Q(name__contains=form.cleaned_data['name']), Q.OR)
                    q_price = Q()
                    if form.cleaned_data['price_min'] != None:
                        q_price.add(
                            Q(price__gte=int(form.cleaned_data['price_min'])), Q.AND)
                    if form.cleaned_data['price_max'] != None:
                        q_price.add(
                            Q(price__lte=int(form.cleaned_data['price_max'])), Q.AND)
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
