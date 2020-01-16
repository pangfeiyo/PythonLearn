# 动手试一试
# 9-4  就餐人数 ：
# 在为完成练习 9-1 而编写的程序中，添加一个名为 number_served 的属性，并将其默认值设置为 0 。
# 根据这个类创建一个名为 restaurant 的实例；打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
# 添加一个名为 set_number_served() 的方法，它让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值。
# 添加一个名为 increment_number_served() 的方法，它让你能够将就餐人数递增。
# 调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。
class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print(msg)
    def open_restaurant(self):
        msg = self.name + " is open. Come on in !"
        print(msg)
    def set_number_served(self, number_served):
        self.number_served = number_served
    def increment_number_served(self, additional_served):
        self.number_served += additional_served
        
restaurant = Restaurant('the mean queen', 'pizza')
restaurant.describe_restaurant()

print("Number served:", str(restaurant.number_served))
restaurant.set_number_served(430)
print("Number served:", str(restaurant.number_served))
restaurant.set_number_served(1257)
print("Number served: " + str(restaurant.number_served))
restaurant.increment_number_served(239)
print("Number served: " + str(restaurant.number_served))


# 9-5  尝试登录次数 ：
# 在为完成练习 9-3 而编写的 User 类中，添加一个名为 login_attempts 的属性。
# 编写一个名为 increment_login_attempts() 的方法，它将属性 login_attempts 的值加 1 。
# 再编写一个名为 reset_login_attempts() 的方法，它将属性 login_attempts 的值重置为 0 。
# 根据 User 类创建一个实例，再调用方法 increment_login_attempts() 多次。
# 打印属性 login_attempts 的值，确认它被正确地递增；
# 然后，调用方法 reset_login_attempts() ，并再次打印属性 login_attempts 的值，确认它被重置为 0 。
class User():
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print("\n" + self.first_name, self.last_name)
        print("Username:", self.username)
        print("Email:",self.email)
        print('Location:', self.location)

    def greet_user(self):
        print("Welcome back", self.username , "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

eric = User('eric','matthes','e_matthes','e_matthes@example.com','alaska')
eric.describe_user()
eric.greet_user()

print("\nMaking 3 login attempts...")
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
print(" Login attempts:",eric.login_attempts)

print("\nResetting login attempts...")
eric.reset_login_attempts()
print(" Login attempts:", eric.login_attempts)