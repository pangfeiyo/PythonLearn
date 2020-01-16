#有返回值的叫函数，没有返回值的叫过程
#python严格来说只有函数，没有过程
def hello():
    print("hello word")
temp = hello()
print(temp)
print(type(temp))

#返回多个值
def back():
    return [1,'小甲鱼',3.14]
print(back())

def back():
    return 1,'小甲鱼',3.14
print(back())


#全局变量和局部变量
def discounts(price,rate):
    final_price = price * rate
    old_price  = 50
    print("修改后 old_price 的值是1：",old_price)
    return final_price

old_price = float(input('请输入原价：'))
rate = float(input('请输入折扣率：'))
new_price = discounts(old_price, rate)
print('修改后的old_price的值是2：',old_price)
print('打折后的值是：',new_price)
#print('这里试图打印局部变量final_price的值：',final_price)   #这句会提示报错，因为 final_price只存在于函数discounts里面，是局部变量
'''若在函数内修改已定义的全局变量，python会自动在函数内创建一个同全局变量同一个名字的局部变量'''
'''
old_price = 88  # 这里试图修改全局变量
print('修改后的old_price的值是：', old_price)
'''