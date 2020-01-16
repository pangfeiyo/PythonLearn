print("-- 0 --")
# 请使用 lambda 表达式将下边函数转变为匿名函数
def fun_A(x, y = 3):
    return x * y
print(fun_A(2))

fun_A = lambda x, y = 3 : x * y
print(fun_A(2))

print("-- 1 --")
# 请将下边的匿名函数转变为普通函数
g = lambda x : x if x % 2 else None
print(g(5))

# 在 python 中   if 语句如果不写具体则默认为 True    。 在 python 中， True 为 1 。 False 为 0
def is_odd(x):
    if x % 2:
        return x
    else:
        return None
print(is_odd(5))


print("-- 3 --")
# 利用 filter() 和 lambda 表达式快速求出 100 以内所有 3 的倍数
print(list(filter(lambda n : not(n % 3),range(1,101))))
# 个人解析（可配合前面的 filter 解释看）：
# filter() 有两个参数，前者为函数【也可以称为条件等】（lambda n : not(n % 3)）， 后者为序列（ range(1,101) ）
# 将序列中的每一个元素当做参数传给函数进行判定，筛选出所有返回值为 True 的元素，将这些元素放到新的序列中
# 使用 not(n % 3) 的原因：
# 在 python 中， True == 1， False == 0。 假设 n = 6 ， 6 肯定是 3 的倍数，但 n % 3 的返回值为 0 ；
# 并且前面使用了 filter() 函数，不会将返回值为 0 的元素存放到新序列中，所以这里要用 not 。 （这里也不会出现0 和 1 以外的结果）


print("-- 4 --")
print("使用列表推导式，代替filter()和lambda()组合")
list1 = [i for i in range(1,101) if not i % 3]
print(list1)
# 推导式还原
# list = []
# for i in range(1,101):
#     if not i % 3:   # 这里省略了 i % 3 的结果，Python 默认为   i % 3 == True，即 i % 3 == 1 ，因为求的是 3 的倍数，所以结果不可以为 1 ，这里要用 not
#         list.append(i)
# print(list)


print("-- 5 --")
# 还记得 zip 吗？ 使用 zip 会将两数以元组的形式绑定在一块，例如：
print("zip：",list(zip([1,3,5,7],[2,4,6,8])))
# 但希望打包的形式是灵活多变的列表，采用 map 和 lambda 表达式
# map()  会根据提供的函数对指定序列做映射。
# map() 函数接收两个参数，一个是函数，一个是序列。 将序列中的每一个元素传给函数，把结果作为新的序列返回
print("map + lambda：",list(map(lambda x, y : [x, y],[1,3,5,7], [2,4,6,8])))


print("-- 6 --")
# 以下表达式会打印什么
def make_repeat(n):
    return lambda s : s * n
double = make_repeat(2)
print(double(8))
print(double("FishC"))
# 解析：
# make_repeat 返回的是一个匿名函数（ lambda )
# 这个匿名函数接收一个参数，当你在调用他的时候，把 8 作为参数

