def MyFirstFunction(name):
    ' 函数定义过程中的name是叫形参'        #这是函数文档，功能和注释一样不会被打印
    # 因为Ta只是一个形式，表示占据一个参数位置
    print('传递进来的' + name + '叫做实参，因为Ta是具体的参数值！')

MyFirstFunction('小甲鱼')

#查看自定义函数 MyFirstFunction的函数文档
print(MyFirstFunction.__doc__)
#print(help(MyFirstFunction))

#print(print.__doc__)

#print(help(print))

'''
def SaySome(name,words):
    print(name + " -> " + words)
SaySome("小甲鱼","让编程改变世界")
SaySome('让编程改变世界','小甲鱼')
SaySome(words='让编程改变世界',name='小甲鱼')         #关键字参数
'''
def SaySomes(name='小甲鱼',words='让编程改变世界'):
    '这叫默认参数，依旧可以传入参数'
    print(name + " -> " + words)
SaySomes()
SaySomes('一地在要工','上是中国同')


#收集参数
#把标志是收集参数的参数把他用元组给打包起来
#若还有其他自定义函数，需要使用关键字参数，否则python会把所有参数传给收集参数
def test(*params):
    print('参数的长度是：',len(params))
    print('第二个参数是：',params[1])
test(1,'小甲鱼',3.14,5,6,7,8)

def test(*params,exp):
    print('参数的长度是：',len(params),exp)
    print('第二个参数是：',params[1])
test(1,'小甲鱼',3.14,5,6,7,8,exp=1)
def test(*params,exp=1):
    print('参数的长度是：',len(params),exp)
    print('第二个参数是：',params[1])
test(1,'小甲鱼',3.14,5,6,7,8,exp=1)

