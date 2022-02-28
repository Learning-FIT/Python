from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
# Day6 商品検索
from django.db.models import Q
# Day6 メッセージフレームワーク
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
        form = ItemForm(request.POST, instance=item)
        # Day6 画像ファイルのアップロード
        # form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            # Day6 画像ファイルのアップロード
            #item = form.save()
            message = '保存しました'
            # messages.success(request, '保存しました')
        else:
            message = 'エラーがあります'
            # messages.error(request, 'エラーがあります')
    else:
        form = ItemForm(instance=item)
        message = ''
    context = {
        'item_id': item_id,
        'form': form,
        'message': message,
        # Day6 画像ファイルのアップロード
        # 'item': item,
    }
    return HttpResponse(render(request, 'calc/item.html', context=context))

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
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
        'message': message,
    }
    return HttpResponse(render(request, 'calc/add_item.html', context=context))

# Day6 商品検索の作成
def index(request):
    if request.method == 'POST':
        form = ItemSearchForm(request.POST)
        items = []
        if form.is_valid():
            #items = Item.objects.filter(code=form.cleaned_data['code'])
            if form.cleaned_data['code'] == '' and form.cleaned_data['name'] == '':
                messages.error(request, '商品コードか品名のどちらかを入力してください')
            else:
                items = Item.objects
                if form.cleaned_data['code'] != '':
                    items = items.filter(code=form.cleaned_data['code'])
                if form.cleaned_data['name'] != '':
                    items = items.filter(name__contains=form.cleaned_data['name'])
                if len(items) < 1:
                    messages.info(request, '商品が見つかりません')
        else:
            messages.error(request, '入力エラーがあります')
    else:
        form = ItemSearchForm()
        items = []
    context = {
        'form': form,
        'items': items,
    }
    return HttpResponse(render(request, 'calc/index.html', context=context))

# Day6 明細登録画面の作成
def line(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        # Day6 明細登録画面の作成（POSTされた後）
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

# Day6 ショッピングカート画面の作成
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
