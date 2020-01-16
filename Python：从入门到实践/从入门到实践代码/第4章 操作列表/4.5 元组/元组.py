# 列表非常适合用于存储在程序运行期间可能变化的数据集。列表是可以修改的，这对处理网站的用户列表或游戏中的角色列表至关重要。
# 然而，有时候你需要创建一系列不可修改的元素，元组可以满足这种需求。
# Python 将不能修改的值称为 不可变的 ，而不可变的列表被称为 元组

# 元组不可改

# 4.5.1 　定义元组
# 元组看起来犹如列表，但使用圆括号而不是方括号来标识。定义元组后，就可以使用索引来访问其元素，就像访问列表元素一样。
# 例如，如果有一个大小不应改变的矩形，可将其长度和宽度存储在一个元组中，从而确保它们是不能修改的
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# 4.5.2 　遍历元组中的所有值
# 像列表一样，也可以使用 for 循环来遍历元组中的所有值
dimensions = (200,50)
for dimension in dimensions:
    print(dimension)

# 4.5.3 　修改元组变量
# 虽然不能修改元组的元素，但可以给存储元组的变量赋值。因此，如果要修改前述矩形的尺寸，可重新定义整个元组
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print('Modified dimensions:')
for dimension in dimensions:
    print(dimension)


