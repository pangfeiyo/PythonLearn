# 魔法方法总是被双下划线包围，如 __init__
# 方法方法是面向对象的python的一切
# 魔法方法体现在它们能够在适当的时候被自动调用

# __init__(self[, ...])



# __new__(cls[, ...])
# 在init之前被调用，对象实例化被第一个调用
# 有一种情况要重写：
# 当继承一个不可变类型和需要修改的时候
class CapStr(str):
     def __new__(cls, string):
         string = string.upper()
         return str.__new__(cls, string)    
a = CapStr("I love fishc.com")
print(a)


# __del__(self)
class C:
    def __init__(self):
        print("__init__被调用")
    def __del__(self):
        print("__del__被调用")
c1 = C()
c2 = c1
c3 = c2

del c3
del c2
del c1


