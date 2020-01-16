# 封装 对外部隐藏对象的工作细节
class Turtle:   # Python 中的类名约定以大写字母开头
    '''关于类的一个简单例子'''
    # 属性
    color = 'green'
    weight = 10
    legs = 4
    shell = True
    mouth = '大嘴'

    # 方法
    def climb(self):
        print("向前爬")

    def run(self):
        print("向前跑")

    def bite(self):
        print("咬人")

    def eat(self):
        print("吃东西")

    def sleep(self):
        print("睡觉")

# Turtle()
tt = Turtle()
tt.climb()

# OO的特征
# OO = Object Oriente 面向对象

list1 = [2,3,1,5,4]
list1.sort()    # 排序
print(list1)
list1.append(9)
print(list1)


# 子类自动共享父类之间的数据和方法的机制
# 继承list这个列表（方法或属性）
# class 子类(父类)
class MyList(list):
    pass

list2 = MyList()
list2.append(5)
list2.append(3)
list2.append(7)
print("list2:",list2)
list2.sort()
print(list2)

# 多态 可以对不同类的对象调用相同的方法，产生不同的结果
# 多态：不同对象对同一方法响应不同的行动
class A:
    def fun(self):
        print("我是A...")

class B:
    def fun(self):
        print("我是B...")

a = A()
b = B()
a.fun()
b.fun()