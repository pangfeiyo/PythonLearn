# 生成器generator，只需在普通的函数里加入yield语句
# 所谓的协同程序就是可以运行的独立函数调用，函数可以暂停或挂起，
# 并在需要的时候从程序离开的地方继续或者重新开始
def myGen():
    print("生成器被执行")
    yield 1
    yield 2

myG = myGen()
print(next(myG))
print(next(myG))

myG = myGen()
for i in myG:
    print(i)



def libs():
    a = 0
    b = 1
    while True:
        a, b = b, a + b
        yield a

for each in libs():
    if each > 100:
        break
    print(each, end=" ")

print()

# 列表推导式
# 能被2整除，但不能被3整除的所有数
# 1为True ， 0为False
a = [i for i in range(100) if not (i % 2) and i % 3]
print(a)

# 字典推导式
# 显示0-9这几个数是否为偶数，如果是为True
b = {i:i % 2 == 0 for i in range(10)}
print(b)

# 集合推导式
c = {i for i in [1,1,2,3,4,5,5,6,7,8,3,2,1]}
print(c)
    

# 字符串推导式  不行
d = "i for i in 'l love fishC.com!"
print(d)

# 元组推导式 元组叫tuple
e = (i for i in range(10))
print(e)
# 这里不输出内容，输出一串字符串 <generator object <genexpr> at 0x00000287BBDDD200>
# generator 是生成器
# 用普通（）括起来的生成，就是生成器推导式
print(next(e))
print(next(e))
print(next(e))
print(next(e))
for each in e:
    print(each)
 
# 生成器推导式如果做为函数的参数，可直接写推导式
s = sum(i for i in range(100) if i % 2)
print(s)