import requests
import os

url = 'http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg'
path = url.split("/")[-1]
try:
    # exists() 如果存在返回True
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            # 图片是二进制格式，如何保存？
            # r.content 表示  返回内容的二进制形式
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")
