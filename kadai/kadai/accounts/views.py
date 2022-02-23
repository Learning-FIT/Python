from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .forms import *


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(
                request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('analysis:index')
            else:
                messages.error(request, 'ログインに失敗しました')
        else:
            messages.error(request, '入力エラーがあります')
            print(form.errors)
    else:
        form = LoginForm()
    context = {
        'form': form,
    }
    return HttpResponse(render(request, 'accounts/login.html', context=context))


def logout(request):
    auth.logout(request)
    messages.info(request, 'ログアウトしました')
    return redirect('accounts:login')
