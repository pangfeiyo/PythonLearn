# 屏蔽机制
# 全局变量与局部变量
count = 5
def MyFun():
    count = 10
    print("函数内的count:",count)

MyFun()
print("全局变量count：",count)
print("……")


# global
# 在函数内修改全局变量
count = 5
def MyFun():
    global count
    count = 10
    print("函数内：",count)
MyFun()
print("全局：",count)



# 内嵌函数
print("\n--- 内嵌函数 ---")
def fun1():
    print("fun1()正在被调用...")
    def fun2():
        print("fun2()正在被调用...")
    fun2()

fun1()


# 闭包
# 闭包（closure）是函数式编程的重要的语法结构
# 如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包(closure)。
print("\n--- 闭包 ---")
def FunX(x):
    def FunY(y):
        return x * y
    return FunY
# 方法一
i = FunX(8)
print("方法一：",i(5))
# 方法二
print("方法二：",FunX(8)(5))


# nonlocal
print("\nnonlocal")
# 闭包中是不能修改外部作用域的局部变量的  如下方 Fun1()中的 x = 5
# def Fun1():
#     x = 5
#     def Fun2():
#         x *= x
#         return x
#     return Fun2()
# print(Fun1())
'''
以上代码会出错，因为在 Fun2() 中 x 是其局部变量，找不到外部程序的 x = 5。
解决以上问题可以使用列表
参考   http://www.jb51.net/article/54498.htm
'''
# python 3.x 的解决方案
def Fun1():
    x = 5
    def Fun2():
        # 该语句显式的指定 a 不是闭包( Fun2() )的局部变量
        nonlocal x
        x *= x
        return x
    return Fun2()
print("nonlocal py3.x：",Fun1())

# python 2.x 的解决方案，使用列表或元组。 即 容器
def Fun1():
    x = [6]
    def Fun2():
        x[0] = x[0] * x[0]
        return x[0]
    return Fun2()
print("py2.x：",Fun1())