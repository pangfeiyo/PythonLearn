#乌龟类
class Turtle:
    def __init__(self, x):
        self.num = x

class Fish:
    def __init__(self, x):
        self.num = x

# 水池类
class Pool:
    # x个乌龟 y个鱼
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)
    def print_num(self):
        print("水池里总共有乌龟 %d 只，鱼 %d 条" % (self.turtle.num, self.fish.num))
pool = Pool(1,3)
pool.print_num()

# 所谓组合就是把类的实例化放到一个新类中，就把旧类给组合进去了



# 类、类对象和实例对象
class C:
    count = 0

a = C()
b = C()
c = C()
print(a.count, b.count, c.count)
c.count += 10
print("c.count+=10",c.count)
print("a.count",a.count)

C.count += 100
print("C.count+=100之后的a",a.count)

'''
           类定义    C
                     |            
                     |
           类对象    C
                     |
               |-----|-----|
     实例对象  a     b     c

'''


# 属性和方法名相同，会把方法给覆盖掉
class C:
    def x(self):
        print("x-man")
c = C()
c.x()
c.x = 1
print(c.x)
# c.x()  这句就会报错



# Python严格要求方法需要有实例才能被调用，这种限制其实就是Python所谓的绑定概念
class BB:
    def printBB():
        print("bbj")
BB.printBB()    # 这样可以
# 但如果类实例化之后，就找不到了，需要绑定个参数(self)才可以
class BB:
    def printBB(self):
        print("bbj")
bb = BB()
bb.printBB()



class CC:
    def setXY(self, x, y):
        self.x = x
        self.y = y
    def printXY(self):
        pint(self.x, self.y)
dd = CC()
# 查看对象所拥有的属性
print(dd.__dict__)
print(CC.__dict__)

dd.setXY(4,5)
print(dd.__dict__)
print(CC.__dict__)