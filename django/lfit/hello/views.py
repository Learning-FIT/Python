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
