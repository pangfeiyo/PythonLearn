#元组插入内容和列表是不一样的，元组插件和字符串是一样的
#元组和列表最大的区别，列表可以随意修改，元组不行
#创建元组 大部分 使用()
tuple1 = (1,2,3,4,5,6,7,8)
print(tuple1)
print(tuple1[2])

tuple2 = (6)
print(tuple2)

print(type(tuple1)) #返回值为 tuple   元组
print(type(tuple2)) #返回值为  int

#创建元组可以不加括号，重要的是逗号。
#创建空元组，需要加小括号
temp2 = 2,3,4
print('type2:',type(temp2))

temp3 = (1,)
print('temp3:',type(temp3))

temp4 = 8 * (8)
print(temp4)

#括号里面的内容是元组， * 不再是乘，而是重复操作符。同列表一样
temp5 = 8 * (8,)
print(temp5)

#元组插入新元素
abc = ('甲鱼','黑夜','作为','而在')
abc = abc[:2] + ('怡静',) + abc[2:]       #当添加完成后，上一条的四个元素的元组没有指向，py会自动删除
print(abc)                                  #如果没有abc = abc    新插入的元组不会改变原来的ABC，相当于再建个新的

#删除整个元组
del abc
print(abc) #这里是输出不了的，因为已经给删掉元组了