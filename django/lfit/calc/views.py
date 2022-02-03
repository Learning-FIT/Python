from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

def items(request):
    items = Item.objects.all()
    context = {
        'items': items,
    }
    return HttpResponse(render(request, 'calc/items.html', context=context))

def item(request, item_id):
    item = Item.objects.get(pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        form.save()
    else:
        form = ItemForm(instance=item)
    context = {
        'item_id': item_id,
        'form': form,
    }
    return HttpResponse(render(request, 'calc/item.html', context=context))

'''django (4)
def item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            message = '保存しました'
        else:
            message = 'エラーがあります'
    else:
        form = ItemForm(instance=item)
        message = ''
    context = {
        'item_id': item_id,
        'form': form,
        'message': message,
    }
    return HttpResponse(render(request, 'calc/item.html', context=context))
'''