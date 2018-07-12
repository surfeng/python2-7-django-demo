#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/7/11 15:18
# @Author : 
# @File : search2.py
# @Software: PyCharm
# @Desc  : 

from django.shortcuts import render
from django.views.decorators import csrf


# 接收POST请求数据
def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q'].encode('utf-8')
    return render(request, "post.html", ctx)