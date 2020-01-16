for value in range(1,5):
    print(value)        #输出为1~4

#使用range()创建数字列表
#可使用函数 list()将range()的结果直接转换为列表
number = list(range(1,5))
print(number)
#range()的步长    从2开始，每次+2，到11结束
even_numbers = list(range(2,11,2))
print(even_numbers)

#创建一个列表，包含前10个整数（1 - 10）的平方
#方法一
squares= []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

#更简洁的方法二
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)

#最大、最小、和
print('最大',max(squares))
print('最小',min(squares))
print('和',sum(squares))