# os.path 模块中关于路径常用的函数使用方法
# 去掉目录路径，单独返回文件名
import os
ospath = 'C:\\Users\\PangFei\\Desktop\\Python学习\\甲鱼python\\课程代码\\第30讲\\os.path模块.py'
print(os.path.basename(ospath))
# 去掉文件名，只返回路径
print(os.path.dirname(ospath))
# 将path1, path2 各部分组合成一个路径名
print(os.path.join('D:\\','A','B','C'))
# 分割文件和路径（如果完全使用目录，也会将最后一个目录作为文件名分离，且不会判断文件或者目录是否存在）
print(os.path.split(ospath))
print(os.path.split(r'C:\Users\PangFei\Desktop\Python学习\甲鱼python\课程代码\第30讲'))
# 分离文件名和扩展名
print(os.path.splitext(r'D:\A\test1.txt'))
# 返回指定文件的尺寸，单位是字节
print(os.path.getsize(ospath))


# 返回指定文件最近的访问时间（浮点型秒数，可用time模块的 gmtime() 或 localtime() 函数换算）
getatime = os.path.getatime(ospath)
print(getatime)
# time 模块
import time
# time.gmtime() 函数将一个时间戳转换为UTC时区（英国的0时区）
print(time.gmtime(getatime))
# time.localtime() 本地时间
print(time.localtime(getatime))
# 返回指定文件的创建时间（浮点型秒数，可用time模块的 gmtime() 或 localtime() 函数换算）
getctime = os.path.getctime(ospath)
print(getctime)
print(time.localtime(getctime))
# 返回指定文件最新的修改时间（浮点型秒数，可用time模块的 gmtime() 或 localtime() 函数换算）
getmtime = os.path.getmtime(ospath)
print(getmtime)


# 以下函数返回True或False
# 判定指定路径（目录或文件）是否存在
print(os.path.exists(ospath))
# 判断指定路径是否为绝对路径
# 相对与绝对路径区别：
#  - 相对：  A\\B\\test.txt     ..\\C\\1.txt
#  - 绝对：  D:\\A\\B\\test.txt
print(os.path.isabs(ospath))
# 是否存在且是一个目录
# os.path.isdir(path)
# 是否存在且是一个文件
# os.path.isfile(path)
# 是否存在且是一个符号链接（在win上指是否为一个快捷方式）
# os.path.islink(path)
# 是否存在且是一个挂载点（A盘B盘C盘D盘等等）
print('挂载点 E:\\  ',os.path.ismount('E:\\'))
print('挂载点 E:\\a ',os.path.ismount('E:\\a'))
# 判断path1和path2是否指向同一个文件
# os.path.somefile(path1, path2)
