from django.db import models


class InvoiceLine(models.Model):
    invoice = models.CharField(max_length=10, verbose_name='請求書番号')
    stock_code = models.CharField(max_length=20, verbose_name='商品コード')
    quantity = models.IntegerField(verbose_name='数量')
    invoice_date = models.DateTimeField(verbose_name='取引日時')
    price = models.FloatField(verbose_name='単価')
    customer_id = models.CharField(max_length=10, verbose_name='顧客ID')
    is_cancel = models.BooleanField(verbose_name='キャンセル')
    subtotal = models.FloatField(verbose_name='小計')


class Stock(models.Model):
    stock_code = models.CharField(max_length=20, verbose_name='商品コード')
    description = models.CharField(max_length=255, verbose_name='品名')


class Customer(models.Model):
    customer_id = models.CharField(max_length=10, verbose_name='顧客ID')
    country = models.CharField(max_length=30, verbose_name='国名')
