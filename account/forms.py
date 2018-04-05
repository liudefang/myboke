# -*- encoding: utf-8 -*-
# @Time    : 2018-04-05 18:12
# @Author  : mike.liu
# @File    : forms.py
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)