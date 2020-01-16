# 模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。
# 模块可以被别的程序引入，以使用该模块中的函数等功能。
import os
import random
sercet = random.randint(1,10)
print(sercet)

# C:\Users\PangFei\Desktop\Python学习\甲鱼python\课程代码\第30讲
# OS模块

# 返回当前工作目录
print(os.getcwd())
# 改变工作目录，转到D盘下    ch，change
os.chdir('d:\\')
print(os.getcwd())
os.chdir(r'C:\Users\PangFei\Desktop\Python学习\甲鱼python\课程代码\第30讲')
print(os.getcwd())
# 列举指定目录中的文件名（"." 表示当前目录 ，".."表示上一级目录）
print(os.listdir('d:\\'))
# 创建单层目录，如该目录已存在抛出异常
os.mkdir(r'C:\Users\PangFei\Desktop\Python学习\甲鱼python\课程代码\第30讲\测试目录')
# 递归创建多层目录，如该目录已存在抛出异常（注意：'E:\\a\\b'和 'E:\\a\\c'并不会冲突）
  # 这里和上一条会冲突，因为上一条代码已经创建了“测试目录”，所以要先删掉该目录
os.rmdir(r'C:\Users\PangFei\Desktop\Python学习\甲鱼python\课程代码\第30讲\测试目录')  # 理论这该语句在第二次运行时应该优先执行
# 递归创建多层目录
os.makedirs(r'C:\Users\PangFei\Desktop\Python学习\甲鱼python\课程代码\第30讲\测试目录\子目录1\次子目录')
# 创建一个 .txt 文件
f = open(r'C:\Users\PangFei\Desktop\Python学习\甲鱼python\课程代码\第30讲\测试目录\子目录1\次子目录\test1.txt','w')
f.close()
# 文件重命名
os.rename(r'C:\Users\PangFei\Desktop\Python学习\甲鱼python\课程代码\第30讲\测试目录\子目录1\次子目录\test1.txt',
          r'C:\Users\PangFei\Desktop\Python学习\甲鱼python\课程代码\第30讲\测试目录\子目录1\次子目录\test2.txt')
# 删除单层目录，如该目录非空则抛出异常
  # 因为要删除“子目录1”与“次子目录”，所以应该先把这两目录中的文件删除
  # 删除 tst1.txt 文件
os.remove(r'C:\Users\PangFei\Desktop\Python学习\甲鱼python\课程代码\第30讲\测试目录\子目录1\次子目录\test2.txt')
  # 删除单层目录（需一级一级删）
# os.rmdir(r'C:\Users\PangFei\Desktop\Python学习\甲鱼python\课程代码\第30讲\测试目录\子目录1\次子目录')
# os.rmdir(r'C:\Users\PangFei\Desktop\Python学习\甲鱼python\课程代码\第30讲\测试目录\子目录1')
# 递归删除目录，从子目录到父目录逐层尝试删除，遇到目录非空抛出异常
os.removedirs(r'C:\Users\PangFei\Desktop\Python学习\甲鱼python\课程代码\第30讲\测试目录\子目录1\次子目录')

# 运行系统的shell命令
# os.system('cmd')
# os.system('calc')   # 计算器


# 以下是支持路径操作中常用到的一些定义，支持所有平台
# 指代当前目录 “.”
print(os.curdir)
# 显示当前目录下的所有文件
print(os.listdir(os.curdir))
# 指代上一级目录 “..”
print(os.pardir)
print(os.listdir(os.pardir))
# 输入操作系统特定的路径分隔符（WIN下是“\\”，Liunx下为“/”）
print(os.sep)
# 输入操作系统特定的行终止符（WIN下是“\r\n”，Liunx下为“\n”）
print(os.linesep)
# 指代当前使用的操作系统（包括：'posix','nt','mac','os2','ce','java'）
print(os.name)