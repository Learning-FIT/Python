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

]