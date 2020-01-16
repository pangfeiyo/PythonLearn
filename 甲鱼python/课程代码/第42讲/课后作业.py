# 在pthon中两个字符串相加会自动拼接字符串，但相减会抛出异常。
# 因此，现在要求定义一个Nstr类，支持字符串的相减操作：A-B，从A中去除所有B的子字符串
'''
示例：
>>> a = Nstr('I love FishC.com!iiiiiiii')
>>> b = Nstr('i')
>>> a - b
'I love FshC.com'
'''
# 只需要重载__sub__魔法方法即可
class Nstr(str):
    def __sub__(self,other):
        # str.replace(old, new[, max])
        # old 将被替换的子字符串
        # new 新字符串，用于替换old子字符串
        # max 可选字符串，替换不超过max次
        return self.replace(other,"")
a = Nstr('I love FishC.com!iiiiiiii')
b = Nstr('i')
print(a-b)



# 定义一个类 Nstr， 当该类的实例对象间发生的加、减、乘、除运算时，
# 将该对象的所有字符串的ASCII码之和进行计算
'''
>>> a = Nstr('FishC')
>>> b = Nstr('love')
>>> a + b
899
>>> a - b
23 
>>> a * b
201918
>>> a / b
1.052511415525114
>>> a // b
1
'''
class Nstr:
    def __init__(self, arg=''):
        if isinstance(arg, str):
            self.total = 0
            for each in arg:
                self.total += ord(each)
        else:
            print("参数错误！")

    def __add__(self, other):
        return self.total + other.total

    def __sub__(self, other):
        return self.total - other.total

    def __mul__(self, other):
        return self.total * other.total

    def __truediv__(self, other):
        return self.total / other.total

    def __floordiv__(self, other):
        return self.total // other.total
a = Nstr("FishC")
b = Nstr('love')
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)

# 方法二
class Nstr(int):
    def __new__(cls, arg = 0):
        if isinstance(arg, str):
            total = 0
            for each in arg:
                total += ord(each)
            arg = total
        return int.__new__(cls, arg)

a = Nstr("FishC")
b = Nstr('love')
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)

