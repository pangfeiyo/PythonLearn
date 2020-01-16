# 5-8  以特殊方式跟管理员打招呼 ：创建一个至少包含 5 个用户名的列表，且其中一个用户名为 'admin' 。
# 想象你要编写代码，在每位用户登录网站后都打印一条问候消息。遍历用户名列表，并向每位用户打印一条问候消息。
# 如果用户名为 'admin' ，就打印一条特殊的问候消息，如 “Hello admin, would you like to see a status report?” 。
# 否则，打印一条普通的问候消息，如 “Hello Eric, thank you for logging in again” 。
names = ['wang','li','liu','admin','zhang']
for name in names:
    if name == 'admin':
        print("Hello",name,"would you like to see a status report?")
    else:
        print("hello" , name)


# 5-9  处理没有用户的情形 ：在为完成练习 5-8 编写的程序中，添加一条 if 语句，检查用户名列表是否为空。
# 如果为空，就打印消息 “We need to find some users!” 。
# 删除列表中的所有用户名，确定将打印正确的消息。
print('\n5-9:')
names = []
if names:
    for name in names:
        if name == 'admin':
            print("Hello", name, "would you like to see a status report?")
        else:
            print("hello", name)
else:
    print('We need to find some users!')


# 5-10  检查用户名 ：按下面的说明编写一个程序，模拟网站确保每位用户的用户名都独一无二的方式。
# 创建一个至少包含 5 个用户名的列表，并将其命名为 current_users 。
# 再创建一个包含 5 个用户名的列表，将其命名为 new_users ，并确保其中有一两个用户名也包含在列表 current_users 中。
# 遍历列表 new_users ，对于其中的每个用户名，都检查它是否已被使用。
# 如果是这样，就打印一条消息，指出需要输入别的用户名；否则，打印一条消息，指出这个用户名未被使用。
# 确保比较时不区分大小写；换句话说，如果用户名 'John' 已被使用，应拒绝用户名 'JOHN' 。
print('\n5-10:')
current_users =  ['wanG','LI','lIu','qiAn','Zhang']
# 这里把 current_users  列表里的值转为小写。  用的是列表解析写法
current_users_lower = [name_lower.lower() for name_lower in current_users]
# 写法二，正常写法，有点长
# current_users_lower = []
# for name_lower in current_users:
#     current_users_lower.append(name_lower.lower())
new_users = ['Luna','SNK','zhanG','coco','LI']
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("已被注册，请输入其他用户名！")
    else:
        print('恭喜你，该用户名未被使用！')


# 5-11  序数 ：序数表示位置，如 1st 和 2nd 。大多数序数都以 th 结尾，只有 1 、 2 和 3 例外。
# 在一个列表中存储数字 1~9 。
# 遍历这个列表。
# 在循环中使用一个 if-elif-else 结构，以打印每个数字对应的序数。
# 输出内容应为 1st 、 2nd 、 3rd 、 4th 、 5th 、 6th 、 7th 、 8th 和 9th ，但每个序数都独占一行。
numbers = ['1','2','3','4','5','6','7','8','9']
for number in numbers:
    # print(number)
    if number == '1':
        print(number+'st')
    elif number == '2':
        print(number+'nd')
    elif number == '3':
        print(number+'rd')
    else:
        print(number+'th')