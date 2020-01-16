# 描述符就是将某种特殊类型的类的实例指派给另一个类的属性
# 特殊类型的类有一个要求，至少实现以下三种其中一种
#   __get__(self, instance, owner)
#       - 用于访问属性，它返回属性的值
#   __set__(self, instance, value)
#       - 将在属性分配操作中调用，不返回任何内容
#   __delete__(self, instance)
#       - 控制删除操作，不返回任何内容
class MyDecriptor:
    def __get__(self, instance, owner):
        print("getting...",self, instance, owner)

    def __set__(self, instance, value):
        print("setting...",self, instance, value)

    def __delete__(self, instance):
        print("deleting...",self, instance)

class Test:
    x = MyDecriptor()

test = Test()
test.x
print(test)
print(Test)

test.x = 'X-man'

del test.x



class MyProgerty:
    def __init__(self, fget= None, fset = None, fdel = None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        return self.fget(instance)

    def __set__(self, instance, value):
        self.fset(instance, value)

    def __del__(self, instance):
        self.fdel(instance)

class C:
    def __init__(self):
        self._x = None
    
    def getX(self):
        return self._x

    def setX(self, value):
        self._x = value

    def delX(self):
        del self.x

    x = MyProgerty(getX, setX,delX)

c = C()
c.x = 'x-man'
print(c.x)
print(c._x)
# del c.x 出错



# 定义一个温度类，然后定义两个描述符类用于描述摄氏度和华氏度两个属性
# 要求两个属性会自动进行转换，也就是说你可以给摄氏度这个属性赋值，然后打印的华氏度属性是自动转换后的结果
class Celsius:
    def __init__(self, value = 26.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)

class Fahrenheit:
    def __get__(self, instance, owner):
        return instance.cel * 1.8 + 32

    def __set__(self, instance, value):
        instance.cel = (float(value) - 32) / 1.8


class Temperature:
    cel = Celsius()
    fah = Fahrenheit()

temp = Temperature()
print("temp.cel",temp.cel)
temp.cel = 30
print("temp.fah",temp.fah)
temp.fah = 100
print("temp.cel",temp.cel)