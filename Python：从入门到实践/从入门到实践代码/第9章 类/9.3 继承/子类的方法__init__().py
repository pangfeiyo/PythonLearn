# 9.3 　继承
# 编写类时，并非总是要从空白开始。如果你要编写的类是另一个现成类的特殊版本，可使用 继承 。
# 一个类 继承 另一个类时，它将自动获得另一个类的所有属性和方法；
# 原有的类称为 父类 ，而新类称为 子类 。子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。


# 9.3.1 　子类的方法 __init__()
# 创建子类的实例时， Python 首先需要完成的任务是给父类的所有属性赋值。
# 为此，子类的方法 __init__() 需要父类施以援手。
# 例如，下面来模拟电动汽车。
# 电动汽车是一种特殊的汽车，
# 因此我们可以在前面创建的 Car 类的基础上创建新类 ElectricCar ，这样我们就只需为电动汽车特有的属性和行为编写代码。
# 下面来创建一个简单的 ElectricCar 类版本，它具备 Car 类的所有功能：
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    # 电动车的独特之处
    def __init__(self, make, model, year):
        '''初始化父类的属性'''
        # super()函数帮助父类和子类关联起来
        # 这行代码让 Python 调用 ElectricCar 的父类的方法 __init__() ，让 ElectricCar 实例包含父类的所有属性。
        # 父类也称为 超类 （ superclass ），名称 super 因此而得名
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla',"model's",2016)
print(my_tesla.get_descriptive_name())



# 9.3.3 给予类定义属性和方法
# 让一个类继承另一个类后，可添加区分子类和父类所需的新属性和方法。
# 下面来添加一个电动汽车特有的属性（电瓶），以及一个描述该属性的方法。我们将存储电瓶容量，并编写一个打印电瓶描述的方法：
class ElectricCar(Car):
    def __init__(self, make, model, year):
        '''电动汽车的独特之处
        初始化父类的属性，再初始化电动汽车特有的属性  '''
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        # 打印一条描述电瓶容量的消息
        print("This car has a " + str(self.battery_size) + "-KWh battery.")
my_tesla = ElectricCar('tesla-X', "model's", 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

 

# 9.3.4 重写父类的方法
# 可在子类中定义一个这样的方法，即它与要重写的父类方法同名
# 假设 Car 类有一个名为 fill_gas_tank() 的方法，它对全电动汽车来说毫无意义，因此你可能想重写它。下面演示了一种重写方式：
class ElectricCar(Car):
    def __init__(self, make, model, year):
        '''电动汽车的独特之处
        初始化父类的属性，再初始化电动汽车特有的属性  '''
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        # 打印一条描述电瓶容量的消息
        print("This car has a " + str(self.battery_size) + "-KWh battery.")

    # 假设父类中有 fill_gas_tank方法
    def fill_gas_tank():
        # 电动汽车没有油箱
        print("This car doesn't need a gas tank!")



# 9.3.5 将实例用作属性
# 使用代码模拟实物时，你可能会发现自己给类添加的细节越来越多：属性和方法清单以及文件都越来越长。
# 在这种情况下，可能需要将类的一部分作为一个独立的类提取出来。
# 你可以将大型类拆分成多个协同工作的小类。
# 例如，不断给 ElectricCar 类添加细节时，我们可能会发现其中包含很多专门针对汽车电瓶的属性和方法。
# 在这种情况下，我们可将这些属性和方法提取出来，放到另一个名为 Battery 的类中，并将一个 Battery 实例用作 ElectricCar 类的一个属性
class Battery():
    # 一次模拟电动汽车电瓶的简单尝试
    def __init__(self, battery_size = 70):
        # 初始化电瓶的属性
        self.battery_size = battery_size

    def describe_battery(self):
        # 打印一条描述电瓶容量的消息
        print("This car has a " + str(self.battery_size) + "-KWh battery.")

    def get_range(self):
        # 打印一条消息，指出电瓶的续航里程
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    '''电动汽车的独特之处'''
    def __init__(self, make, model, year):
        ''' 初始化父类的属性，再初始化电动汽车特有的属性  '''
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar("tesla-Max", "model's",2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
