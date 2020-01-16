#讲列表中的两个元素调换位置
member = ['小甲鱼','牡丹','水仙','花']
print(member)
temp = member[0]
member[0] = member[1]
member[1] = temp
print(member)


#删除元素   .remove
member.remove('牡丹')
print(member)
member.remove(member[1])
print(member)

#删除元素   del语句
del member[1]
print('del:',member)

del member[0]
print('del:',member)

#删除元素 pop()    删除最后一个元素
#也可以pop(1)
print()
print("pop")
member = ['小甲鱼','牡丹','水仙','花']
print(member)
print(member.pop())
print(member)


print(),print('分片')
#列表分片（切片）
#一次获取多个元素
member = ['小甲鱼','牡丹','水仙','花']
print(member)
print(member[1:3])      #从1开始，到3之前，不包换3   不会原列表造成改变
print(member[:3])       #省去从0开始
print(member[:])        #省去开始到结尾，拷贝完整列表


print(),print("切片  步长")
#切片  步长
list2 = [1,3,2,9,7,8]
print(list2[::2])   #从开始到结束，每次加2

#步长可以为负，改变方向（从尾部开始向左走）
print(list2[::-2])
