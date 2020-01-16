class Parent:
    def hello(self):
        print("正在调用父类的方法")

# class 子类（父类）
class child(Parent):
    pass

p = Parent()
p.hello()

c = child()
c.hello()

# 如果子类中定义与父类同名的方法或属性，则会自动覆盖父类对应的方法或属性
class child(Parent):
    def hello(self):
        print("正在调用子类的方法")
c = child()
c.hello()
p.hello()



# 扩展37讲动动手第二题里的鱼的种类
import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        self.x -= 1
        print("我的位置是：", self.x, self.y)
# 以下三个是小鱼
class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass
# 鲨鱼
class Shark(Fish):
    def __init__(self):
        # 饿不饿
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("想吃")
            self.hungry = False
        else:
            print("饱了")

fish = Fish()
# 位置
fish.move()
fish.move()

goldfish = Goldfish()
goldfish.move()
shark = Shark()
shark.eat() # 想吃
shark.eat() # 饱了
# shark.move()  # 想通过让鲨鱼移动减少饱食，但会报错。因为Shark()类中重新定义了与父类同名的__init__，找不到 x 属性
# 解决方法，在Shark()类调用自己的__init__之类先调用父类的__init__
# 实现方法有两种：  1.调用未绑定的父类方法    2.使用super函数
# 方法一：
class Shark(Fish):
    def __init__(self):
        # 方法一：
        Fish.__init__(self) # 这个self并不是父类的，而是子类的。 这里写 Fish.__init__(Shark)也可以
        # 饿不饿
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("想吃")
            self.hungry = False
        else:
            print("饱了")
shark = Shark()
shark.move()
shark.move()
# 方法二：  使用super函数，更好
class Shark(Fish):
    def __init__(self):
        # 方法二：
        super().__init__()  # 调用父类的方法
        # 饿不饿
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("想吃")
            self.hungry = False
        else:
            print("饱了")
shark = Shark()
shark.move()
shark.move()



# 多重继承，可以同时继承多个父类
class Base1:
    def foo1(self):
        print("my foo1")
class Base2:
    def foo2(self):
        print("my foo2")
class C(Base1, Base2):
    pass
c = C()
c.foo1()
c.foo2()