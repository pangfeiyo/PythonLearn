# 5-3  外星人颜色
# #1  ：假设在游戏中刚射杀了一个外星人，请创建一个名为 alien_color 的变量，并将其设置为 'green' 、 'yellow' 或 'red' 。
# 编写一条 if 语句，检查外星人是否是绿色的；如果是，就打印一条消息，指出玩家获得了 5 个点。
# 编写这个程序的两个版本，在一个版本中上述测试通过了，而在另一个版本中未通过（未通过测试时没有输出）。
alien_color = 'green'
if alien_color == 'green':
    print("player have 5")
if alien_color != 'green':
    print("player have 5")

print()
# 5-4  外星人颜色
# 2  ：像练习 5-3 那样设置外星人的颜色，并编写一个 if-else 结构。
# 如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了 5 个点。
# 如果外星人不是绿色的，就打印一条消息，指出玩家获得了 10 个点。
# 编写这个程序的两个版本，在一个版本中执行 if 代码块，而在另一个版本中执行 else 代码块。
alien_color = 'green'
if alien_color == 'green':
    print('player have 5')
else:
    print('player have 10')

if alien_color == 'green':
    print('player have 5')
if alien_color != 'green':
    print('player have 10')


# 5-5  外星人颜色
# 3  ：将练习 5-4 中的 if-else 结构改为 if-elif-else 结构。
# 如果外星人是绿色的，就打印一条消息，指出玩家获得了 5 个点。
# 如果外星人是黄色的，就打印一条消息，指出玩家获得了 10 个点。
# 如果外星人是红色的，就打印一条消息，指出玩家获得了 15 个点。
# 编写这个程序的三个版本，它们分别在外星人为绿色、黄色和红色时打印一条消息。
print('\n5-5 3:')
alien_color = 'green'
if alien_color == 'green':
    print('player have 5')
elif alien_color == 'yellow':
    print('player have 10')
else:
    print('player have 15')
#三个版本不写了没意义


print('\n5-7:')
# 5-7  喜欢的水果 ：创建一个列表，其中包含你喜欢的水果，再编写一系列独立的 if 语句，检查列表中是否包含特定的水果。
# 将该列表命名为 favorite_fruits ，并在其中包含三种水果。
# 编写 5 条 if 语句，每条都检查某种水果是否包含在列表中，如果包含在列表中，就打印一条消息，如 “You really like bananas!” 。
favorite_fruits = ['xigua','caomei','huolongguo']
shuiguo = 'xigua'
if shuiguo in favorite_fruits:
    print(shuiguo, 'in favorite_frnits')
shuiguo = 'caomei'
if shuiguo in favorite_fruits:
    print(shuiguo, 'in favorite_frnits')

