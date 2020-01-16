# 函数是一段具有特定功能、可重用的语句组
# 函数是一段代码的表示
'''
def <函数名>(<参数(0个或多个)>):
    <函数体>
    return <返回值>
'''

# 计算N
def fact(n):    # fact 函数名， n 参数
    s = 1
    for i in range(1,n+1):
        s *= i
    return s

print(fact(10))

# y =f(x)  函数定义时，所指定的参数是一种占位符
'''
 -调用时要给出实际参数
 -实际参数替换定义参数
 -函数调用后得到返回值
'''
# 函数可以有参数，也可以没有，但必须保留括号


# 可选参数传递
# 计算n!//m    n的阶乘整除m
def fact(n, m=1):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s // m
print(fact(10,5))


# 函数定义时可以设计可变数量参数，既不确定参数总数量
# def <函数名>(<参数>, *b):
def fact(n, *b):
    s = 1
    for i in range(1, n+1):
        s *= i
    for item in b:
        s *= item
    return s
print(fact(10,3,5,8))


# 参数传递两种方式
# 函数调用时，参数可以按照位置或名称方式传递
def fact(n, m=1):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s//m
# 位置传递
fact(10,5)
# 名称位置
fact(m=5, n=10)



# 函数的返回值
'''
 -return保留字用来传递返回值
 -函数可以有返回值，也可以没有，可以有return，也可以没有
'''
def fact(n, m=1):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s//m, n, m
# 元组类型
print(fact(10,5))

a,b,c = fact(10,5)
print(a,b,c)
