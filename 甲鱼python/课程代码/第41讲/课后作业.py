# 经常打开文件后忘记关闭
# 写一个FileObject类，给文件对象进行包装，从而确认在删除对象时文件能自动关闭
'''灵活搭配__init__和__del__方法'''
class FileObject:
    '''给文件对象进行包装从而确认在删除时文件流关闭'''
    def __init__(self, filename = 'sample.txt'):
        self.new_file = open(filename,'r+') # r+ 读写，不创建文件

    def __del__(self):
        self.new_file.close()
        del self.new_file


# 按以下要求定义一个类实现摄氏度到华氏度的转换
# 转换公式： 华氏度 = 摄氏度 * 1.8 + 32
# 要求：我们希望这个类尽量简练地实现功能，如下
'''
>>> print(C2F(32))
89.6
'''
# 为尽量简练实现功能，在类进行初始化之前，通过“掉包”arg参数，让实例对象直接返回计算后的结果
class C2F(float):
    '''摄氏度转华氏度'''
    def __new__(cls, arg = 0.0):
        return float.__new__(cls, arg * 1.8 + 32)



# 定义一个类继承于int类型，并实现一个特殊功能：
# 当传入的参数是字符串的时候，返回该字符串中所有字符的ASCII码的和
# （使用ord()获得一个字符的ASCII码值）
# ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，
# 它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，
# 如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。
# 实现如下：
'''
>>> print(Nint(123))
123
print(Nint(1.5))
1
print(Nint('A'))
65
print(Nint('FishC))
461
'''
class Nint(int):
    def __new__(cls, arg = 0):
        # isinstance(object, classinfo) 函数来判断一个对象是否是一个已知的类型，类似type()
        if isinstance(arg, str):
            total = 0
            for each in arg: 
                total += ord(each)
            arg = total
        return int.__new__(cls, arg)


