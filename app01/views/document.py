from django.shortcuts import render, redirect
from app01 import models
from app01.utils.pagination import Pagination  # 自定义的分页组件
from app01.utils.form import UserModelForm
import pandas as pd
from django.http import HttpResponse
import os
from django.shortcuts import render


def document(request):
    df = pd.read_excel(r'E:\code\sms-b\app01\static\document\网站.xlsx')
    data = []

    kinds = df['文件名'].tolist()
    sj = df['创建时间'].tolist()
    ti = df['修改时间'].tolist()
    for i, j,k in zip(kinds, sj,ti):
        dic = {
            '文件名': i,
            '创建时间': j,
            '修改时间':k,
        }
        data.append(dic)
    # for i, j in zip(kinds, sj):
    #     dic = {
    #         '文件名': i,
    #         '创建时间': j,
    #     }
    #     data.append(dic)

    # data=pd.read_excel('E:\code\sms-b\mysql\微博搜索.xlsx',engine='openpyxl')
    # print(data)
    # return render(request, 'document.html', {"data": data})
    # page_object = Pagination(request, data)
    df = pd.read_excel(r'E:\code\sms-b\app01\static\document\书.xlsx')
    data1 = []

    kinds = df['文件名'].tolist()
    sj = df['创建时间'].tolist()
    ti = df['修改时间'].tolist()
    t9 = df['链接'].tolist()
    for i, j, k,l in zip(kinds, sj, ti,t9):
        dic = {
            '文件名': i,
            '创建时间': j,
            '修改时间': k,
            '链接':l,
        }
        data1.append(dic)
    context = {
        "data": data,
        "data1": data1,# 分完页的数据
        # "page_string": data.html()       # 生成页码
    }
    return render(request, 'document.html', context)
    # return render(request, 'document.html', {"data": page_object.page_queryset, "page_string": page_object.html()})

def screp(request):
    return render(request, 'screp.html')


def screp_weibo(request):
    data = models.webo.objects.all()

    return render(request, 'screp_weibo.html', {"data": data})
