from django.shortcuts import render, redirect
from app01 import models
from app01.utils.pagination import Pagination  # 自定义的分页组件
from app01.utils.form import UserModelForm

from django.http import HttpResponse
import os
from django.shortcuts import render

def chat(request):
    return render(request, 'chat.html')
def screp(request):
    return render(request, 'screp.html')
def screp_weibo(request):

    data = models.webo.objects.all()

    return render(request, 'screp_weibo.html', {"data": data})