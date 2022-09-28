# 开发时间 2022/9/13 14:57
# 文件: encrypt.py
"""
该插件为 MD5加密插件
返回加密后的结果
"""
from django.conf import settings
import hashlib


def md5(data_string):
    obj = hashlib.md5(settings.SECRET_KEY.encode('utf-8'))
    obj.update(data_string.encode('utf-8'))
    return obj.hexdigest()
