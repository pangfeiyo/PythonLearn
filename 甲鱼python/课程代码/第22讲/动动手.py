



# 使用递归编写一个 power() 函数模拟内建函数 pow()，即 power(x ,y ) 为计算并返回 x 的 y　次幂的值。
def power(x, y):
    # 当 y != 0 时
    if y:
        return x * power(x, y - 1)
    else:
        return 1
print(power(2,3))

# 使用递归编写一个函数，利用欧几里得算法求最大公约数，例如 gcd(x, y) 返回值为参数 x 和参数 y 的最大公约数
def gcd(x, y):
    if y:
        return gcd(y, x % y)
    else:
        return x
print(gcd(4,6))
'''
解析：
gcd(x = 4,y = 6) 
    return gcd(6,4)
        return (4,2)
            return (2,0)
                reutn 2
'''