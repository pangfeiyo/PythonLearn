# 常见的三种读文件方式：
# a.read(size)    a.readline(size)      a.readlines(hint)

# 常用的三咱写文件方式：
# a.write(s)      a.writelines(lines)   a.seek(offset)

'''
文件的打开模式
r       只读模式，默认值，如果文件不存在，返回FileNotFoundError
w       覆盖写模式，文件不存在则创建，存在则完全覆盖
x       创建写模式，文件不存在则创建，存在则返回FileExistsError
a       追加写模式，文件不存在则创建，存在则在文件最后追加内容
b       二进制文件模式
t       文本文件模式，默认值
+       与r/w/x/a一同使用，在原功能基础上增加同时读写功能

f = open("f.txt")            文本形式、只读模式、默认值
f = open("f.txt", 'rt')      文本形式、只读模式、同默认值
f = open("f.txt", 'w')       文本形式、覆盖写模式
f = open("f.txt", 'a+')      文本形式、追加写模式+读文件
f = open("f.txt", 'x')       文本形式、创建写模式
f = open("f.txt", 'b')       二进制形式、只读模式
f = open("f.txt", 'wb')      二进制形式、覆盖写模式

文件关闭
<变量名>.close()
'''