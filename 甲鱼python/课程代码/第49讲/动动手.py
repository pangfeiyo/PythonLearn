# 实现一个功能与reversed()相同
# （内置函数reversed(seq)是返回一个迭代器，是序列seq的逆序显示）的生成器
# 例如：
'''
>>> for i in myRev("FishC"):
        print(i, end="")

ChsiF
'''
def myRev(data):
    # 这里用 range 生成 data 的倒序索引
    # 注意， range 的结束位置是不包含的
    # range(start, stop[, step])  计数从start开始，到stop结束，step步长，默认为1
    for index in range(len(data)-1, -1, -1):
        yield data[index]

# 这里变量名要和函数名分开，不然会造成覆盖
'''
变量名覆盖函数名
def a():
    return 1

print(a)

a = a()

print(a)
'''
myR = myRev("FishC")
print(next(myR))
print(next(myR))
print(next(myR))
print(next(myR))
print(next(myR))


myR = myRev("FishC")
for i in myR:
    print(i)



# 10以内的素数之和是：2+3+5+7=17，计算200W以内的素数之和
# 如果将200w以内的所有素数找到并存放到一个列表中，再依次求和计算，可能会挤爆内存
# 所以这里要用生成器
# 答案是142913828922，计算时间可能有点长
# 素数，被1和自己整除
import math
def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        # sqrt(x) 返回x的平方根 
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False

def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1

def solve():
    total = 2 
    # 这里不等同于in range()，   这里get_primes()的返回值是多少，next_prime就是多少
    for next_prime in get_primes(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return

if __name__ == '__main__':
    solve()
