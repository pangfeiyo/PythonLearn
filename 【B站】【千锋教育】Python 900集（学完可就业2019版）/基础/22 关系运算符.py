n1 = 8
n2 = 5 

result = n1 > n2
print("n1 > n2:", result)

result = n1 == n2   # 赋值运算的优先级较低，先判断n1==n2
print("n1 == n2", result)

m1 = "hello"
m2 = "hello"
result = m1 == m2
print("m1==m2:", result)

# username = input("输入用户名：")
# uname = "admin123"
# result = username != uname 	# 如果两个不相等时返回True，相等时返回False
# print("用户名的验证结果是：", result)


# is 用户对象的比较
age = 20
age1 = 20
print(id(age))	# id()用于获取对象的内存地址
print(id(age1))
print("age is age1:",age is age1)

money = 999999
salary = 1000000
print(id(money))
print(id(salary))
print("money is salary:",money is salary)

'''
在交互式环境（CMD）下money,salary是不同地址
在源文件下，是同一地址

是因为源文件在处理时是批量处理的，是将文件一次性送入解释器，自上而下开始
发现有两个200万，会复用

交互式中是所见即所得，默认有一个小整数对象池，在[-5,256]之间会进入池子中，相当复用，不会垃圾回收

'''