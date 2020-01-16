# 工厂函数
print(type(len))

print(type(len))

print(type(int))

print(type(list))

class C:
    pass
print(type(C))

# 工厂函数是类对象


a = int("123")
print(a)
print(type(a))

b = int(456)
print(b)

print(a+b)



class New_int(int):
    def __add__(self,other):
        return int.__sub__(self, other)
    def __sub__(self,other):    #减法
        return int.__add__(self, other)

a = New_int(3)
b = 5
print("a  new_int")
print("a+b: ",a+b)
print("a-b: ",a-b)

print("b+a: ",b+a)
print("b-a: ",b-a)

print("\na与b都new_int")
b = New_int(5)
print("a+b: ",a+b)
print("a-b: ",a-b)

print("b+a: ",b+a)
print("b-a: ",b-a)




'''
class Try_int(int):
    def __add__(self,other):
        return self + other
    def __sub__(self,other):
        return self - other
a = Try_int(3)
b = Try_int(5)
print(a+b)
会报错，因为在a+b时，出现+ 会自动调用前者a的__add__方法，会返回 self + other 
self是什么，self是实例化对象绑定进来的一个方式 ，这里就是a，other是加法右边的数，这里是b
return的又是a+b，继续__add__，进入无限递归
'''
# 可以这么改
class Try_int(int):
    def __add__(self,other):
        return int(self) + int(other)
    def __sub__(self,other):
        return int(self) - int(other)
a = Try_int(3)
b = Try_int(5)
print("\n" , a+b)