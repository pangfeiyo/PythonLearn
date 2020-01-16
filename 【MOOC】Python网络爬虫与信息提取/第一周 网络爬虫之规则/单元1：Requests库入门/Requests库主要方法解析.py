'''
Requests库的7个主要方法
requests.request()      构造一个请求，支撑以下各方法的基础方法
requests.get()          获取HTML网页的主要方法，对应于HTTP的GET
requests.head()         获取HTML网页头信息的方法，对应于HTTP的HEAD
requests.post()         向HTML网页提交POST请求的方法，对应于HTTP的POST
requests.put()          向HTML网页提交PUT请求的方法，对应于HTTP的PUT
requests.patch()        向HTML网页提交局部修改请求，对应于HTTP的PATCH
requests.delete()       向HTML页面提交删除请求，对应于HTML的DELETE



requests.request(method, url, **kwargs)
  - method：请求方式，对应get/put/post等7种
  - 拟获取页面的url链接
  - **kwargs：另外的控制访问参数，共13个

  	- method：请求方式
  	  r = requests.request("GET", url, **kwargs)
  	  r = requests.request("HEAD", url, **kwargs)
  	  r = requests.request("POST", url, **kwargs)
  	  r = requests.request("PUT", url, **kwargs)
  	  r = requests.request("PATCH", url, **kwargs)
  	  r = requests.request("delete", url, **kwargs)
  	  r = requests.request("OPTIONS", url, **kwargs)	向服务器获取服务器能和客户端打交道的参数

  	- **kwargs：控制访问的参数，均为可选项
  	  params：字典或字节序列，作为参数增加到url中
  	  data：字典、字节序列或文件对象，作为Request的内容，向服务器提供或提交资源时使用
  	  json：JSON格式的数据，作为Request的内容
  	  headers：字典，HTTP定制头
      cookies：字典或CookieJar，Request中的cookie
      auth：元组，支持HTTP认证功能
      files：字典类型，传输文件
      timeout：设定超时时间，秒为单位
      proxies：字典类型，设定访问代理服务器，可以增加登录认证
      allow_redirects：True/False，默认为True，重定向开关
      stream：True/False，默认为True，获取内容立即下载开关
      verify：True/False，默认为True，认证SSL证书开关
      cert：本地SSL证书路径
'''
import requests

kv = {"key1":"value1", 'key2':'value2'}
r = requests.request("get", 'http://python123.io/ws', params=kv)
print(r.url)


kv = {"key1":"value1", 'key2':'value2'}
r = requests.request("post", 'http://python123.io/ws', data=kv)
body = '主体内容'
r = requests.request("post", 'http://python123.io/ws', data=body)


kv = {"key1":"value1"}
r = requests.request("post", 'http://python123.io/ws', json=kv)


# 模拟chrome10向服务器发起访问
hd = {'user-agent':'Chrome/10'}
r = requests.request('post', 'http://python123.io/ws', headers=hd)


fs = {'file':open('data.xls','rb')}
r = requests.request('post', 'http://python123.io/ws', file=fs)


r = requests.request('get', 'http://www.baidu.com', timeout=10)


pxs = {'http':'http://user:pass@10.10.10.1:1234',
       'https':'https://10.10.10.1:4321'}
r = requests.request('get', 'http://www.baidu.com', proxies=10)