from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='ユーザー名', required=True)
    password = forms.CharField(label='パスワード', required=True, widget=forms.PasswordInput)
    