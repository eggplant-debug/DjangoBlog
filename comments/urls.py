# -*- coding:utf-8 -*-
from django.urls import path
from .import views

app_name='comments' # url模式命名规定空间


urlpatterns=[
    path('comment/<int:post_pk>',views.comment,name='comment'),
]