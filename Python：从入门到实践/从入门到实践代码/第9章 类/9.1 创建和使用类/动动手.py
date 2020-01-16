# 9-1  餐馆 ：创建一个名为 Restaurant 的类，其方法 __init__() 设置两个属性： restaurant_name 和 cuisine_type 。
# 创建一个名为 describe_restaurant() 的方法和一个名为 open_restaurant() 的方法，
# 其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
# 根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。
class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print(msg)
    def open_restaurant(self):
        msg = self.name + " is open. Come on in !"
        print(msg)

restaurant = Restaurant('the mean queen', 'pizza')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2  三家餐馆 ：根据你为完成练习 9-1 而编写的类创建三个实例，并对每个实例调用方法 describe_restaurant() 。
restaurant2 = Restaurant('Quan ju de','Kaoya')
print()
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3 = Restaurant('LanzhouLaMian','miaotiao')
print()
restaurant3.describe_restaurant()
restaurant3.open_restaurant()

restaurant4 = Restaurant('ShaxianXiaoChi','danchaofan')
print()
restaurant4.describe_restaurant()
restaurant4.open_restaurant()


# 9-3  用户 ：创建一个名为 User 的类，其中包含属性 first_name 和 last_name ，还有用户简介通常会存储的其他几个属性。
# 在类 User 中定义一个名为 describe_user() 的方法，它打印用户信息摘要；
# 再定义一个名为 greet_user() 的方法，它向用户发出个性化的问候。
# 创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。
print("\n9-3")
class User():
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        print("\n" + self.first_name, self.last_name)
        print("Username:", self.username)
        print("Email:",self.email)
        print('Location:', self.location)

    def greet_user(self):
        print("Welcome back", self.username , "!")

user = User('eric','matthes','e_matthes','e_matthes@example.com','alaska')
user.describe_user()
user.greet_user()

willie = User('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska')
willie.describe_user()
willie.greet_user()