'''
<f>.read(size=-1)       读入全部内容，如果给出参数，读入前size长度
<f>.readline(size=-1)   读入一行内容，如果给出参数，读入该行前size长度
<f>.readlines(hint=-1)  读入文件所有行，以每行为元素形成列表。如果给出参数，读入前hint行
'''

f = open("f.txt")
s = f.read(2)
print(s)
f.close()   # 不关闭的话会影响指针

f = open("f.txt")
s = f.readline()
print(s)
f.close()

f = open("f.txt")
s = f.readlines()
print(s)
f.close()



# 文件的全文本操作
# 遍历全文本：方法一
fname = 'f.txt'
fo = open(fname, 'r')
# 对全文本txt进行处理
txt = fo.read()      # 一次读入，统一处理
fo.close()


# 遍历全文本：方法二
# 读数量读入，逐步处理，可以处理大文件
fname = 'f.txt'
fo = open(fname, 'r')
txt = fo.read(2)
while txt != "":
    # 对txt进行处理
    txt = fo.read(2)
fo.close()



# 文件的逐行操作
# 逐行遍历文件：方法一
fname = 'f.txt'
fo = open(fname, 'r')
for line in fo.readlines():
    print(line)
fo.close()


# 逐行遍历文件：方法二
# 分行读入，逐行处理，对极大文件处理很有效
fname = 'f.txt'
fo = open(fname, 'r')
for line in fo:
    print(line)
fo.close()


'''
数据的文件写入
<f>.write(s)            向文件写入一个字符串或字节流
<f>.writelines(lines)   将一个元素全为字符串的列表写入文件，将列表内容拼接写入文件
<f>.seek(offset)        改变当前文件操作指针的位置，offset含义如下：
                        0 - 文件开头； 1 - 当前位置； 2 - 文件结尾
'''
f = open("f.txt",'a')
f.write("\n中国是一个伟大的国家！")
f.close()


fo = open('output.txt', 'w+')
ls = ['中国','美国','法国']
fo.writelines(ls)   # 写入一个字符串列表
fo.seek(0)
for line in fo:
    print(line)
fo.close()

# f.seek(0) 回到文件开头