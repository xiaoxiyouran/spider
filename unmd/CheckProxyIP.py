#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
filename: CheckProxyIP.py
message:
检查以下代理ip 是否可用
platform: pyhon 3.5
'''

__author__ = 'xi'

import telnetlib

def checkProxyIP( proxy_ip, port ):
    try:
        telnetlib.Telnet(proxy_ip, port=port, timeout=20)
    except:
        print ( '%s:%s connect failed' % (proxy_ip, port) )
        return False;
    else:
        print ( '%s:%s connect success' % (proxy_ip, port) )
        return True;

if __name__ == '__main__':
    proxyIP = '117.21.191.154'
    port = '32340'
    checkProxyIP(proxyIP, port);

