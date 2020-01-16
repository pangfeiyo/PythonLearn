#编写一个函数power()模拟内建函数pow()，即power(x,y)为计算并返回x的y次幂的值
#方法一
def power1(x,y):
    return x ** y
print(power1(2,3))
#方法二
def power2(x, y):
    result = 1

    for i in range(y):
        result *= x

    return result
#有return的话，就需要用print()打印出来
print(power2(2, 3))

#编写一个函数，利用欧几里得算法（如下）求最大公约数
# http://baike.baidu.com/item/%E8%BE%97%E8%BD%AC%E7%9B%B8%E9%99%A4%E6%B3%95
def gcd(x, y):
    while y:
        t = x % y
        x = y
        y = t

    return x


print(gcd(4, 6))


#将十进制转换成二进制数。   结果与调bin()一样返回字符串形式
def Dec2Bin(dec):
    temp = []
    result = ''

    while dec:
        quo = dec % 2
        dec = dec // 2
        temp.append(quo)
    #print(temp)
    while temp:
        result += str(temp.pop())

    return result


print(Dec2Bin(62))

'''
print(62%2)
print(62//2)
print(31%2)
print(31//2)
'''