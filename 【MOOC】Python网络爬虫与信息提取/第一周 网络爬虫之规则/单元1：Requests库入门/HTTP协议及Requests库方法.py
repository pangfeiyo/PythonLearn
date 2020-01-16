import requests

# 访问百度
r = requests.get("http://www.baidu.com")
# 状态码
# print(r.status_code)    # 返回值是200，代表访问成功
# 更改编码
r.encoding = "utf-8"
# print(r.text)

'''
Requests库的7个主要方法
requests.request()      构造一个请求，支撑以下各方法的基础方法
requests.get()          获取HTML网页的主要方法，对应于HTTP的GET
requests.head()         获取HTML网页头信息的方法，对应于HTTP的HEAD
requests.post()         向HTML网页提交POST请求的方法，对应于HTTP的POST
requests.put()          向HTML网页提交PUT请求的方法，对应于HTTP的PUT
requests.patch()        向HTML网页提交局部修改请求，对应于HTTP的PATCH
requests.delete()       向HTML页面提交删除请求，对应于HTML的DELETE


HTTP协议对资源的操作
GET         请求获取URL位置的资源
HEAD        请求获取URL位置资源的响应消息报告，即获得该资源头部信息
POST        请求向URL位置的资源后附加新的数据
PUT         请求向URL位置存储一个资源，覆盖原URL位置的资源
PATCH       请求局部更新URL位置的资源，即改变该处资源的部分内容
DELETE      请求删除URL位置存储的资源


          GET   HEAD
个 <----------------------- 云
             URL
人 -----------------------> 端
    PUT POST PATCH DELETE
    
    
理解PATCH和PUT的区别
假设URL位置有一组数据UserInfo，包括UserID、UserName等20个字段
需求：用户修改了UserName，其他不变
  - 采用PATCH，仅向URL提交UserName的局部更新请求。
  - 采用PUT，必须将所有20个字段一并提交到URL，未提交字段被删除

'''

# Requests库的head()方法
r = requests.head("http://www.baidu.com")
# print(r.headers)

# Requests库的post()方法   向服务器提交新增数据
# 向URL POST一个字典  自动编码为form（表单）
payload = {'key1':'value1', 'key2':'value2'}
r = requests.post('http://httpbin.org/post', data=payload)
# print(r.text)

# 向URL POST一个字符串  自动编码为data
r = requests.post("http://httpbin.org/post", data="ABC")
print(r.text)