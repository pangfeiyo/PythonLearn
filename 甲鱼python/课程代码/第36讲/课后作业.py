# 0.按照以下提示尝试定义一个Person类并生成类实例对象 
'''
属性：姓名（默认姓名为"小甲鱼"）
方法：打印姓名
提示：方法中对属性的引用形式上需要加上self ，如 self.name
'''
class Person:
    name = '小甲鱼'
    def printName(self):
        print(self.name)
Person().printName()


# 1.按照以下提示尝试定义一个矩形类并生成类实例对象
'''
属性：长和宽
方法：设置长和宽 -> setRect(self) ，获得长和宽 -> getRect(slef) ，获得面积 -> getAreat(self)
提示：方法中对属性的引用形式上需要加上self ，如 self.width
'''
class Rectangle:
    length = 5
    width = 4
    
    def setRect(self):
        print("请输入矩形的长和宽")
        self.length = float(input("长："))
        self.width = float(input("宽："))

    def getRect(self):
        print("这个矩形的长是：%.2f，宽是：%.2f" % (self.length, self.width))

    def getAreat(self):
        return self.length * self.width

rec = Rectangle()
rec.getRect()
print("这个矩形的面积是：",rec.getAreat())
rec.setRect()
rec.getRect()
print("这个矩形的面积是：",rec.getAreat())
