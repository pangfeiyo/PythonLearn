#用for 打印1 到20

#简单方法
values = []
for value in range(1,21):
    values.append(value)
print('简单方法：',values)

#列表解析
values = [value for value in range(1,21)]
print('列表解析：',values)

#包含1~1 000 000，如果时间过长，使用ctrl+c停止或关闭窗口
#values = [value for value in range(1,10000001)]
#print('列表解析1到100万：',values)

# 计算1到100万的总和   计算量太大所有全部注释方便下面的代码
# values = []
# for value in range(1,10000001):
#     values.append(value)
# print(values)
# print(min(values))
# print(max(values))
# print(sum(values))

#包含1到20的奇数，使用步长
values = [value for value in range(1,21,2)]
print(values)

#能被3 整除
values = [value for value in range(3,31,3)]
print(values)

#立方数
values = [value ** 3 for value in range(1,11)]
print(values)