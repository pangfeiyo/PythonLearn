# 下载鱼C首页（http://www.fishC.com），并打印前三百个字节
import urllib.request
response = urllib.request.urlopen("http://www.fishC.com")
response = response.read(300)
print(response)
# decode(encoding="utf-8", errors="strict")方法以encoding指定的编码格式解码字符串。默认编码为字符串编码
response = response.decode("utf-8")
print("\n"+ response)


# 写一个程序，检测指定URL的编码
import urllib.request
import chardet  # 第三方库，python2和3的通用编码检测器

def main():
    url = input("\n请输入URL：")
    # url要加上http://等协议开头
    response = urllib.request.urlopen(url)
    html = response.read()

    # 识别网页编码
    # 这里为什么要加上['encoding']和下面的if
    # 因为文档中给出的用法中是不加[]的，但返回结果是一个字典，字典开头就是encoding，后面的参数暂时用不到，所以这里只取第一个，打印出字典键encoding的值
    encode = chardet.detect(html)['encoding']
    if encode == "GB2312":
        encode = "GBK"

    print("该页面使用的编码是：%s" % encode)


# 写一个程序，依次访问文件中指定的站点，并将每个站点返回的内容依次存放到不同的文件中
def main2():
    i = 0

    # r 只读， 
    with open("urls.txt", "r") as f:
        # 读取待访问的网址
        # 由于urls.txt每一行一个url
        # 所以按换行符'\n'分割
        urls = f.read().splitlines()
    
    for each_url in urls:
        response = urllib.request.urlopen(each_url)
        html = response.read()

        # 识别网页编码
        encode = chardet.detect(html)['encoding']
        if encode == "GB2312":
            encode = 'GBK'

        i += 1
        filename = "url_%d.txt" % i

        with open(filename,"w", encoding = encode) as each_file:
            # encode() 方法以指定的编码格式编码字符串。errors参数可以指定不同的错误处理方案。
            each_file.write(html.decode(encode, "ignore"))

number = input("请输入要执行的代码段编号: ")
if number == "1":
    main()
if number == "2":
    main2()