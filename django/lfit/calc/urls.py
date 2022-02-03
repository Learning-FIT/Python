from django.urls import path
from . import views

app_name = 'calc'
urlpatterns = [
    path('items/', views.items, name='items'),
    path('item/<int:item_id>', views.item, name='item'),
    # 課題（3）
    path('add_item/', views.add_item, name='add_item'),
]
