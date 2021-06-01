# -*- coding:utf-8 -*-
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):# 类似于ORM, 表单前端也有类似的HTML代码

    class Meta:
        model=Comment
        fields=['name','email','text']

