# 演示HTML页面地址：http://python123.io/ws/demo.html
import requests

r = requests.get("http://python123.io/ws/demo.html")
# print(r.text)
demo = r.text

from bs4 import BeautifulSoup
# html.parser  解析器
soup = BeautifulSoup(demo, "html.parser")
print(soup.prettify())
