#del 和 pop() 的区别，
#如果你要从列表中删除一个元素，并不再使用它，使用 del
#如果你要在列表中删除一个元素后并继续使用它，使用 pop()方法

#使用 del 语句
motoche = ['honda','yamaha','suzuki']
print(motoche)
print(motoche[0])

del motoche[0]
print(motoche)
print(motoche[0])

del motoche[1]
print(motoche)

print()
print('以下是pop()方法')
#使用 pop()方法删除
#有时候，你要将元素从列表中删除，并接着使用它的值。  方法 pop()可删除列表末尾的元素，并让你能够接着使用它。
motoche = ['honda','yamaha','suzuki']
print(motoche)

popped_motoche = motoche.pop()
print(motoche)
print(popped_motoche)

#
print(),print()
#假设列表中的摩托车是按购买时间存储的，指出最后购买的是哪款车
motoche = ['honda','yamaha','suzuki']
last_owned = motoche.pop()
print('最后购买的摩托车是：' + last_owned.title())   #title() 首字母大写

print()
#可以使用pop() 删除列表中任何元素的位置，只需在括号中指定要删除的元素的索引即可。
motoche = ['honda','yamaha','suzuki']
first_owned = motoche.pop(0)
print('the First motoche is '+first_owned)
print(motoche)


# 4.根据值删除元素 .remove()
#有时候你不知道从列表中删除的值所处的位置。如果你只知道要删除的元素的值，使用方法 .remove()
print(),print('4.根据值删除元素')
motoche = ['honda','yamaha','suzuki']
print(motoche)
motoche.remove('yamaha')
print(motoche)

#使用 remove()方法从列表中删除元素时，也可以接着使用它的值。
print(),print('使用 remove()方法从列表中删除元素时，也可以接着使用它的值')
motoche = ['honda','yamaha','suzuki']
print(motoche)
too_expensive = 'yamaha'
motoche.remove(too_expensive)
print(motoche)
print("\nA " + too_expensive.title() + " is too_expensive for me.")
#remove()方法只能删除第一个指定的值。如果要删除的值可能在列表中出现很多次，需要使用循环来判定是否全部删除。将在第7 章学习