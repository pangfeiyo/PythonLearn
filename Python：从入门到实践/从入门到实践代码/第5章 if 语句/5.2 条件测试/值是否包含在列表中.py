# 5.2.6 　检查特定值是否包含在列表中
# 有时候，执行操作前必须检查列表是否包含特定的值。
# 例如，结束用户的注册过程前，可能需要检查他提供的用户名是否已包含在用户名列表中。
# 在地图程序中，可能需要检查用户提交的位置是否包含在已知位置列表中。
# 要判断特定的值是否已包含在列表中，可使用关键字 in 。来看你可能为比萨店编写的一些代码；
# 这些代码首先创建一个列表，其中包含用户点的比萨配料，然后检查特定的配料是否包含在该列表中。
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)


# 5.2.7 　检查特定值是否不包含在列表中
# 还有些时候，确定特定的值未包含在列表中很重要；在这种情况下，可使用关键字 not in 。
# 例如，如果有一个列表，其中包含被禁止在论坛上发表评论的用户，就可在允许用户提交评论前检查他是否被禁言：
banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
    print(user.title(),', you can post a response if you wish.')


