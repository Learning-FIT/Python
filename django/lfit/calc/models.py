from django.db import models
from django.conf import settings
import os


class Item(models.Model):
    code = models.CharField(max_length=10, verbose_name='商品コード', unique=True)
    name = models.CharField(max_length=255, verbose_name='商品名')
    price = models.IntegerField(verbose_name='単価')
    image = models.ImageField(upload_to='images/', default=None, verbose_name='商品画像')

    def thumb_image(self):
        if self.image:
            return os.path.join(settings.MEDIA_URL, 'thumb', f'{self.id}.jpg')
        else:
            return False


class Order(models.Model):
    order_datetime = models.DateTimeField(verbose_name='注文日時')

    def total_sum(self):
        total_sum = 0
        for order_line in self.orderline_set.all():
            total_sum += order_line.sum()
        return total_sum


class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='注文')
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING, verbose_name='商品')
    price = models.IntegerField(verbose_name='販売単価')
    count = models.IntegerField(verbose_name='個数')

    def sum(self):
        return self.price * self.count
