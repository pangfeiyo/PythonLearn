'''
集合类型定义
是多个元素的无序组合
- 与数学中的集合概念一致
- 集合元素之间无序，每个元素唯一，不存在相同元素
- 集合元素不可更改，不能是可变数据类型

- 集合用大括号{}表示 ，元素间用逗号分隔
- 建立集合类型用 {} 或 set()
- 建立空集合必须使用　set()'''

# 使用{}建立集合
A = {"python", 123, ("python", 123)}    # () 是元组
print(A)
# 使用set()建立集合
B = set('pypy123')
print(B)    # 重复会被删除，且无序

C = {"python", 123, "python", 123}
print(C)


'''
S | T     并，返回一个新集合，包括在集合S和T中所有元素
S - T     减（差），返回一个新集合，包括在集合S但不在T中的元素
S & T     交，返回一个新集合，包括同时在集合S和T中的元素
S ^ T     补，返回一个新集合，包括集合S和T中的非相同元素

S <= T 或 S < T    返回True/False，判断S和T的子集关系
S >= T 或 S > T    返回True/False，判断S和T的包含关系

增强操作符
S |= T    更新集合S，包括在集合S和T中的所有元素
S -= T    更新集合S，包括在集合S但不在T中的元素
S &= T    更新集合S，包括同时在集合S和T中的元素
S ^= T    更新集合S，包括集合S和T中的非相同元素
'''
A = {"p","y",123}
B = set("pypy123")
print("A：",A)
print("B：",B)
print("A-B：",A-B)
print("B-A：",B-A)
print("A&B：",A&B)
print("A|B：",A|B)
print("A^B：",A^B)


'''
集合处理方法
S.add(x)        如果 x 不在集合S中，将 x 增加到S
S.discard(x)    移除S中元素，如果 x 不在集合S中，不报错
S.remove(x)     移除S中元素 x，如果 x 不在集合 S 中，产生KeyError异常
S.clear()       移除S中所有元素
S.pop()         随机取出S的一个元素，更新S，若S为空产生KeyError异常
S.copy()        返回集合S的一个副本
len(S)          返回集合S的元素个数 
x in S          判断S中元素x，x在集合S中，返回True，否则返回False
x not in S      判断S中元素x，x不在集合S中，返回False，否则返回True
set(x)          将其他类型变量x转变为集合类型
'''
A = {"p","y",123}
print("item：", end="")
for item in A:
    print(item, end="")


print(),print("A.pop()：",end="")
try:
    while True:
        print(A.pop(),end="")
except:
    pass
print("\nA：",A)


# 包含关系比较
print("p" in {"p","y",123})
print({"p","y"} >= {"p","y",123})


# 数据去重：集合类型所有元素无重复
ls = ["p","p","y",'y',123]
s = set(ls) # 利用了集合无重复元素的特点
print(s)
lt = list(s)    # 将集合转换为列表
print(lt)