#help(list)
#迭代，重复反馈过程的活动
#每一次对过程重复称为一次迭代，结果被用来下一次迭代的初始值。for循环算是
#list 要么不带参数，要么带一个迭代器
a = list()
print(a)
b = 'I love fishC.com'
b = list(b)
print(b)
c = (1,1,2,3,5,6,13,21,34)
c = list(c)
print(c)
ee =list('123434ababced')
print(ee)

#tuple([iterable])，把一个可迭代对象转换成元组
#和list差不多
#help(tuple)
print(len(a))
print(len(b))

#使用max()和min()需要保证集合中的数据类型都是一个类型
#max() 返回序列或参数集合中的最大值
max1 = max(1,2,3,4,5)
print(max1)
print(max(b))
print(max(ee))
numbers = [1,18,13,0,-98,34,54,76,32]
print(max(numbers))
#min() 返回序列或参数集合中的最小值
print(min(numbers))
#n2 = [1,2,3,4,5,6,'x','z','c']  这样就会报错
#print(max(n2))

#  sun(iterable[, start = 0])     返回序列iterable和可选参数start的总和
tuple2 = (3.1,2.3,3.4)
print(sum(tuple2))

#sorted()  返回一个排序列表，默认从小到大，使用方法和list.sort() 一致
print(sorted(numbers))

#reversed() 返回一个迭代器对象
print(reversed(numbers))
#加入list即可转回列表，并反转列表顺序
print(list(reversed(numbers)))

#enumerate() 枚举，生成每个元素的index值和value值，并组成一个元组
print(enumerate(numbers))
print(list(enumerate(numbers)))

#zip 打包、压缩    返回由各个参数的序列组成的元组
#多余的不显示
a = [1,2,3,4,5,6,7,8]
b = [4,5,6,7,8]
print(zip(a,b))
print(list(zip(a,b)))