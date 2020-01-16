# 递归属于算法
# 以下代码会报错，提示超过 python 规定递归的最大深度，理论上会一直持续下去
def recursion():
    return recursion()
# print(recursion())
# python 出于善意的保护，对于递归的深度默认是 100 层，如果是写网络爬虫，有时候不止 100 层，可以自己设置深度
# 以下为修改递归深度
# import sys
# sys.setrecursionlimit(1000000)

# 用非递归写一个求阶乘的函数
# ——正整数阶乘指从 1 乘以 2 乘以 3 乘以 4 一直乘到所要求的数。
# ——例如所给的数是 5 ，则阶乘式是 1 * 2 * 3 * 4 * 5 ，得到的积是 120 ， 所以 120 就是 5 的阶乘
print("-- 非递归函数 --")

def factorial(n):
    result = n
    for i in range(1,n):
        result = result * i
    return result
number = int(input("请输入一个正整数："))
# 这里这个result 是全局变量，而上面的result 是内部变量
result = factorial(number)
print("%d 的阶乘是 %d" % (number, result))


# 递归阶乘
print("\n-- 递归阶乘 --")
def recursive_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n-1)
number = int(input("请输入一个正整数："))
result = recursive_factorial(number)
print("%d 的阶乘是 %d" % (number, result))
'''
解析： 以上满足递归的两个条件
调用函数自身、设置了自身正确的返回条件
recursive_factorial(5) = 5 * recursive_factorial(4)
    recursive_factorial(4) = 4 * recursive_factorial(3)
        recursive_factorial(3) = 3 * recursive_factorial(2)
            recursive_factorial(2) = 2 * recursive_factorial(1)
                recursive_factorial(1) = 1 
'''

# 递归在编程上的形式是如何表现的呢？
# 答：在编程上，递归表现为函数调用本身这么一个行为。
