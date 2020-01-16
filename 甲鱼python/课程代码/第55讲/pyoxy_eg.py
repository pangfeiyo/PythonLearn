import urllib.request
import random

url = "http://www.whatismyip.com.tw"    # 显示当前访问他的来源IP

# 创建一个iplist，每次随机抽取里面的Ip地址作代理
iplist = ['182.129.240.150:9000','121.232.147.95:9000','180.118.92.227:9000']

# 设置代理Ip地址及端口
proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})

# 创建一个opener
opener = urllib.request.build_opener(proxy_support)
# headers 识别是否浏览器操作
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36')]
# 安装opener
urllib.request.install_opener(opener)

# 安装完成之后就可以以普通的形势来访问了
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)
