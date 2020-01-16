# 使用 open 这个函数打开文件，并返回文件对象
# help(open)

# 使用 \\   或  /  都可以，双 \\ 是为了转义，转义一个\
# f = open('C:/Users/PangFei/Desktop/Python学习/甲鱼python/课程代码/第28讲/record.txt')
f = open('C:\\Users\\PangFei\\Desktop\\Python学习\\甲鱼python\\课程代码\\第28讲\\record.txt')
# 将返回从文件指针开始（注意这里并不是文件头）的连续 ？ 个字符，如果没有参数即指全部
print(f.read())
# 再来一次 f.read() ，因为之前读取了全部，所以指针现在在末尾，从末尾开始读就是空的
print(f.read())
# 用完要记得关闭
f.close()

#读取前5个字符
f = open('C:\\Users\\PangFei\\Desktop\\Python学习\\甲鱼python\\课程代码\\第28讲\\record.txt')
print(f.read(5))
# 返回当前在文件中的位置，这里返回值是 9 ， 因为一个中文占两个字节，上面的 f.read(5)读出了 1.人最宝
print(f.tell())

# f.seek(offset, from)
# 在文件中移动文件指针，从 from（ 0 代表文件起始位置，1 代表当前位置， 2 代表文件末尾）偏移 offset 个字节
f.seek(45,0)    # print(f.seek(45,0))  返回值是45
print(f.readline())     # 一行一行读

# 迭代读取文本中的每一行，数据量越大，此方法越没有效率
print("-- 迭代读取每一行 --")
f.seek(0,0) # 重置偏移，因为上面偏移了45
lines = list(f)
for each_line in lines:
    print(each_line)

# 优化方法，直接用 For （官方文档推荐）
print("\n-- 优化迭代 --")
f.seek(0,0)
for each_line in f:
    print(each_line)

f.close()

# 用列表读
# 如果不先在上面把 f 给关闭再重新打开，下面的 list 读取出来的是从 2. 开始的
print("\n-- 用列表读 --")
f = open('C:\\Users\\PangFei\\Desktop\\Python学习\\甲鱼python\\课程代码\\第28讲\\record.txt')
print(list(f))
f.close()


# 文件的写入
# f.write(str)  将字符串 str 写入文件
# f.writelines(seq)  向文件写入字符串序列seq, seq 应该是一个返回字符串的可迭代对象
# 'w',以写入方式打开文件，会覆盖已存在的文件，若不存在则会创建一个新文件
f = open('C:\\Users\\PangFei\\Desktop\\Python学习\\甲鱼python\\课程代码\\第28讲\\test.txt','w')
f.write("我爱鱼C工作室!")      # print(f.write("我爱鱼C工作室"))    返回值为 7 ，显示你输出了 7 个字符
f.close()