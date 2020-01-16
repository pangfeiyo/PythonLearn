# 类 是图纸，而由类实例化后的对象才是可以住人的房子
#class Ball:
#    def setName(self, name):
#        self.name = name
    
#    def kick(self):
#        print("这个球叫：",self.name)
#a = Ball()
#a.setName("A")

#b = Ball()
#b.setName("B")

#c=Ball()
#c.setName("dog")

#a.kick()
#b.kick()
#c.kick()


# 魔法方法
class Ball:
    # name也可以设置默认参数
    def __init__(self, name):
        self.name = name
    def kick(self):
        print("这个球叫：", self.name)

a = Ball('A')
b = Ball("土豆")

a.kick()
b.kick()



# 公有和私有
class Person:
    name = '甲鱼一号'

p = Person()
print(p.name)

# name mangling 名字改编，名字重整
# 在Python中定义私有变量只需要在变量名或
class Person:
    __name = '甲鱼'
p = Person()
# print(p.__name) 找不到
# 若要访问需要从内部引用
class Person:
    __name = '小甲鱼'
    def getName(self):
        return self.__name
p=Person()
print(p.getName())
# 也可以这么访问，但并不推荐
print(p._Person__name)

# 其实这是伪私有