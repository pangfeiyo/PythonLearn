# 使用修饰符（装饰器）修改以下代码
# 代码 A：
class CodeA:
    def foo():
        print("调用静态方法 foo()")

        # 将 foo() 方法设置为静态方法
        foo = staticmethod(foo)

# 代码 B：
class CodeB:
    def foo(cls):
        print("调用类方法 foo()")

        # 将 foo() 方法设置为类方法
        foo = classmethod(foo)


# 修改后
# 代码 A：
class CodeA:
    @staticmethod
    def foo():
        print("调用静态方法 fod()")

# 代码 B：
class CodeB:
    @classmethod
    def foo(cls):
        print("调用方法 foo()")


# 将以下代码没有用上修饰符的等同形式：
@something
def f():
    print("I love fishC.com")
'''
Python的修饰符就是一种优雅的封装，但要注意只可以在模块或类定义内对函数进行修饰，不允许修饰一个类。
一个修饰符就是一个函数，它将被修饰的函数做为参数，并返回修饰后的同名函数或其它可调用的东西。
'''
# 相当于
def f():
    print("I love fishC.com")
f = something(f)




class C:
    def __init__(self, size=10):
        self.size = size
        
    @property
    def x(self):
        return self.size

    @x.setter
    def x(self, value):
        self.size = value

    @x.deleter
    def x(self):
        del self.size
