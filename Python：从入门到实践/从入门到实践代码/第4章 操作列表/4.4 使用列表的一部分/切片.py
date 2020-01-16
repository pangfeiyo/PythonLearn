# 要创建切片，可指定要使用的第一个元素和最后一个元素的索引。与函数 range() 一样， Python 在到达你指定的第二个索引前面的元素后停止。
# 要输出列表中的前三个元素，需要指定索引 0~3 ，这将输出分别为 0 、 1 和 2 的元素。
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
# 如果你没有指定第一个索引， Python 将自动从列表开头开始
print(players[:4])
# 要让切片终止于列表末尾，也可使用类似的语法
print(players[2:])
# 负数索引返回离列表末尾相应距离的元素，因此你可以输出列表末尾的任何切片。
# 例如，如果你要输出名单上的最后三名队员，可使用切片 players[-3:]
print(players[-3:])

# 如果要遍历列表的部分元素，可在 for 循环中使用切片
# 在下面的示例中，我们遍历前三名队员，并打印他们的名字：
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("前三名队员是：")
for player in players[:3]:
    print(player.title())


# 复制列表
# 要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引（ [:] ）
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My favorite food are:',my_foods)
print("My friend's favorite food are:",friend_foods)