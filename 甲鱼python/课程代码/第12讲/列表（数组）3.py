#常用操作符

list1= [123]
list2= [234]
print(list1 > list2)

list1 = [123,456]
list2 = [456,123]
print(list1 > list2)    #如果有多个元素，第一个为false的话，结果就是FALSE，不考虑后面

list4 = list1 + list2
print('list4：',list4)

list5 = [123,['甲鱼','牡丹'],456]
print('甲鱼' in list5)
print('甲鱼' in list5[1])
print(list5[1][1])

print(dir(list))

list3 = [123,456]
list3 *= 3
list3 *= 5
print(list3)
print(list3.count(123))  #次数

# index  在列表中的位置
print(list3.index(123))
# 从下标为3开始，到下标为7结束，查123第一次出现在哪
print(list3.index(123,3,7))


#reverse 将整个列表顺序反转
list6 = [9,6,4,3,1,5,7]
list6.reverse()
print('reverse：',list6)

#对列表中的数字从小到大排列
list7 = [78,11,30,0,45,97,3,21]
list7.reverse()     #列表顺序反转
print('list7的反转：',list7)
list7.sort()       #大小排序，从小到大
print('list7排序：',list7)

# sort(func, key, reverse)
#func 排序搭配的算法    key 关键字    前两者都是默认
#reverse 默认值为false
list7.sort(reverse=True)   #True 从大到小  false 从小到大
print(list7)
