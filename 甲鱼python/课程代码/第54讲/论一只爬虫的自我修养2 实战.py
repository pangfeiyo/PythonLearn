import urllib.request

response = urllib.request.urlopen("http://placekitten.com/g/200/300")

cat_img = response.read()

with open('cat_500_600.jpg','wb')as f:
    f.write(cat_img)

# 写法二  使用Request
# req = urllib.request.Request("http://placekitten.com/g/200/300")
# response = urllib.request.urlopen(req)
# cat_img = response.read()
# with open('cat_500_600.jpg','wb')as f:
#     f.write(cat_img)





import urllib.parse     # url解析模块
import json

content = input("请输入需要翻译的内容：")

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {}
data['i'] = content
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '1517452803993'
data['sign'] = 'ce63d1250f723037d2446b795236e386'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTION'
data['typoResult'] = 'false'

data = urllib.parse.urlencode(data).encode("utf-8")

response = urllib.request.urlopen(url, data)
html = response.read().decode('utf-8')  # windows下可以不输入这个.decode('utf-8")

print(html)

# json.loads 对数据进行解码
target = json.loads(html)
print(type(target))
print(target)
print(target['translateResult'])
print(target['translateResult'][0][0])
print(target['translateResult'][0][0]['tgt'])
target = target['translateResult'][0][0]['tgt']
print("翻译结果为：%s" % target)