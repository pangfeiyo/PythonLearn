# 9-6  冰淇淋小店 ：
# 冰淇淋小店是一种特殊的餐馆。编写一个名为 IceCreamStand 的类，让它继承你为完成练习 9-1 或练习 9-4 而编写的 Restaurant 类。
# 这两个版本的 Restaurant 类都可以，挑选你更喜欢的那个即可。
# 添加一个名为 flavors 的属性，用于存储一个由各种口味的冰淇淋组成的列表。
# 编写一个显示这些冰淇淋的方法。
# 创建一个 IceCreamStand 实例，并调用这个方法。
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)
    def open_restaurant(self):
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)
    def set_number_served(self, number_served):
        self.number_served = number_served
    def increment_number_served(self, additional_served):
        self.number_served += additional_served

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type = 'ice_cream'):
        super().__init__(name, cuisine_type)
        self.flavors=[] # 用于存储一个由各种口味的冰淇淋组成的列表
    # 创建显示这些冰淇淋的方法
    def show_flavors(self):
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor.title())

big_one = IceCreamStand("The Big One")
big_one.flavors = ['vanilla','chocolate','black cherry']
big_one.describe_restaurant()
big_one.show_flavors()


# 9-7  管理员 ：管理员是一种特殊的用户。
# 编写一个名为 Admin 的类，让它继承你为完成练习 9-3 或练习 9-5 而编写的 User 类。
# 添加一个名为 privileges 的属性，用于存储一个由字符串（如 "can add post" 、 "can delete post" 、 "can ban user" 等）组成的列表。
# 编写一个名为 show_privileges() 的方法，它显示管理员的权限。创建一个 Admin 实例，并调用这个方法。
class User:
    '''表示简单的用户配置文件'''
    def __init__(self, first_name, last_name, username, email, location):
        '''初始化用户'''
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0
    
    def describe_user(self):
        '''显示用户信息的摘要'''
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        '''向用户显示个性化的问候语'''
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []

    def show_privileges(self):
        '''显示管理员拥有的特权'''
        print("\nPrivileges:")
        for privilege in self.privileges:
            print("- " + privilege)

eric = Admin('eric','matthes','e_matthes','e_matthes@example.com','alaska')
eric.describe_user()
eric.privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
eric.show_privileges()


# 9-8  权限 ：
# 编写一个名为 Privileges 的类，它只有一个属性 —— privileges ，其中存储了练习 9-7 所说的字符串列表。
# 将方法 show_privileges() 移到这个类中。
# 在 Admin 类中，将一个 Privileges 实例用作其属性。
# 创建一个 Admin 实例，并使用方法 show_privileges() 来显示其权限。
class User():
    """表示简单的用户配置文件"""

    def __init__(self, first_name, last_name, username, email, location):
        """初始化用户"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """显示用户信息的摘要"""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """向用户显示个性化的问候语"""
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        """login_attempts 增量值"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """login_attempts 归0"""
        self.login_attempts = 0


class Admin(User):
    """具有管理员特权的用户"""

    def __init__(self, first_name, last_name, username, email, location):
        """初始化管理员"""
        super().__init__(first_name, last_name, username, email, location)

        # Initialize an empty set of privileges.
        # 初始化一组空的权限   谷歌直翻
        #将一个privileges 实例用作其属性
        self.privileges = Privileges()

class Privileges():
    """存储管理员权限的类"""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("- This user has no privileges.")


eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric.privileges.show_privileges()

print("\nAdding privileges...")
eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
eric.privileges.privileges = eric_privileges
eric.privileges.show_privileges()



# 9-9  电瓶升级 ：
# 在本节最后一个 electric_car.py 版本中，给 Battery 类添加一个名为 upgrade_battery() 的方法。
# 这个方法检查电瓶容量，如果它不是 85 ，就将它设置为 85 。
# 创建一辆电瓶容量为默认值的电动汽车，调用方法 get_range() ，然后对电瓶进行升级，并再次调用 get_range() 。
# 你会看到这辆汽车的续航里程增加了。
class Car:
    '''试图代表一辆汽车的简单尝试'''
    def __init__(self, manufacturer, model, year):
        '''初始化属性来描述一辆汽车'''
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        '''返回一个格式整洁的描述性名称'''
        long_name = str(self.year) + " " + self.manufacturer + " " + self.model
        return long_name.title()
    def read_odometer(self):
        '''打印显示汽车里程'''
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        '''
        将里程表读数设置为给定值
        如果试图将里程表向后滚动，则拒绝更改'''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        '''在里程表读数中加上给定的量'''
        self.odometer_reading += miles

class Battery:
    '''一个简单的尝试，为电动汽车的电池模型'''
    def __init__(self, battery_size = 60):
        '''初始化电池的属性'''
        self.battery_size = battery_size
    def describe_battery(self):
        '''打印一个描述电池大小的语句'''
        print("This car has a " + str(self.battery_size) + "-KWh battery.")
    def get_rane(self):
        '''打印关于电池提供范围的语句'''
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    def upgrade_battery(self):
        '''如果可能的话，升级电池'''
        if self.battery_size == 60:
            self.battery_size = 85
            print("Upgraded the battery to 85 KWh.")
        else:
            print("The battery is already upgraded.")

class ElectricCar(Car):
    '''汽车模型方面，特定于电动汽车'''
    def __init__(self, manufacturer, model, year):
        '''
        初始化父类的属性
        然后初始化电动车特有的属性'''
        super().__init__(manufacturer, model, year)
        self.battery = Battery()

print("\nMake an electric car, and check the battery.")
my_tesla = ElectricCar('tesla','model s',2016)
my_tesla.battery.describe_battery()

print("\nUpgrade the battery, and check it again:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

print("\nTry upgrading the battery a second time.")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
