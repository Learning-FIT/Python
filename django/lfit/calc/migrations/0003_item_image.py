# Generated by Django 4.0.1 on 2022-02-06 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_alter_item_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default=None, upload_to='images/', verbose_name='商品画像'),
        ),
    ]