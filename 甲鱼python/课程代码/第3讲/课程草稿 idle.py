'''
Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 5+8
13
>>> '5'+8
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    '5'+8
TypeError: must be str, not int
>>> '5'+'8'
'58'
>>> print("let's go")
let's go
>>> print('let's go')
      
SyntaxError: invalid syntax
>>> print('let\'s go')
let's go
>>> str = 'c:\now'
>>> print(str)
c:
ow
>>> str = 'c:\\now'
>>> str
'c:\\now'
>>> print(str)
c:\now
>>> str = r'c:\now'
>>> str
'c:\\now'
>>> print(str)
c:\now
>>> str = '''一地在要工

上是中国同

和的有人我
主产不为这
民了发以经

'''
>>> str
'一地在要工\n\n上是中国同\n\n和的有人我\n主产不为这\n民了发以经\n\n'
>>> print(str)
一地在要工

上是中国同

和的有人我
主产不为这
民了发以经


>>> str = '''一地在要工

上是中国同

和的有人我
主产不为这
民了发以经

'''
>>> print(str)
一地在要工

上是中国同

和的有人我
主产不为这
民了发以经


>>> str = '''一地在要工
上是中国同
和的有人我
主产不为这

民了以经经
'''
>>> str
'一地在要工\n上是中国同\n和的有人我\n主产不为这\n\n民了以经经\n'
>>> print(str)
一地在要工
上是中国同
和的有人我
主产不为这

民了以经经

>>> str = '''
gfds
'''
>>> str
'\ngfds\n'
>>> print(str)

gfds

>>> str="""一地在要工

上是中国同
和的有人我

主产不为这

民了发以经
"""
>>> str
'一地在要工\n\n上是中国同\n和的有人我\n\n主产不为这\n\n民了发以经\n'
>>> print(str)
一地在要工

上是中国同
和的有人我

主产不为这

民了发以经

>>> str='''【黄瓜】次(262985698) 13:38:13
第一个
【肥皂】字幕君(792200488) 13:39:02
我去年盖的还有更糊的
【肥皂】字幕君(792200488) 13:39:18
就TM外面一圈红印
【肥皂】字幕君(792200488) 13:40:35
领补贴他们会仔细看么    很担心啊
'''
>>> print(str)
【黄瓜】次(262985698) 13:38:13
第一个
【肥皂】字幕君(792200488) 13:39:02
我去年盖的还有更糊的
【肥皂】字幕君(792200488) 13:39:18
就TM外面一圈红印
【肥皂】字幕君(792200488) 13:40:35
领补贴他们会仔细看么    很担心啊

>>> str = '''gfdsa
hjkl;
qwewr
upyiu
bxcbx
'''
>>> print(str)
gfdsa
hjkl;
qwewr
upyiu
bxcbx

>>> 
>>> name= input("请输入您的姓名：")
请输入您的姓名：
========= RESTART: C:/Users/PangFei/Desktop/甲鱼python/课程代码/第三讲/hello.py =========
请输入您的姓名
========= RESTART: C:/Users/PangFei/Desktop/甲鱼python/课程代码/第三讲/hello.py =========
请输入您的姓名：甲鱼
你好，甲鱼
>>> 
========= RESTART: C:/Users/PangFei/Desktop/甲鱼python/课程代码/第三讲/hello.py =========
请输入您的姓名：123
你好，123!
>>> 
==== RESTART: C:/Users/PangFei/Desktop/甲鱼python/课程代码/第三讲/要求用户输入1~100并判定.py ====
请输入1到100之间的数字：999
错误
>>> 
==== RESTART: C:/Users/PangFei/Desktop/甲鱼python/课程代码/第三讲/要求用户输入1~100并判定.py ====
请输入1到100之间的数字：5
正确
>>> 


'''
