num1 = {}
print(type(num1))   # type:dict

num2 = {1,2,3,4}
print(type(num2))   # type:set 集合

# {} 不是字典专属
# 在 {} 中存入不带有映射类型（即字典）数据时，为集合
# 集合中不存在重复，如果有会自动剔除，如下
num2 = {1,2,3,4,5,4,3,2,1,6}
print(num2)
# 并且在集合中是无序的，即无法通过 num2[2]这样的方法获取具体下标元素



# 如何创建一个集合
# 一种是直接把一堆元素使用花括号{} 括起来
# 一种是使用set()工厂函数
set1 = set([1,2,3,4,5,5])
print(set1)



# 要求：去除列表中重复的元素
# [0,1,2,3,4,5,5,3,1]
# 方法一
num1 = [1,2,3,4,5,5,3,1,0]
temp = []
for each in num1:
    if each not in temp:
        temp.append(each)
print('方法一：', temp)
#方法二
num1 = list(set(num1))
print('方法二：',num1)  # 得到的集合值的顺序是无序的


# in, not in 
print(1 in num1)


# 增加
num2.add(8)
print(num2)
# 删除
num2.remove(5)
print(num2)


# 不可变集合
# frozen  冰冻的，冻结的
num4 = frozenset({1,2,3,4,5})
# num4.add(5)   这里是报错的，不给增加
print(num4)