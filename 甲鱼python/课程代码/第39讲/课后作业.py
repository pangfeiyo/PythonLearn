# 在一个类中定义一个变量，用于跟踪该类有多少个实例被创建
# （当实例化一个对象，这个变量+1，删除时-1）
class C:
    count = 0

    def __init__(self):
        C.count+=1
    def __del__(self):
        C.count-=1
a = C()
b = C()
c = C()
print(C.count)
del a
print(C.count)
del b, c
print(C.count)


# 1.定义一个栈（Stack）类，用于模拟一种具有后进先出（LIFO）特性的数据结构。
'''
push()----      ---- pop()
          \    /
  top() -->  F
             i
             s
             h
 bose() -->  C

至少需要有以下方法
isEmpty()   判断当前栈是否返回为空（返回True或False）
push()      往栈的顶部压入一个数据项
pop()       从栈顶弹出一个数据项（并在栈中删除)
top()       显示当前栈顶的一个数据项
bottom()    显示当前栈底的一个数据项
'''
class Stack:
    def __init__(self, start = []):
        self.stack = []
        for x in start:
            self.push(x)
    
    def isEmpty(self):
        # not **  类似判断语句 返回True或False
        # 如果是空返回True
        return not self.stack

    def push(self, obj):
        self.stack.append(obj)

    def pop(self):
        if not self.stack:
            print("警告:栈为空！")
        else:
            return self.stack.pop()

    def top(self):
        if not self.stack:
            print("警告：栈为空！")
        else:
            return self.stack[-1]

    def bottom(self):
        if not self.stack:
            print("警告：栈为空！")
        else:
            return self.stack[0]

stack = Stack(start=['aaa'])
print(stack.bottom())
stack.push(123)
print(stack.top())