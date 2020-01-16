old = [1,2,3,4,5]
new = old
old = [5,4,3,2,1]
print(new)
print(old)


#将甲鱼修改为鱿鱼
list1 = [1,[1,2,['甲鱼']],3,5,8,13,18]
list1[1][2][0]='鱿鱼'
print(list1)

#顺序排序
list2=[3,7,2,4,9,8]
list2.sort()
print(list2)

#逆序排序
#方法一
list2=[3,7,2,4,9,8]
list2.sort()
list2.reverse()
print(list2)

#方法二
list2=[3,7,2,4,9,8]
list2.sort(reverse=True)
print(list2)


#copy()  复制     copy()方法跟使用切片拷贝是一样的
list3 = list1.copy()
print(list3)

#clear()方法用于清空列表的元素，但列表还在，变成空列表
list3.clear()
print(list3)

