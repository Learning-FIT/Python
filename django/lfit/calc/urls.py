from django.urls import path
from . import views

app_name = 'calc'
urlpatterns = [
    path('items/', views.items, name='items'),
    path('item/<int:item_id>', views.item, name='item'),
    # 課題（3）
    path('add_item/', views.add_item, name='add_item'),
    # Day6 商品検索の作成
    path('', views.index, name='index'),
    # Day6 ナビゲーションバー
    path('line/<int:item_id>', views.line, name='line'),
    path('cart/', views.cart, name='cart'),
    # Day6 ショッピングカートを空にする、注文
    path('cart_clear/', views.cart_clear, name='cart_clear'),
    path('save_order/', views.save_order, name='save_order'),
    # Day7 API
    path('items.json', views.items_json, name='items_json'),
    # 課題（11）
    path('orders.json', views.orders_json, name='orders_json'),
]