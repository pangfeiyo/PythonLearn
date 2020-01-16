# 补全
# try:
#     for i in range(3):
#         for j in range(3):
#             if i == 2:
#                 raise KeyboardInterrupt
#             print(i,j)
# except KeyboardInterrupt:
#     print("退出啦！")

import random
# 0.用户输入非整型数据，提示错误

# # import math
# # 1-10 随机数
# secret = random.randint(1,10)
# ''' 这个方法也可以， math模块中的ceil函数可以只保留整数位
# # secret = random.random() * 10 // 1
# # secret = math.ceil(ran)
#  '''
# print("--------------------")
# temp = input("猜一下数字：")
# try:
#     guess = int(temp)
# except ValueError:
#     print("输入错误！")
#     guess = secret
# while guess != secret:
#     temp = input("猜错了，继续：")
#     guess = int(temp)
#     if guess == secret:
#         print("猜对了")
#     else:
#         if guess > secret:
#             print("大了")
#         else:
#             print("小了")
# print("游戏结束")


# 1.input()函数有可能产生两类异常：EOFError（文件末尾endoffile,当用户按下组合键 Ctrl + D 产生）和
# Keyboardlnterrupt（取消输入，当用户按下组合键 Ctrl + C 产生），再次修改上边代码，捕获处理input()的两类异常，提高用户体验
# 1-10 随机数
# secret = random.randint(1,10)
# print("--------------------")
# try:
#     temp = input("猜一下数字：")
#     guess = int(temp)
# except (ValueError, EOFError, KeyboardInterrupt):
#     print("输入错误！")
#     guess = secret
# while guess != secret:
#     temp = input("猜错了，继续：")
#     guess = int(temp)
#     if guess == secret:
#         print("猜对了")
#     else:
#         if guess > secret:
#             print("大了")
#         else:
#             print("小了")
# print("游戏结束")


# 2.尝试一个新的函数 int_input()，当用户输入整数的时候正常返回，否则提示出错并要求重新输入：
def int_input(prompt=""):
    while True:
        try:
            int(input(prompt))
            break
        except:
            print("出错，输入的不是整数")
int_input('请输入一个整数：')


# 3.把文件关闭放在 finally 语句中执行还是会出现错误，例如要关闭的文件名不存在
# 如何修改
try:
    f = open('My_File.txt') # 当前文件夹中不存在这个文件
    print(f.read())
except OSError as reason:
    print("出错啦", str(reason))
finally:
    if 'f' in locals(): # 如果文件对象变量存在当前局部变量符号表的话，说明打开成功
        f.close()