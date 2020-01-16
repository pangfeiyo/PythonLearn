# BIF 内置函数
# 跟类与对象相关的BIF

'''
issubclass(class, classinfo)
如果 class 是 classinfo 的子类，返回True
'''
# 注意点：
# 1.一个类被认为是其自身的子类
# 2.classinfo可以是类对象组成的元组，只要class与其中任何一个候选类的子类，则返回Ture
class A:
    pass
class B(A):
    pass
class C:
    pass
print(issubclass(B,A))
print(issubclass(B,B))
# object 是所有类的基类，所有类 无论有没有写 class A(object)，都是默认继承于object
print(issubclass(B,object))
print(issubclass(B,C))


'''
isinstance(object, classinfo)
检查一个实例对象是否属于一个类
传入一个实例对象，传入一个类
这里同样可以传入元组 
'''
# 注意点：
# 1.如果第一个参数不是对象，则永远返回False
# 2.如果第二个参数不是类或由类对象组成的元组，会抛出一个TypeError异常  
print("\n-- isinstance(object, classinfo)")
print(isinstance(B,C))
b1 = B()
print(isinstance(b1,B))
# 这里为什么为True，因为B类是继承A类的
print(isinstance(b1,A))
print(isinstance(b1,(A,B,C)))



'''以下是访问对象的属性'''

'''
hasattr(object, name)   
测试一个对象里是否有指定的属性
'''
# attr = attribute 属性
# object 对象名， name 属性名
# name 必须要 "" 或 '' 括起
print("\n-- hasattr(object, name)")
class C:
    def __init__(self, x = 0):
        self.x = x
c1 = C()
print(hasattr(c1,'x'))

'''
getattr(object, name[, default])
返回对象指定的属性的值
'''
# 如果指定的属性不存在，会抛出一个异常AttributeError
# 如果设定了 default ， 异常时会打印default的内容
print("\n-- getattr(object, name[, default])")
print(getattr(c1,'x'))
#print(getattr(c1,'y'))
print(getattr(c1,'y','你所搜索的属性不存在'))

'''
setattr(object, name, value)
设定对象中指定属性的值，如果属性不存在，则会新建这个属性并赋值
'''
print("\n-- setattr(object, name, value)")
setattr(c1,'y','FishC')
print(getattr(c1,'y','您搜索的不存在'))

'''
delattr(object, name)
删除对象是指定的属性，如果不存在则抛出异常AttributeError
'''
delattr(c1,'y')
#delattr(c1,'y')    # 二次删除就会抛出异常了
print(hasattr(c1,'y'))  # 查找是否存在 






'''
property(fget=None, fset=None, fdel=None, doc=None)
通过属性来设置属性
'''
# fget 获取属性， fset 设置属性， fdel 删除属性， doc 
print("\n-- property(fget=None, fset=None, fdel=None, doc=None)")
class C:
    def __init__(self, size = 10):
        self.size = size
    def getSize(self):
        return self.size
    def setSize(self, value):
        # 让用户设置这个属性
        self.size = value
    def delSize(self):
        del self.size
    x = property(getSize, setSize, delSize)

c1 = C()
# 获取c1里的size值，按以前的方法
print(c1.getSize())
# 用propetry之后
print(c1.x)
# 修改值
c1.x = 18
print(c1.x)
# 删除
del c1.x
#print(c1.x)    # 被删除了这里会找不到