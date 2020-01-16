players = ['charles', 'martina', 'michael', 'florence', 'eli']
# 用切片打印前三
print('The first three items in the list are:',players[:3])
# 用切片打印中间三个
print('The first three items in the list are:',players[1:4])
# 用切片打印最后三个
print('The first three items in the list are:',players[-3:])

# 创建比萨列表的副本，并将其存储到变量 friend_pizzas
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
# 在原来的比萨列表中添加一种比萨
my_foods.append('hanbo')
# 在列表 friend_pizzas 中添加另一种比萨
friend_foods.append('shutiao')
print('My favorite pizzas are:')
for food in my_foods:
    print(food)
print('My Friend favorite pizzas are:')
for food in friend_foods:
    print(food)