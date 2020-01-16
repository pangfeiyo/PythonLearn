# 假设已有鸟类的定义，现在要定义企鹅类继承于鸟类，但企鹅不会飞，如何屏蔽父类（鸟类）中飞的方法
class Bird:
    def fly(self):
        print("Fly away!")

class Penguin(Bird):
    def fly(self):
        pass
bird = Bird()
bird.fly()
penguin = Penguin()
penguin.fly()


# 0.定义一个点（Point)类和直线（Line)类，使用getLen方法可以获得直线的长度
'''提示：
设点A（x1, y1）、点B（x2, y2），则两点构成的直线长度 |AB| = ✓（（x1 - x2）2 + （y1 - y2）2）
Python中计算开根号可使用math模块中的sqrt函数（sqrt(x) 返回数字x的平方根）
直线需要有两点构成，因此初始化时需要有两个点（Point）对象作为参数 '''
import math 

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x
    def getY(self):
        return self.y

class Line():
    def __init__(self, p1, p2):
        self.x = p1.getX() - p2.getX()
        self.y = p1.getY() - p2.getY()
        self.len = math.sqrt(self.x * self.x + self.y * self.y)
    
    def getLen(self):
        return self.len

p1 = Point(1,1)
p2 = Point(4,5)
line = Line(p1, p2)
print(line.getLen())



