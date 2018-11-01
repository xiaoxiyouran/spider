#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
filename: main.py
message:
refer: https://blog.csdn.net/qq_39652201/article/details/81744347
platform: pyhon 3.7
'''

__author__ = 'xi'

# 需要安装 requests 库 :
# sudo easy_install pip
# sudo pip install requests
import requests
import random
import UserAgent

url = "https://item.taobao.com/item.htm?spm=a1z0k.7386009.0.0.1e7e3ff8RWP09T&id=580745433585&_u=t2dmg8j26111"
print(url)

def conf():
        '''
        配置代理，和 头
        :return:
        '''

        proxies = [
                {"http": "http://117.21.191.154:32340"},
                {"http": "http://58.251.49.4:58729"}
                ]

        headers = {
                "User-agent": UserAgent.getAgent()
        }

        proxy_ip = random.choice(proxies);
        print( proxy_ip )
        return (proxy_ip, headers)

def request_get(url, headers, params={}):
        req = requests.get(url, headers=headers, params=params )

        # 设置编码
        # req.encoding = 'utf-8'
        print(req.text)

def main(url):
        proxies, headers = conf()
        request_get(url, headers)

if __name__ == '__main__':
        main(url)


