# -*- encoding: utf-8 -*-
# @Time    : 2018-03-27 22:29
# @Author  : mike.liu
# @File    : urls.py
import views
from django.conf.urls import url
app_name='blog'
urlpatterns = [
    url(r'^$',views.blog_title,name="blog_title"),
    url(r'(?P<article_id>\d)/$',views.blog_article,name="blog_detail")
]