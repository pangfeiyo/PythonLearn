class int(int):
    def __add__(self, oterh):
        return int.__sub__(self, oterh)

a = int("5")
print(a)

b = int(3)
print(b)

print(a+b)

# 反运算，加一个 r    __radd__
# a + b ，当a的加法操作没有实现或不支持的时候，由b来执行加法操作
print("\n-- 反运算")
class Nint(int):
    def __radd__(self, other):
        return int.__sub__(self, other)

a = Nint('5')
print(a)

b = Nint(3)
print(b)

'''
这里的print(a+b)结果为2，为什么不是正确答案8
因为上面的class int(int)  第一个int是类名，括号里的int是继承，类里的方法改变了int这个类型的加法运算。
而下面的Nint类也是继承int类型，因为在类int中已经改变了int类型的加法运算所以这里a,b=Nint(5,3)   a+b不符合radd，采用add（被转为减法）
'''
print(a+b)
'''
这里的print(1+b)结果为什么是2
1+Nint的时候，会按顺序执行数字1，加号，有Nint的数字，这时候发现Nint有radd，回去找第一个数字的add，没有，执行后面Nint的radd
变成3+1，因为3是Nint，继承了int类型，变成3-1
以上是个人理解，以下是ooxx7788的回复 
是先看1有没有__add__，发现没有，那么执行的是Nint(3)的__radd__
而Nint(3)的__radd__ 是int.__sub__(self,other)【因为继承了class int(int)】
self就是Nint(3)，other就是1
'''
print(1+b)



class Nint(int):
    def __rsub__(self, other):
        return int.__sub__(self, other)
a = Nint('5')
print(a)
print(3-a)

class Nint(int):
    def __rsub__(self, other):
        return int.__sub__(other, self)
a = Nint('5')
print(a)
print(3-a)
