'''
获取或改变系统环境信息

os.chdir(path)      修改当前程序操作的路径
os.getcwd()         返回程序的当前路径
os.getlogin()       获得当前系统登录用户名称
os.cpu_count()      获得当前系统的CPU数量
os.urandom(n)       获得n个字节长度的随机字符串，通常用于加解密运算
'''
import os

os.chdir('d:\\')
print(os.getcwd())

print(os.getlogin())

print(os.cpu_count())

print(os.urandom(10))