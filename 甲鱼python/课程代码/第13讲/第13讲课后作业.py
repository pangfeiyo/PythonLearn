x, y, z = 1, 2, 3
print(type(x))

h = x, y, z
print(type(h))

#这里不会报错，因为得到了一个生成器  generator
list1 = (x**2 for x in range(10))
print("list1：",list1)

print(list1.__next__())
print(list1.__next__())
print(list1.__next__())
print(list1.__next__())
print(list1.__next__())
print(list1.__next__())
print(list1.__next__())
print(list1.__next__())
print(list1.__next__())
print(list1.__next__())