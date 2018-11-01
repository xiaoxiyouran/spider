#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
filename: main.py
message:
refer: https://blog.csdn.net/qq_39652201/article/details/81744347
platform: pyhon 3.7
'''

__author__ = 'xi'

import DownloadProxyIP
import CheckProxyIP
import UserAgent
import requests
import ssl
from lxml import etree
# ssl._create_default_https_context = ssl._create_unverified_context

import time, random

def run():
    cnt_sucess = 0
    cnt = 0
    total = 7000
    for i in range(total):
        randomTime = random.uniform(1, 3)  # 取1-10之间的随机浮点数
        time.sleep(0.5)  # 随机等待时间

        print("process..." + str(i))
        proxyIp = DownloadProxyIP.getProxyIP()
        useragent = UserAgent.getAgent()
        headers = {
            "User-agent": useragent
        }

        # print(headers)



        # url = "https://item.taobao.com/item.htm?spm=a1z0k.7386009.0.0.1e7e3ff8RWP09T&id=580745433585&_u=t2dmg8j26111"
        url = "https://shop377074213.taobao.com/?spm=a1z10.1-c-s.0.0.202c7707Lo3tta"

        try:
            print(proxyIp)
            res = requests.get(url, proxies=proxyIp, headers=headers, timeout = 5)
            status = res.status_code  # 状态码
            if status == 200:
                cnt_sucess += 1

            # with open("dd.html", 'w') as f:
            #     f.write(res.text)
            # print(res.request)
            # print(status)
            # content = res.text
            # print(content)
            # html = etree.HTML(content)
            # ip = html.xpath('//ul[@class="inner"]/li[1]/text()')[0]
            # print("当前请求IP地址为：" + ip)
        except BaseException as e:
            print("网络连接错误", e)
        else:
            cnt += 1
            print( str(cnt) + " :sucess")

    print('----------complete----------')
    print("total:%d, sucess:%d" % (total, cnt_sucess))

if __name__ == '__main__':
    run()


