# 6.4 　嵌套
# 有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为 嵌套 。
# 你可以在列表中嵌套字典、在字典中嵌套列表甚至在字典中嵌套字典。正如下面的示例将演示的，嵌套是一项强大的功能。
# 6.4.1 　字典列表
# 字典 alien_0 包含一个外星人的各种信息，但无法存储第二个外星人的信息，更别说屏幕上全部外星人的信息了。
# 如何管理成群结队的外星人呢？一种办法是创建一个外星人列表，其中每个外星人都是一个字典，包含有关该外星人的各种信息。
# 例如，下面的代码创建一个包含三个外星人的列表：
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)
print("……")
# 更符合现实的情形是，外星人不止三个，且每个外星人都是使用代码自动生成的。
# 在下面的示例中，我们使用 range() 生成了 30 个外星人：
# 创建一个用于存储外星人的空列表
aliens = []
# 创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
# 显示前五个外星人：
for alien in aliens[:5]:
    print(alien)
# 显示创建了多少个外星人
print('Total number of aliens:',len(aliens))
print('……')


# 在什么情况下需要处理成群结队的外星人呢？想象一下，可能随着游戏的进行，有些外星人会变色且移动速度会加快。
# 必要时，我们可以使用 for 循环和 if 语句来修改某些外星人的颜色。
# 例如，要将前三个外星人修改为黄色的、速度为中等且值 10 个点，可以这样做：
# 创建一个用于存储外星人的空列表
aliens = []
# 创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
# 把字典中下标为2 的键改为 'yellow' ，这样就可以触发 elif:  里的判定，将黄色改为红字等
aliens[2]['color'] = 'yellow'

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
# 你可以进一步扩展这个循环，在其中添加一个 elif 代码块，将黄色外星人改为移动速度快且值15
# 个点的红色外星人，如下所示（这里只列出了循环，而没有列出整个程序）：
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'
# 显示前五个外星人：
for alien in aliens[:5]:
    print(alien)
# 显示创建了多少个外星人
print('Total number of aliens:',len(aliens))