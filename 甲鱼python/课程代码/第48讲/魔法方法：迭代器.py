# 通常使用for语句迭代
for i in "Fishc":
    print(i)

# 每次从容器里依次拿出一个数据，就是迭代操作
# 字典和文件也是支持迭代的
links = {'鱼C工作室':'http://www.fishc.com',
         '鱼C论坛':'http://bbc.fishc.com',
         '鱼C博客':'http://blog.fishc.com',
         '支持小甲鱼':'http://fishc.taobao.com'}
for each in links:
    print("%s -> %s" % (each, links[each]))


# 关于迭代，python自带两个内置函数
# iter()和next()
# 对一个容器对象调用iter()就会得到他的迭代器
# 调用next()就会返回下一个值 
# 如何结束？如果没有返回了就会抛出一个StopIterationn异常

string = 'Fishc'
it = iter(string)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))  第六个会报错


print()
string = 'FishC'
it = iter(string)
while True:
    try:
        each = next(it)
    except StopIteration:
        break
    print(each)



print()
for each in string:
    print(each)



print()
# 迭代器的魔法方法
# __iter__()  返回迭代器本身
# __next__()  决定迭代器的规则
class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

fibs = Fibs()
# 会一直循环下去
#for each in fibs:
#    print(each)
for each in fibs:
    if each < 20:
        print(each)
    else:
        break


# 以下是改进代码，加入控制次数
print("\n加入了数量控制")
class Fibs:
    def __init__(self,n=20):
        self.a = 0
        self.b = 1
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > self.n:
            raise StopIteration
        else:
            return self.a

fibs = Fibs()
# 会一直循环下去
#for each in fibs:
#    print(each)
for each in fibs:
    if each < 20:
        print(each)
    else:
        break