# -*- encoding: utf-8 -*-
# @Time    : 2018-04-05 18:06
# @Author  : mike.liu
# @File    : urls.py.py
from django.conf.urls import url

from account import views

app_name = 'account'
urlpatterns = [
    url(r'^login/$',views.user_login,name="user_login"),

]