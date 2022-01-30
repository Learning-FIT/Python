from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse('Hello, world!')
    return HttpResponse(render(request, 'hello/index.html'))

def name(request):
    if request.method == 'POST':
        name = request.POST['name']
        context = {
            'name': name
        }
    else:
        context = {
            'name': 'name'
        }
    return HttpResponse(render(request, 'hello/name.html', context=context))

def calc(request):
    if request.method == 'POST':
        a = int(request.POST['a'])
        b = int(request.POST['b'])
        sum = a + b
        context = {
            'result': f'{a} + {b} = {sum}'
        }
    else:
        context = {
            'result': '計算したい値を入力して「計算」をクリックしてください。'
        }
    return HttpResponse(render(request, 'hello/calc.html', context=context))