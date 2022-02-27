from dataclasses import fields
from django import forms
from .models import *

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['code', 'name', 'price']

# Day6 商品検索の作成
class ItemSearchForm(forms.Form):
    code = forms.CharField(label='商品コード', required=False)
    name = forms.CharField(label='品名', required=False)

# Day6 明細登録画面の作成
class LineForm(forms.Form):
    count = forms.IntegerField(label='個数', required=True)