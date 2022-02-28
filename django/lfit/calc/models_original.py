from django.db import models

class Item(models.Model):
    code = models.CharField(max_length=10, verbose_name='商品コード')
    name = models.CharField(max_length=255, verbose_name='商品名')
    price = models.IntegerField(verbose_name='単価')

class Order(models.Model):
    order_datetime = models.DateTimeField(verbose_name='注文日時')

class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='注文')
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING, verbose_name='商品')
    price = models.IntegerField(verbose_name='販売単価')
    count = models.IntegerField(verbose_name='個数')
