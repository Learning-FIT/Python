from dataclasses import fields
from django import forms
from .models import *


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['code', 'name', 'price']


class ItemSearchForm(forms.Form):
    code = forms.CharField(label='商品コード', required=False)
    name = forms.CharField(label='品名', required=False)
