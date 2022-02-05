from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

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
        'message': message
    }
    return HttpResponse(render(request, 'calc/add_item.html', context=context))
