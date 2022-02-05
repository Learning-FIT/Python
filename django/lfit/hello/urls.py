from django.urls import path
from . import views

app_name = 'hello'
urlpatterns = [
    path('', views.index, name='index'),
    path('name/', views.name, name='name'),
    # 課題（1）
    # path('calc/', views.calc, name='calc'),
]