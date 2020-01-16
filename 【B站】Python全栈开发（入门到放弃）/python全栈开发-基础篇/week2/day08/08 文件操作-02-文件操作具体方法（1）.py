# 按行拿内容
f = open("小重山.txt",'r')

# readline 单行
print(f.readline())
print(f.readline())

# readlines 多行   输出结果是列表类型
print(f.readlines())
f.close()

print()



# 利用readlines的列表，输出结果
f = open("小重山.txt",'r')
for i in f.readlines():
    print(i.strip())    # 字符串方法，去空格
f.close()
# 加strip()是因为每行后面都有一个\n


print()

# 给第六行内容最后加字符串
number = 0
f = open("小重山.txt",'r')
for i in f.readlines():
    number+=1
    if number == 6:
        # i = i.strip() + 'ikeit'
        i = " ".join([i.strip(),"iiiii"])   # 取代 +  
    print(i.strip())

f.close()