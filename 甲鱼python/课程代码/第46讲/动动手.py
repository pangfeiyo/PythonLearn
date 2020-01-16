class MyDes:
    def __init__(self, value = None):
        self.val = value
    def __get__(self, instance, owner):
        return self.val ** 2


class Test:
    def __init__(self):
        self.x = MyDes(3)

test =Test()
test.x


# 当类的属性被访问、修改或设置的时候，分别做出提醒
# 程序实现如下：
'''
class Test:
        x = MyDes(10, 'x')

>>> test = Test()
>>> y = test.x
正在获取变量： x
>>> y
10
>>> test.x = 8
正在修改变量： x
>>> del test.x
正在删除变量： x
噢~这个变量没法删除~
>>> test.x
正在获取变量： x
8
'''
# 这里描述符起到的作用是间接地保存指定变量的数据
class MyDes:
    def __init__(self, initval = None, name = None):
        self.val = initval
        self.name = name

    def __get__(self, instance, owner):
        print("正在获取变量：", self.name)
        return self.val

    def __set__(self, instance, value):
        print("正在修改变量：", self.name)
        self.val = value

    def __delete__(self, instance):
        print("正在删除变量", self.name)
        print("无法删除")

class Test:
    x = MyDes(10,'x')

test = Test()
y = test.x
print(y)
test.x = 8
del test.x
print(test.x)


print("\n")
# 按要求编写描述符MyDes
# 记录指定变量的读取和写入操作，并将记录以及触发时间保存到文件
# record.txt
import time 

class Record:
    def __init__(self, initval=None, name=None):
        self.val = initval
        self.name = name 
        self.filename = 'record.txt'

    def __get__(self, instance, owner):
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write("%s 变量于北京时间 %s 被读取， %s = %s\n" %
                    (self.name, time.ctime(), self.name, str(self.val)))
        return self.val

    def __set__(self, instance ,value):
        filename = "%s_record.txt" % self.name
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write("%s 变量于北京时间 %s 被修改， %s = %s\n" %
                    (self.name, time.ctime(), self.name, str(self.val)))
        self.val = value

class Test:
    x = Record(10,'x')
    y = Record(8.8,'y')

test = Test()
print(test.x)
print(test.y)
test.x = 123
test.y = 1.23
test.y = "i love fishc.com"



print("\n")
# 编写描述符MyDes，使用文件来存储属性，属性的值会直接存储到对应的pickle（腌菜）的文件中
# 如果属性被删除了，文件也会同时被删除，属性的名字也会被注销
# python的pickle模块实现了基本的数据序列和反序列化。
# 通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
import os 
import pickle

class MyDes:
    saved = []

    def __init__(self, name=None):
        self.name =  name 
        self.filename = self.name + '.pkl'

    def __get__(self, instance, owner):
        if self.name not in MyDes.saved:
            raise AttributeError("%s 属性还没有赋值！" % self.name)

        # rb 只读二进制
        with open(self.filename,'rb') as f:
            value = pickle.load(f)
        
        return value

    def __set__(self, instance, value):
        with open(self.filename, 'wb') as f:
            pickle.dump(value, f)
            MyDes.saved.append(self.name)

    def __delete__(self, instance):
        os.remove(self.filename)
        MyDes.saved.remove(self.name)

class Test:
        x = MyDes('x')
        y = MyDes('y')
        
test = Test()
test.x = 123
test.y = "I love FishC.com!"
print(test.x)
print(test.y)
