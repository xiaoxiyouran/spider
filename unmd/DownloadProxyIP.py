#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
filename: CheckProxyIP.py
message:
检查以下代理ip 是否可用
platform: pyhon 3.5
'''

__author__ = 'xi'

import  requests
from html.parser import HTMLParser
from urllib import request
import re
from collections import OrderedDict
import random


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super(MyHTMLParser,self).__init__()
        self.IP = False #这些布尔值是为了在handle_data里作处理data的判断条件。
        self.PORT = False
        self.type = False
        # self.j_year = False
        self.currentTag = ''
        self.all_info=[]
        self.m_dict = {}

    def handle_starttag(self, tag, attrs):
        if tag == 'td' and ('data-title','IP') in attrs:
            self.IP=True
            self.currentTag = 'IP'
        elif tag == 'td' and ('data-title','PORT') in attrs:
            self.PORT=True
            self.currentTag = 'PORT'

        elif tag == 'td' and ('data-title','类型') in attrs:
            self.type=True
            self.currentTag = 'TYPE'

        else:
            pass
        # elif tag == 'time':
        #     self.IP=True

    def handle_data(self,data):
        if self.IP is True:   #经大佬提醒这里很关键，要给个正则约束年份只读数字进去。[0-9]就是只读数字。否则会读出两个莫名其妙的字符。
            if re.match(r'[0-9.]',data.strip()):
                # self.all_info.append(dict(IP=data))
                self.m_dict['IP'] = data
        elif self.PORT is True:
            # self.all_info.append(dict(PORT=data))
            self.m_dict['PORT'] = data
        elif self.type is True:
            # self.all_info.append(dict(type=data))
            self.m_dict['TYPE'] = data
            self.all_info.append(self.m_dict)
            self.m_dict = {}
        # elif self.j_title is True:
        #     self.all_info.append(dict(会议主题=data))

    #这里还是不太理解，不过不这样的话，读出来都是乱了的，有始有终？?
    def handle_endtag(self,tag):
        if self.currentTag == 'IP':
            self.IP=False

        elif self.currentTag == 'PORT':
            self.PORT=False

        elif self.currentTag == 'TYPE':
            self.type = False

    def handle_startendtag(self, tag, attrs):
        '''
        处理 <br /> 这种标签的
        :param tag:
        :param attrs:
        :return:
        '''
        pass

def deal(content):
    cope=MyHTMLParser()
    cope.feed(content)
    count=0       #这里可以用大佬的enumerate（枚举）
    # for i in cope.all_info:
    #     count += 1
    #     print(i)
    #     if count % 4 == 0:
    #         print('-------------------------------------------------')

    return  cope.all_info


def refreshIP():
    freeIPUrl = 'https://www.kuaidaili.com/free/'
    r = requests.get(freeIPUrl,
                     # proxies = proxies,
                     headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
                     )  # 20s 超时

    with open('ip.html', 'w') as f:
        f.write(r.text)


s = ''
with open('ip.html', 'r') as f:
    s = f.read()

    # print(s)
res = deal(s)

def getProxyIP():

    oneIP  = random.choice(res)
    strHead = 'http' if oneIP['TYPE'] == 'HTTP' else 'https'
    value = 'http://' + oneIP['IP'] + ':' + oneIP['PORT']

    comb = {}
    comb[strHead] = value
    # print( comb )
    return comb



if __name__ == '__main__':

    # proxyIP = '124.235.145.79'

    proxies = {"http": "http://124.235.145.79:80", "https": "http://:8060", }


    one = getProxyIP()
    print(one)

