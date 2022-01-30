from django.urls import path
from . import views

app_name = 'hello'
urlpatterns = [
    path('', views.index, name='index'),
    path('name/', views.name, name='name'),
    path('calc/', views.calc, name='calc'),
]