# coding=gbk
# -*- coding:uft-8 -*-
# 微博搜索

import requests
from lxml import etree
import time
from urllib import parse
import pandas as pd
import mysql
import openpyxl

def collect(k, da):

    resLs = []
    for page in range(6):
        time.sleep(2)
        page += 1
        url = f'https://s.weibo.com/weibo?q={parse.quote(k)}&suball=1&timescope=custom:{da}&Refer=g&page={page}'
        print(url)
        print(k, da, page)
        headers = {
            'Cookie': ck,
            'User-Agent': ua,
            'Referer': url
        }
        while True:
            try:
                res = requests.get(url=url, headers=headers, timeout=(5, 5)).content.decode('utf-8', errors='ignore')
                # print(res)

                break
            except:
                time.sleep(2)
        if f'<p>抱歉，未找到“{k}”相关结果。</p>' in res:
            break
        tree = etree.HTML(res)
        for li in tree.xpath('//div[@action-type="feed_list_item"]'):

            name = li.xpath('.//a[@class="name"]/text()')[0]
            date = li.xpath('.//div[@class="from"]/a/text()')[0].strip()
            print(date)
            cbox = li.xpath('.//p[@node-type="feed_list_content_full"]')
            cbox = li.xpath('.//p[@node-type="feed_list_content"]')[0] if not cbox else cbox[0]
            cont = '\n'.join(cbox.xpath('./text()')).strip()
            tran = li.xpath('.//div[@class="card-act"]/ul/li[1]/a//text()')[1].strip()
            ID = li.xpath('./@mid')[0]
            try:

                mysql.insertdata(name, cont, date, f'https://m.weibo.cn/detail/{ID}')
            except:
                continue
            try:
                tran = eval(tran)
            except:
                tran = 0
            comm = li.xpath('.//div[@class="card-act"]/ul/li[2]/a//text()')[0].strip()
            try:
                comm = eval(comm)
            except:
                comm = 0
            like = li.xpath('.//div[@class="card-act"]/ul/li[3]/a//text()')[0].strip()
            try:
                like = eval(like)
            except:
                like = 0
            ID = li.xpath('./@mid')[0]
            dic = {
                '昵称': name,
                '时间': date,
                '内容': cont,
                '转发': tran,
                '评论': comm,
                '点赞': like,
                '链接': f'https://m.weibo.cn/detail/{ID}',
                'ID': ID
            }
            resLs.append(dic)
            print(dic)
    df = pd.DataFrame(resLs)
    df.to_excel('微博搜索.xlsx', index=False)

if __name__ == '__main__':
    mysql.deleteall()
    ck='UOR=login.sina.com.cn,s.weibo.com,login.sina.com.cn; SINAGLOBAL=5282098544343.845.1691556520904; ALF=1694398680; SCF=AuuPlH13F8OP2kz2pqgFYna_8rc7jJjIR63X32Np-cfA5rPjzT9tyk3GQVrlavtnAONL1qRmfj8QAKLcFgPYAHs.; _s_tentry=passport.weibo.com; Apache=966214344228.24.1691806908871; ULV=1691806908877:12:12:12:966214344228.24.1691806908871:1691806682815; PC_TOKEN=e134925cfc; crossidccode=CODE-tc-1QuEgm-168oIs-TRH8szEI1RQB1znff73e4; SSOLoginState=1691806923; SUB=_2A25J0pybDeThGeFI7FcY8SnIyz-IHXVrPCTTrDV8PUJbkNAGLRL_kW1NfPVuyjEcpDhjTSqlkUDnDWzg0eG92N6i; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFQMIYgcLScXc9x3dC1DwZ-5NHD95QNSoMf1K2NSh50Ws4DqcjPi--Xi-i2iKLWi--fiK.7iKy2S0q0Soqt'
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'
    collect('#华北理工大学#', '2022-01-1:2023-08-31')

#ck='UOR=login.sina.com.cn,s.weibo.com,login.sina.com.cn; SINAGLOBAL=5282098544343.845.1691556520904; ALF=1694398680; SCF=AuuPlH13F8OP2kz2pqgFYna_8rc7jJjIR63X32Np-cfA5rPjzT9tyk3GQVrlavtnAONL1qRmfj8QAKLcFgPYAHs.; _s_tentry=passport.weibo.com; Apache=966214344228.24.1691806908871; ULV=1691806908877:12:12:12:966214344228.24.1691806908871:1691806682815; PC_TOKEN=e134925cfc; crossidccode=CODE-tc-1QuEgm-168oIs-TRH8szEI1RQB1znff73e4; SSOLoginState=1691806923; SUB=_2A25J0pybDeThGeFI7FcY8SnIyz-IHXVrPCTTrDV8PUJbkNAGLRL_kW1NfPVuyjEcpDhjTSqlkUDnDWzg0eG92N6i; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFQMIYgcLScXc9x3dC1DwZ-5NHD95QNSoMf1K2NSh50Ws4DqcjPi--Xi-i2iKLWi--fiK.7iKy2S0q0Soqt'
