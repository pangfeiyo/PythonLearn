# 9-10  导入 Restaurant 类 ：
# 将最新的 Restaurant 类存储在一个模块中。
# 在另一个文件中，导入 Restaurant 类，创建一个 Restaurant 实例，并调用 Restaurant 的一个方法，以确认 import 语句正确无误。
from dongdongshou import Restaurant
channel_club = Restaurant("the channel culb",'steak and seafood')
channel_club.describe_restaurant()
channel_club.open_restaurant()


# 9-11  导入 Admin 类 ：
# 以为完成练习 9-8 而做的工作为基础，
# 将 User 、 Privileges 和 Admin 类存储在一个模块中，
# 再创建一个文件，在其中创建一个 Admin 实例
# 并对其调用方法 show_privileges() ，以确认一切都能正确地运行。
from dongdongshou import Admin
eric = Admin('eric','matthes','e_matthes','e_matthes@example.com','alaska')
eric.describe_user()

eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
eric.privileges.privileges = eric_privileges

print("\nThe admin " + eric.username + " has these privileges: ")
eric.privileges.show_privileges()

# 9-12  多个模块 ：
# 将 User 类存储在一个模块中，并将 Privileges 和 Admin 类存储在另一个模块中。
# 再创建一个文件，在其中创建一个 Admin 实例，
# 并对其调用方法 show_privileges() ，以确认一切都依然能够正确地运行。
from dongshou_admin import Admin
eric = Admin('eric233', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
eric.privileges.privileges = eric_privileges

print("\nThe admin " + eric.username + " has these privileges: ")
eric.privileges.show_privileges()