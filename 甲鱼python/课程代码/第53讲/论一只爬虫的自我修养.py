import urllib.request

response = urllib.request.urlopen("http://www.fishC.com")
# 只能用read读取
html = response.read()
print(html)
# 打印出字符串，b开头的，二进制字符串

# 对其进行解码，就是正常的HTML代码
html = html.decode("utf-8")
print(html)