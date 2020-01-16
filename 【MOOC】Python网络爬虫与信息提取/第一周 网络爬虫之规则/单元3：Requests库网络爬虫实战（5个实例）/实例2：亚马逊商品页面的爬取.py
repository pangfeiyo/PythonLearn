import requests

# url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
# r = requests.get(url)
# print(r.raise_for_status())
# r.encoding = r.apparent_encoding
# print(r.text[:1000])
'''
这里有可能会出现503，访问失败
  - 尝试1：改变编码为utf-8，返回页面提示“由于程序执行时，遇到意外错误，操作没有成功”，且英文字段出现“api”字段
           亚马逊说访问出现错误，而且是由API造成的
  - 尝试2：很多网站对网络爬虫有限制，在RoBots协议告知爬虫哪些可以访问
           还有一种方法比较隐性，通过判定对网站访问HTTP的头来查看你的访问是不是由一个爬虫引起的
           网站一般接收由浏览器引发的或者产生的HTTP请求，对于爬虫请求网站可以拒绝
'''
# 查看requests信息的头部内容
# print(r.request.headers)
# 头部中有个字段叫User-Agent，告诉亚马逊这次访问是由python库的一个程序造成的
# 修改头，模拟浏览器向亚马逊发起请求
# Mozilla/5.0 是个很标准的浏览器身份标识，可能有chrome/火狐/ie等
url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
try:
    kv = {"user-agent":'Mozilla/5.0'}
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print("失败")