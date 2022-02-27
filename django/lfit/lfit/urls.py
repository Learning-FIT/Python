"""lfit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# Day6 画像ファイルを使用する
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('hello/', include('hello.urls')),
    path('calc/', include('calc.urls')),
    # Day7 認証システム
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    # Day6 Django Toolbar
    path('__debug__/', include('debug_toolbar.urls')),

]
# Day6 画像ファイルを使用する
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
