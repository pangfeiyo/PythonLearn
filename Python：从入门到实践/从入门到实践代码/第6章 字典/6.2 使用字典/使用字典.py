# 6.2 　使用字典
# 在 Python 中， 字典 是一系列 键 — 值对 。每个 键 都与一个值相关联，你可以使用键来访问与之相关联的值。与键相关联的值可以是数字、字符串、列表乃至字典。事实上，可将
# 任何 Python 对象用作字典中的值。
# 在 Python 中，字典用放在花括号 {} 中的一系列键 — 值对表示，如前面的示例所示
alien_0 = {'color': 'green', 'points': 5}

# 键 — 值 对是两个相关联的值。指定键时， Python 将返回与之相关联的值。键和值之间用冒号分隔，而键 — 值对之间用逗号分隔。
# 在字典中，你想存储多少个键 — 值对都可以。最简单的字典只有一个键 — 值对，如下述修改后的字典 alien_0 所示：
alien_1 = {'color': 'green'}
# 这个字典只存储了一项有关 alien_0 的信息，具体地说是这个外星人的颜色。在这个字典中，字符串 'color' 是一个键，与之相关联的值为 'green'


# 6.2.1 　访问字典中的值
# 要获取与键相关联的值，可依次指定字典名和放在方括号内的键，如下所示：
print(alien_1['color'])

# 访问外星人 alien_0 的颜色和点数。如果玩家射杀了这个外星人，你就可以使用下面的代码来确定玩家应获得多少个点：
new_points = alien_0['points']
print('You just earned',new_points,'points!')


# 6.2.2 　添加键 — 值对
# 字典是一种动态结构，可随时在其中添加键 — 值对。要添加键 — 值对，可依次指定字典名、用方括号括起的键和相关联的值。
# 下面在字典 alien_0 中添加两项信息：外星人的 x  坐标和 y  坐标，让我们能够在屏幕的特定位置显示该外星人。
# 我们将这个外星人放在屏幕左边缘，且离屏幕上边缘 25 像素的地方。
# 由于屏幕坐标系的原点通常为左上角，因此要将该外星人放在屏幕左边缘，可将 x  坐标设置为 0 ；
# 要将该外星人放在离屏幕顶部 25 像素的地方，可将 y  坐标设置为 25 如下所示：
print('\n6.2.2 添加 键 - 值 对')
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


# 6.2.3 　先创建一个空字典
# 有时候，在空字典中添加键 — 值对是为了方便，而有时候必须这样做。为此，可先使用一对空的花括号定义一个字典，再分行添加各个键 — 值对。例如，下例演示了如何以这种
# 方式创建字典 alien_0 ：
print('\n6.2.3')
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)


# 6.2.4 　修改字典中的值
# 要修改字典中的值，可依次指定字典名、用方括号括起的键以及与该键相关联的新值。
# 例如，假设随着游戏的进行，需要将一个外星人从绿色改为黄色：
print('\n6.2.4 修改字典的值')
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

# 来看一个更有趣的例子：对一个能够以不同速度移动的外星人的位置进行跟踪。
# 为此，我们将存储该外星人的当前速度，并据此确定该外星人将向右移动多远：
print('\n')
alien_0 = {'x_position':0, 'y_position':25, 'speed':'medium'}
print('Original x-position:',alien_0['x_position'])
#  向右移动外星人
#  据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人的速度一定很快
    x_increment = 3
# 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print('New x-position:',alien_0['x_position'])


# 6.2.5 　删除键 — 值对
# 对于字典中不再需要的信息，可使用 del 语句将相应的键 — 值对彻底删除。使用 del 语句时，必须指定字典名和要删除的键。
# 例如，下面的代码从字典 alien_0 中删除键 'points' 及其值
print('\n删除键 - 值对')
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)


# 6.2.6 　由类似对象组成的字典
# 在前面的示例中，字典存储的是一个对象（游戏中的一个外星人）的多种信息，但你也可以使用字典来存储众多对象的同一种信息。
# 例如，假设你要调查很多人，询问他们最喜欢的编程语言，可使用一个字典来存储这种简单调查的结果，如下所示：
print('\n6.2.6 　由类似对象组成的字典')
favorite_languages = {
    'jen':'python',
    'sarch':'c',
    'edward':'ruby',
    'phil':'python'
    }
print("Sarah's favorite language is",favorite_languages['sarch'].title())