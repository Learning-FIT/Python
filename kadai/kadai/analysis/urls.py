from django.urls import path
from . import views

app_name = 'analysis'
urlpatterns = [
    path('', views.index, name='index'),
    path('stocks/', views.stocks, name='stocks'),
    path('stock/<int:id>', views.stock, name='stock'),
    path('plot_stock_customer/<int:id>',
         views.plot_stock_customer, name='plot_stock_customer'),
    path('customers/', views.customers, name='customers'),
    path('customers/<int:id>', views.customer, name='customer'),
    path('plot_customer_stock/<int:id>',
         views.plot_customer_stock, name='plot_customer_stock'),
]
