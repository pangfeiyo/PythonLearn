# 编写一个爬虫，爬取百度百科“网络爬虫”的词条
# 将所有包含"view"的链接按下边格式打印出来
'''
锁定 -> http://xxxx
网络爬虫 -> http://xxxx
FOAF -> http://xxxx
'''
'''
简单来说，Beautiful Soup是python的一个库，最主要的功能是从网页抓取数据。官方解释如下：
    Beautiful Soup提供一些简单的、python式的函数用来处理导航、搜索、修改分析树等功能。
    它是一个工具箱，通过解析文档为用户提供需要抓取的数据，因为简单，所以不需要多少代码就可以写出一个完整的应用程序。
    Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码。
    你不需要考虑编码方式，除非文档没有指定一个编码方式，这时，Beautiful Soup就不能自动识别编码方式了。
    然后，你仅仅需要说明一下原始编码方式就可以了。
    Beautiful Soup已成为和lxml、html6lib一样出色的python解释器，为用户灵活地提供不同的解析策略或强劲的速度。
'''
import urllib.request
import re   # 正则表达式模块
from bs4 import BeautifulSoup

def main1():
    url = "https://baike.baidu.com/item/%E6%AF%9B%E5%A7%93/631466?fromtitle=%E6%AF%9B&fromid=142887"
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")   # 使用 Python 默认解析器

    for each in soup.find_all(href=re.compile("view")):
        print(each.txet, "->", ''.join(["http://baike.baidu.com", each["href"]]))
        # 上边用 join() 不用 + 直接拼接，是因为 join() 被证明执行效率要高很多


# 允许用户输入搜索的关键词
def main2():
    keyword = input("请输入关键词：")
    keyword = urllib.parse.urlencode({"word": keyword})
    response = urllib.request.urlopen("http://baike.baidu.com/search/word?%s" % keyword)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")

    for each in soup.find_all(href=re.compile("view")):
        content = ''.join([each.text])
        url2 = ''.join(["http://baike.baidu.com", each["href"]])
        response2 = urllib.request.urlopen(url2)
        html2 = response2.read()
        soup2 = BeautifulSoup(html2, "html.parser")
        if soup2.h2:
            content = ''.join([content, soup2.h2.text])
        content = ''.join([content, " -> ", url2])
        print(content)


# 先打印10个链接，然后问用户还要不要再继续看
def test_url(soup):
    result = soup.find(text=re.compile("百度百科尚未收录词条"))
    if result:
        print(result[0:-1])  # 百度这个碧池在最后加了个“符号，给它去掉
        return False
    else:
        return True


def summary(soup):
    word = soup.h1.text
    # 如果存在副标题，一起打印
    if soup.h2:
        word += soup.h2.text
    # 打印标题
    print(word)
    # 打印简介
    if soup.find(class_="lemma-summary"):
        print(soup.find(class_="lemma-summary").text)


def get_urls(soup):
    for each in soup.find_all(href=re.compile("view")):
        content = ''.join([each.text])
        url2 = ''.join(["http://baike.baidu.com", each["href"]])
        response2 = urllib.request.urlopen(url2)
        html2 = response2.read()
        soup2 = BeautifulSoup(html2, "html.parser")
        if soup2.h2:
            content = ''.join([content, soup2.h2.text])
        content = ''.join([content, " -> ", url2])
        yield content


def main3():
    word = input("请输入关键词：")
    keyword = urllib.parse.urlencode({"word": word})
    response = urllib.request.urlopen("http://baike.baidu.com/search/word?%s" % keyword)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")

    if test_url(soup):
        summary(soup)

        print("下边打印相关链接：")
        each = get_urls(soup)
        while True:
            try:
                for i in range(10):
                    print(next(each))
            except StopIteration:
                break

            command = input("输入任意字符将继续打印，q退出程序：")
            if command == 'q':
                break
            else:
                continue



num = input("请输入序号：")
if num == "1":
    main1()
if num == "2":
    main2()
if num == "3":
    main3()