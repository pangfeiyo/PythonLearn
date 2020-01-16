# headers 识别是否为浏览器发来的请求
'''
修改headers 两种方法
一、在Request对象生成之前，通过设置Request的headers参数修改
二、在Request对象生成之后，通过Request.add_header()方法修改
'''

'''
模拟真人操作，两种方法
一、使用 time.sleep 暂缓操作
二、挂代理
    1.参数是一个字典{'类型':'代理ip:端口号'}
    proxy_support = urllib.request.ProxyHandler({}) 
    2.定制、创建一个opener
    opener = urllib.request.build_opener(proxy_support)
        什么是opener？ 你可以看做是一个私人定制，当你使用urlopen打开一个普通网页的时候，你就是在使用默认的opener在工作
        而这个opener是可以定制的，可以给他加上特殊的headers或者给他指定相关代理，用build_opener来创建定制一个opener
    3a.安装 opener
    urllib.request.install_opener(opener)    安装到系统中，不再使用默认opener
    3b.调用 opener
    opener.open(url) 一般还是用默认，紧急或特殊情况才用定制opener
    
    这里看proxy_eg.py
'''

import urllib.request
import urllib.parse     # url解析模块
import json
import time # 使用 time.sleep  暂缓，模拟真人操作

while True:
    content = input("请输入需要翻译的内容（输入“q!”退出程序）：")
    if content == 'q!':
        break

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    # headers方法一
    '''
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
    '''

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

    # 在request对象生成之前设置好，做为参数传入进入
    '''req = urllib.request.Request(url, data, head)'''
    req = urllib.request.Request(url, data)
    # headers方法二   使用方法二， 上面的这条语句就不能在括号内加 ,head 了，因为前面没有生成head
    # 先生成一个request对象，再追加header
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36')

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

    print(req.headers)


    # 暂缓执行，单位为秒，这是为了模拟真人操作而不是代码操作
    time.sleep(5)



