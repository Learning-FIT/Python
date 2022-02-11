from django.urls import path
from . import views

app_name = 'calc'
urlpatterns = [
    path('items/', views.items, name='items'),
    path('item/<int:item_id>', views.item, name='item'),
    # 課題（3）
    path('add_item/', views.add_item, name='add_item'),
    path('', views.index, name='index'),
    path('line/<int:item_id>', views.line, name='line'),
    path('cart/', views.cart, name='cart'),
    path('cart_clear/', views.cart_clear, name='cart_clear'),
    path('save_order/', views.save_order, name='save_order'),
    path('orders/', views.orders, name='orders'),
    path('order/<int:order_id>', views.order, name='order'),
    path('items.json', views.items_json, name='items_json'),
]
