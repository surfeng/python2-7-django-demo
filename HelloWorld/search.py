#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/7/11 13:55
# @Author : 
# @File : search.py
# @Software: PyCharm
# @Desc  :

from django.http import HttpResponse
from django.shortcuts import render_to_response

#   表单
def search_form(request):
    return render_to_response('search_form.html')

# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        message = '你搜索的内容为：' + request.GET['q'].encode("utf-8")
    else:
        message = '你提交了空表单'
    return HttpResponse(message)
