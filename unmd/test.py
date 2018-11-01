#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
filename: main.py
message:
refer: https://blog.csdn.net/qq_39652201/article/details/81744347
platform: pyhon 3.7
'''

__author__ = 'xi'


proxy_list = [
              {'http':"http://59.53.67.215:80"},
              {'http':"http://60.161.14.77:8001"},
              {'http':"http://61.144.14.68:80"},
              {'http':"http://61.144.68.180:9999"},
              {'http':"http://61.164.108.84:8844"},
              {'http':"http://61.166.55.153:11808"}
             ]


import random
user_agents = [
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'
    ]

import urllib2,re,time,urllib,random


def getHtml(url):
    proxy_ip =random.choice(proxy_list) #在proxy_list中随机取一个ip
    print proxy_ip
    proxy_support = urllib2.ProxyHandler(proxy_ip)
    opener = urllib2.build_opener(proxy_support,urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    request = urllib2.Request(url)
    user_agent = random.choice(user_agents)  # 在user_agents中随机取一个做user_agent
    request.add_header('User-Agent',user_agent) #修改user-Agent字段
    print user_agent
    html = urllib2.urlopen(request).read()
    return proxy_ip

urls = ['http://www.25shiyan.com/?fromuid=16','http://www.25shiyan.com/forum.php?mod=viewthread&tid=37840&extra=page%3D1','http://www.25shiyan.com/forum.php?mod=viewthread&tid=36786&extra=page%3D1']
count_True,count_False,count= 0,0,0
while True:
    for url in urls:
        count +=1
        try:
            proxy_ip=getHtml(url)
        except urllib2.URLError:
            print 'URLError! The bad proxy is %s' %proxy_ip
            count_False += 1
        except urllib2.HTTPError:
            print 'HTTPError! The bad proxy is %s' %proxy_ip
            count_False += 1
        except:
            print 'Unknown Errors! The bad proxy is %s ' %proxy_ip
            count_False += 1
        randomTime = random.uniform(1,3) #取1-10之间的随机浮点数
        time.sleep(randomTime) #随机等待时间
        print '%d Eroors,%d ok,总数 %d' %(count_False,count - count_False,count)
