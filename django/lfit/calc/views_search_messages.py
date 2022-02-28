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
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, '保存しました')
        else:
            messages.error(request, 'エラーがあります')
    else:
        form = ItemForm(instance=item)
        message = ''
    context = {
        'item_id': item_id,
        'form': form,
        'message': message,
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