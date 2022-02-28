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

    price_min = forms.IntegerField(label='単価（下限）', required=False)
    price_max = forms.IntegerField(label='単価（上限）', required=False)

    CHOICES = [('and', 'AND条件で検索'), ('or', 'OR条件で検索')]
    condition = forms.ChoiceField(
        choices=CHOICES, widget=forms.RadioSelect, initial='and')

class LineForm(forms.Form):
    count = forms.IntegerField(label='個数', required=True)