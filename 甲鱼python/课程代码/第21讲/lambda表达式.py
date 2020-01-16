def ds(x):
    return 2 * x + 1
print(ds(5))

g = lambda x : 2 * x + 1
print(g(5))

print("……")
def add(x,y):
    return x + y
print(add(3,4))

g = lambda x , y : x + y
print(g(3,4))


# 过滤器  filter()
# help(filter)

# filter(function or None, iterable) --> filter object
# filter 有两个参数，可以是一个函数或一个 None 对象。第二个参数是一个可迭代数据 iterable

# filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判定，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。

# 如果第一参数值为 None ， 过滤第二个参数中非 True 值
list1 = list(filter(None, [1,0,False,True]))
print(list1)
# 用filter 筛选出奇数
def odd(x):
    return x % 2
temp = range(0,10)
show = filter(odd, temp)
print("使用filter",list(show))
# 返回这些值是因为，在 python 中， True 的默认值为 1

# 使用 lambda
print("使用lambda",list(filter(lambda x : x % 2, range(0,10))))


# map()  映射
# 仍然是一个函数和一个可迭代序列。
# 将序列的每一个元素做为函数的参数进行运算加工，直到可迭代序列的每个元素都加工完毕，返回所有加工后的元素构成的新序列
print("map() 映射：",list(map(lambda x : x * 2, range(10))))
