from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

def item(request, item_id):
    item = Item.objects.get(pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        form.save()
        message = '保存しました'
    else:
        form = ItemForm(instance=item)
        message = ''
    context = {
        'item_id': item_id,
        'form': form,
        'message': message,
    }
    return HttpResponse(render(request, 'calc/item.html', context=context))
