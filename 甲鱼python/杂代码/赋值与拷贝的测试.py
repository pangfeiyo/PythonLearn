list1 = [1,3,4,2]
list2 = list1[:]
list3 =list1

print('list1:',list1)
print('list2:',list2)
print('list3:',list3)

print(),print("排序之后的list")
list1.sort()
print('list1:',list1)
print('list2:',list2)
print('list3:',list3)

print(),print("向list1新加一个元素")
list1.append(233)
print('list1:',list1)
print('list2:',list2)
print('list3:',list3)

print(),print("改变list1的列表")
list1 = [6,9,2,4]
print('list1:',list1)
print('list2:',list2)
print('list3:',list3)
