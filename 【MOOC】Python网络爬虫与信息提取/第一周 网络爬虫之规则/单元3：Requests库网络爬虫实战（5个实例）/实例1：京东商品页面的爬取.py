import requests

url = "https://item.jd.com/7348367.html"
try:
    r = requests.get(url)
    # 返回状态码，200是正常
    print(r.status_code)
    # 改变编码为 apparent_encoding从内容中分析出的响应内容编码方式（备选编码方式）
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")