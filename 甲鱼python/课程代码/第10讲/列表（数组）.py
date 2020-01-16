menber = ['小甲鱼','大甲鱼',1,36.14,[1,2,3]]
print(menber)
print(len(menber))

empty=[]
print(empty)

# .append  向数组加入一个新值，放在最后
menber.append('娃娃')
print(menber)
print(len(menber))

# extend  加入多个信息，放在最后，相当于加入一个列表，要加[]
menber.extend(['竹林','黑夜'])
print(menber)

# insert ，插入某个位置
menber.insert(1,'牡丹')
print(menber)
