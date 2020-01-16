#列表推导式  或   列表解析
abc = [i*i for i in range(10)]
print('abc：',abc)

# [有关A 的表达式 for A in B]
list1 = [x**2 for x in range(10)]
print("list1：",list1)
#相当于
list1 = []
for x in range(10):
    list1.append(x ** 2)
print("相当于list1：",list1)


#推导
list3 = [(x,y) for x in range(10) for y in range(10) if x % 2 == 0 if y % 2 == 0]
print(list3)

list4 = []
for x in range(10):
    for y in range(10):
        if x % 2 ==0:
            if y % 2 ==0:
                list4.append((x,y))
print(list4)



t1 = ['1.Jost do It','2.一切皆有可能','3.让编程改变世界','4.Impossible is Nothing']
t2 = ['4.阿迪达斯','2.李宁','3.鱼C工作室','1.耐克']
t3 = [name + '：' + slogan[2:] for slogan in t1 for name in t2 if slogan[0] == name[0]]
for each in t3:
    print(each)


# t3推导
t3 = []
for name in t2:
    for slogan in t1:
        if slogan[0] == name[0]:
            t3.append(name + "：" + slogan[2:])
print(t3)
t3.sort()
print(t3)
