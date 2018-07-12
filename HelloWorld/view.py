#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/7/11 10:18
# @Author : x
# @File : view.py
# @Software: PyCharm

from django.shortcuts import render


def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)