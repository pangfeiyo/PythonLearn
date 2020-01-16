'''
百度的关键词接口：
http://www.baidu.com/s?wd=keyword

360的关键词接口：
http://www.so.com/s?q=keyword

'''
import requests

def baidu():
    keyword = "Python"
    try:
        kv = {'wd':keyword}
        r = requests.get("http://www.baidu.com/s", params=kv)
        # 发给百度的request，对应的url是什么
        print(r.request.url)
        print(r.raise_for_status())
        print(len(r.text))
        print(r.text)
    except:
        print("爬取失败")


def soq():
    keyword = "Python"
    try:
        kv = {'q':keyword}
        r = requests.get("http://www.so.com/s", params=kv)
        # 发给百度的request，对应的url是什么
        print(r.request.url)
        print(r.raise_for_status())
        print(len(r.text))
        print(r.text)
    except:
        print("爬取失败")

baidu()
# soq()