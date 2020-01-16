# f1 = open(file1)    # 这里不需要对 file1 和 file2 进行写入操作，所以用默认即可
# f2 = open(file2)
# count = 0 # 统计行数
# differ = [] # 统计不一样的数量
# for line1 in f1:
#     line2 = f2.readline()   # 读取并返回一行
#     count += 1
#     if line1 != line2:
#         differ.append(count)

# f1.close()
# f2.close()
# return differ
f = open('boy_1.txt')
count = 0
for line in f:
    count += 1
    print(line)
    if count == 1:
        break

