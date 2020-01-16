# def  创建一个函数
def MyFirstFunction():
    print('这是我创建的第一个函数！')
    print('我表示很激动！')
    print('在此，我要感谢TVB！')
#调用函数   函数调用不需要print()
#调用函数向上查找
MyFirstFunction()

#单参数
def MySecondFunction(name):
    print(name + "我爱你")
MySecondFunction('甲鱼')

#多参数
def add(num1,num2):
    result = 0
    result = num1 +num2
    print(result)
add(1,2)

#函数的返回值
def add2(num1,num2):
    return (num1+num2) # () 不是必须的
add(5,6)

