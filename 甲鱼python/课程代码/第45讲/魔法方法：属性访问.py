'''
 __getattr__(self, name)
 - 当用户试图获取一个不存在的属性时的行为
 __getattribute__(self, name)
 - 定义当该类的属性被访问时的行为
 __setattr__(self, name, value)
 - 定义当一个属性被设置时的行为
 __delattr__(self, name)
 - 定义当一个属性被删除时的行为
 '''

#class C:
#    def __init__(self):
#        self.x = 'x-man'

#c = C()
#print(c.x) 

#print(getattr(c,'x','没有这个属性'))
#print(getattr(c,'y','没有这个属性'))



class C:
    def __init__(self, size = 10):
        self.size = size

    def getSize(self):
        return self.size

    def setSize(self, value):
        self.size = value

    def delSize(self):
        del self.size

    x = property(getSize, setSize, delSize)

c = C()
c.x = 100
print(c.x)

print(c.size)
del c.x
#print(c.x) 删除后这里会报错 



class C:
    def __getattribute__(self, name):
        print("getattribute")
        # super()找其父类，这里class C没有继承，默认继承object
        return super().__getattribute__(name)

    def __getattr__(self, name):
        print("getattr")

    def __setattr(self, name, value):
        print("setattr")
        super().__setattr__(name, value)

    def __delattr__(self, name):
        print("delattr")
        super().__delattr__(name)

c = C()
c.x

c.x=1
c.x

del c.x


# 写一个矩形类，默认有宽和高两个属性
# 如果为一个叫 square的属性赋值，那么说明这是一个正方形，
# 值不是正方形的边长，此时宽和高都应该等于边长
class Rectangle:
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height

    def __setattr__(self, name, value):
        if name == 'square':
            self.width = value
            self.height = value
        else:
            # self.name = value 这样会无限循环
            # 方法一
            # super().__setattr__(name, value)
            # 方法二
            self.__dict__[name] = value
            
    def getArea(self):
        return self.width * self.height

r1 = Rectangle(4,5)
print(r1.getArea())

r1.square = 10
print(r1.width)
print(r1.height)
print(r1.getArea())
# 以字典形式显示当前对象的所有属性和对应的值
print(r1.__dict__)