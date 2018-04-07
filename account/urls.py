# -*- encoding: utf-8 -*-
# @Time    : 2018-04-05 18:06
# @Author  : mike.liu
# @File    : urls.py.py
from django.conf.urls import url
from django.contrib.auth import auth_views

from account import views

app_name = 'account'
urlpatterns = [
    #url(r'^login/$',views.user_login,name="user_login"),     #自定义的登录
    url(r'^login/$',auth_views.login,name="user_login"),   #引用内置的登录方法
    url(r'^new-login/$',auth_views.login,{"template_name":"account/login.html"}),  #③

]