# 02 使用python加代理刷流量

## 关于刷流量

做开发的有的时候会被拜托一些特殊的业务。 
比如说刷票，但是你又不好拒绝，比如你钟情的美女突然有一天拜托你刷票。 
这个时候就开发一个刷票工具了。 
python 还是非常强大的。非常方便。

<br>

## 使用python

不是使用原生的url2访问，而是使用requests库。 
比较方便一点，方便编程。参数比较详细。 
参考文档： 
http://docs.python-requests.org/zh_CN/latest/ 
使用一个高级特性**代理**: 

http://docs.python-requests.org/zh_CN/latest/user/advanced.html#proxies

<br>

## 实现

需要安装 requests 库 , 如果没有安装，使用以下指令安装

```python
sudo easy_install pip
sudo pip install requests
```

使用代理服务器访问csdn网站。 
这样的ip就变成代理服务器的ip了。 
有个问题。代理服务器的ip和端口从哪里查询呢？有个这样的网站 
http://www.kuaidaili.com/free/ 
上面的代理很好用，反正是用来刷的，搜索些免费的就行。

把上面的代理服务器的ip和端口保存下来然后在配合脚本就可以了。 

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 需要安装 requests 库 :
# sudo easy_install pip
# sudo pip install requests
import requests


for i in range(1, 10):
    proxies = {
        "http": "http://117.21.191.154:32340",
        "http": "http://58.251.49.4:58729"
    }
    url = "http://m.csdn.net/index.html"
    print(url)
    req = requests.get(url)
    # 设置编码
    req.encoding = 'utf-8'
    print(req.text)
```

如果增加参数可以随机几个agent和参数

```python
headers = {
        "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2454.85 Safari/537.36"
    }
req = requests.get(url, headers=headers, params={})
```

requests类库还是非常强大的。然后就可以根据每一个网站进行分析了。

<br>

## 参考

1- https://blog.csdn.net/freewebsys/article/details/52999166

2- https://blog.csdn.net/c406495762/article/details/60137956

3- https://www.jianshu.com/p/588241a313e7

4- [使用 Python 进行HTTP代理 多线程刷(投)票](https://blog.csdn.net/Relocy/article/details/51533302?utm_source=blogxgwz5) 

5- [PYTHON实现刷流量工具](https://blog.csdn.net/boksic/article/details/16870453?utm_source=blogxgwz3)

6- [python通过代理刷网页点击量](https://blog.csdn.net/chenfei_5201213/article/details/9327063?utm_source=blogxgwz1)

7- [使用python加代理刷流量](https://blog.csdn.net/freewebsys/article/details/52999166)



