'''
os库基本介绍 
os库提供通用的、基本的操作系统交互功能
  - 路径操作：os.path子库，处理文件路径及信息
  - 进程管理：启动系统中其他程序 
  - 环境参数：获得系统软硬件信息等环境参数


os.path.abspath(path)       返回path在当前系统中的绝对路径
os.path.normpath(path)      归一代path的表示形式，统一用\\分隔路径
os.path.relpath(path)       返回当前程序与文件之间的相对路径(relative path)
os.path.dirname(path)       返回path中的目录名称
os.path.basename(path)      返回path中最后的文件名称
os.path.join(path, *paths)  组合path与paths，返回一个路径字符串   
os.path.exists(path)        判断path对应文件或目录是否存在，返回True或False
os.path.isfile(path)        判断path所对应是否为已存在的文件，返回True或False
os.path.isdir(path)         判断path所对应是否为已存在的目录，返回True或False

os.path.getatime(path)      返回path对应文件或目录上一次的访问时间
os.path.getmtime(path)      返回path对应文件或目录最近一次的修改时间
os.path.getctime(path)      返回path对应文件或目录的创建时间
os.path.getsize(path)       返回path对应文件的大小，以字节为单位
'''


from os import path as op
import time

ospath = op.abspath("os库之路径操作.py")
print(ospath)

print(op.normpath("D://PYE//file.txt"))

print(op.relpath(r"C:\Users\PangFei\Desktop\PythonLearn\【mooc】Python语言程序设计\第7周 文件和数据格式化\7.1 文件的使用"))

print(op.dirname("D://PYE//file.txt"))

print(op.basename("D://PYE//file.txt"))

print(op.join("D:/", "PYE/file.txt"))

print(op.exists("D://PYE//file.txt"))

print(op.isfile("D://PYE//file.txt"))

print(op.isdir("D://PYE//file.txt"))    # 这里是文件，不是目录，所以False

print(op.getatime(ospath))
print(op.getmtime(ospath))
print(time.ctime(op.getctime(ospath)))  # time.ctime 把一个表示时间的元组或者struct_time表示为这种形式：'Sun Jun 20 23:21:05 1993'。
print(op.getsize(ospath))