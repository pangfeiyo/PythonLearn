# 9.2 　使用类和实例
# 你可以使用类来模拟现实世界中的很多情景。类编写好后，你的大部分时间都将花在使用根据类创建的实例上。
# 你需要执行的一个重要任务是修改实例的属性。你可以直接修改实例的属性，也可以编写方法以特定的方式进行修改。

# 9.2.1 　 Car  类
# 下面来编写一个表示汽车的类，它存储了有关汽车的信息，还有一个汇总这些信息的方法：
class Car():
    # 一次模拟汽车的简单尝试
    def __init__(self, make, model, year):
        # 初始化描述汽车的属性
        self.make = make
        self.model = model 
        self.year = year

    def get_descriptive_name(self):
        # 返回整洁的描述信息
        long_name = str(self.year) + " "+ self.make + " " +self.model
        return long_name

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())


# 9.2.2 给属性指定默认值 
# 类中的每个属性都必须有初始值，哪怕这个值是 0 或空字符串。
# 在有些情况下，如设置默认值时，在方法 __init__() 内指定这种初始值是可行的；
# 如果你对某个属性这样做了，就无需包含为它提供初始值的形参。
# 下面来添加一个名为 odometer_reading 的属性，其初始值总是为 0 。
# 我们还添加了一个名为 read_odometer() 的方法，用于读取汽车的里程表：
class Car():
    def __init__(self, make, model, year):
        # 初始化描述汽车的属性
        self.make = make
        self.model = model 
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptiove_name(self):
        pass

    def read_odometer(self):
        # 打印一条指出汽车里程的消息
        print("This car has " + str(self.odometer_reading) + " miles on it.")

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptiove_name())
my_new_car.read_odometer()


# 9.2.3 修改属性的值 
# 可以以三种不同的方式修改属性的值：
# 直接通过实例进行修改；  通过方法进行设置；  通过方法进行递增（增加特定的值）。
# 下面依次介绍这些方法。
# 1.  直接修改属性的值
# 要修改属性的值，最简单的方式是通过实例直接访问它。下面的代码直接将里程表读数设置为 23 ：
print("\n修改属性的值：")
print("方法一：")
my_new_car.odometer_reading = 123
my_new_car.read_odometer()

# 有时候需要像这样直接访问属性，但其他时候需要编写对属性进行更新的方法。
# 2.  通过方法修改属性的值
# 如果有替你更新属性的方法，将大有裨益。这样，你就无需直接访问属性，而可将值传递给一个方法，由它在内部进行更新。
# 下面的示例演示了一个名为 update_odometer() 的方法：
class Car():
    def __init__(self, make, model, year):
        # 初始化描述汽车的属性
        self.make = make
        self.model = model 
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptiove_name(self):
        long_name = str(self.year) + " "+ self.make + " " +self.model
        return long_name

    def read_odometer(self):
        # 打印一条指出汽车里程的消息
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        # 将里程表读数设置为指定的值
        # self.odometer_reading = mileage
        
        # 可对方法 update_odometer() 进行扩展，使其在修改里程表读数时做些额外的工作。
        # 下面来添加一些逻辑，禁止任何人将里程表读数往回调：
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer!")

print("\n方法二")
my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptiove_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()


# 3.  通过方法对属性的值进行递增
# 有时候需要将属性值递增特定的量，而不是将其设置为全新的值。
# 假设我们购买了一辆二手车，且从购买到登记期间增加了 100 英里的里程，
# 下面的方法让我们能够传递这个增量，并相应地增加里程表读数：
class Car():
    def __init__(self, make, model, year):
        # 初始化描述汽车的属性
        self.make = make
        self.model = model 
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptiove_name(self):
        long_name = str(self.year) + " "+ self.make + " " +self.model
        return long_name

    def read_odometer(self):
        # 打印一条指出汽车里程的消息
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        # 将里程表读数设置为指定的值
        # self.odometer_reading = mileage
        
        # 可对方法 update_odometer() 进行扩展，使其在修改里程表读数时做些额外的工作。
        # 下面来添加一些逻辑，禁止任何人将里程表读数往回调：
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer!")

    def increment_odometer(self, miles):
        # 将里程表读数增加指定的量
        self.odometer_reading += miles

print("\n方法三：")
my_user_car = Car('subaru','outback',2013)
print(my_new_car.get_descriptiove_name())

my_user_car.update_odometer(23500)
my_user_car.read_odometer()

my_user_car.increment_odometer(100)
my_user_car.read_odometer()