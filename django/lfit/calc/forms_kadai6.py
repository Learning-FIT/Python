from dataclasses import fields
from django import forms
from .models import *

class ItemSearchForm(forms.Form):
    code = forms.CharField(label='商品コード', required=False)
    name = forms.CharField(label='品名', required=False)

    price_min = forms.IntegerField(label='単価（下限）', required=False)
    price_max = forms.IntegerField(label='単価（上限）', required=False)
