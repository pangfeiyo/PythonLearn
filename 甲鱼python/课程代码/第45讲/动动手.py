# 当访问一个不存在的属性时，不报错且提示“该属性不存在！”
class Demo:
    def __getattr__(self, name):
        return "该属性不存在"

demo = Demo()
print(demo.x)


# 编写Demo类，使得下边代码可正常执行
'''
>>> demo = Demo()
>>> demo.x
'FishC'
>>> demo.x = "X-man"
>>> demo.x
'X-man'
'''
class Demo:
    def __getattr__(self, name):
        self.name = 'FishC'
        return self.name
demo = Demo()
print(demo.x)


# 编写一个Counter类，用于实时检测对象有多少个属性
class Counter:
        def __init__(self):
                super().__setattr__('counter', 0)
        def __setattr__(self, name, value):
                super().__setattr__('counter', self.counter + 1)
                super().__setattr__(name, value)
        def __delattr__(self, name):
                super().__setattr__('counter', self.counter - 1)
                super().__delattr__(name)

c = Counter()
c.x = 1
print(c.counter)

c.y =1
c.z=1
print(c.counter)

del c.x
print(c.counter)