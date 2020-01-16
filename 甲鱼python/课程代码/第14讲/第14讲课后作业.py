#定义一个跨越多行的字符字符串
#方法一
str1 = '''待我，将军？
此身，天后。
天光，莫非。
江南，红绳
'''
print(str1)
#方法二
str2 = '待我，将军？\
此身，天后。\
天光，莫非。\
江南，红绳'
print(str2)
#方法三
str3=('待我，将军？'
'此身，天后。'
'天光，莫非。'
'江南，红绳')
print(str3)

#三引号常用于跨行注释和代码

#打开一个文件
#因为可能会在路径中出现\t \r，\t 表示横向制表符（TAB）和“回车符”
#因此在路径前加上 r ，即可
file1 = open(r'C:\Users\PangFei\Desktop\甲鱼python学习\杂代码\供打开文件只读.txt','r')

#提取字符串中的网址
str4 = '<a href="http://www.fishc.com/dvd" target="_black">鱼C资源打包</a>'
print(str4[16:29])
#使用负数取出
print(str4[-45:-32])
#尝试输出
print(str4[20:-36])

#还原为有意义的字符串
str5 = "i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99"
print(str5[::3]) #从开始到结束切片，每次加3