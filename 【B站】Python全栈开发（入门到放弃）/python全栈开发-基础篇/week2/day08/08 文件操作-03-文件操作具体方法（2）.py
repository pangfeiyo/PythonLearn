# 只读
f = open("小重山.txt",'r')
for i in f: # 这是for内部将f对象做成一个迭代器，用一行取一行
    print(i.strip())

f.close()

print()

# 检测当前光标位置  tell()
f = open("小重山.txt",'r')
print(f.tell()) # 显示当前光标位置
print(f.read(2))
print(f.tell())


print()
# 调整光标位置
f.seek(0)	# 回到初始位置
print(f.read(4))

