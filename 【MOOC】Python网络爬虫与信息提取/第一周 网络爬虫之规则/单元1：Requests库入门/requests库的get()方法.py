'''
requests.get()          获取HTML网页的主要方法，对应于HTTP的GET
requests.get(url, params=None, **kwargs)
  - url：拟获取页面的url链接
  - params：url中的额外参数，字典和字节流格式，可选
  - **kwaargs：12个控制访问的参数


Response对象的属性
r.status_code       HTTP请求的返回状态，200表示连接成功，404表示失败
r.text              HTTP响应内容的字符串形式，即，url对应的页面内容
r.encoding          从HTTPheader中猜测的响应内容编码方式
r.apparent_encoding 从内容中分析出的响应内容编码方式（备选编码方式）
r.content           HTTP响应内容的二进制形式
'''
import requests

r = requests.get("http://www.baidu.com")
print(r.status_code)
print(r.text)
# 打印出来的是乱码，这时候看一下编码
# 如果header中不存在charset，则认为编码为ISO-8859-1
print(r.encoding)

# 看一下另外一个编码
print(r.apparent_encoding)
# 用备选编码来替换
r.encoding = 'utf-8'
print(r.text)