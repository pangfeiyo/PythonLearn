# 9.4 　导入类
# 随着你不断地给类添加功能，文件可能变得很长，即便你妥善地使用了继承亦如此。
# 为遵循 Python 的总体理念，应让文件尽可能整洁。
# 为在这方面提供帮助， Python 允许你将类存储在模块中，然后在主程序中导入所需的模块。

# 9.4.1 　导入单个类
# 下面来创建一个只包含 Car 类的模块。
# 这让我们面临一个微妙的命名问题：
# 在本章中，已经有一个名为 car.py 的文件，但这个模块也应命名为 car.py ，因为它包含表示汽车的代码。
# 我们将这样解决这个命名问题：
# 将 Car 类存储在一个名为 car.py 的模块中，该模块将覆盖前面使用的文件 car.py 。
# 从现在开始，使用该模块的程序都必须使用更具体的文件名，如 my_car.py 。下面是模块 car.py ，其中只包含 Car 类的代码：

'''导入单个类'''
''' 导入同文件夹下的car.py '''
from car import Car
my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()



'''9.4.2 　在一个模块中存储多个类
虽然同一个模块中的类之间应存在某种相关性，但可根据需要在一个模块中存储任意数量的类。
类 Battery 和 ElectricCar 都可帮助模拟汽车，因此下面将它们都加入模块car.py 中
'''
# 导入 ElectricCar 类，并创建一辆电动汽车了：
from car import ElectricCar
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()



'''
9.4.3 　从一个模块中导入多个类
可根据需要在程序文件中导入任意数量的类。如果我们要在同一个程序中创建普通汽车和电动汽车，就需要将 Car 和 ElectricCar 类都导入：
'''
from car import Car, ElectricCar
my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())



'''
9.4.4 　导入整个模块
你还可以导入整个模块，再使用句点表示法访问需要的类。
这种导入方法很简单，代码也易于阅读。
由于创建类实例的代码都包含模块名，因此不会与当前文件使用的任何名称发生冲突。
下面的代码导入整个 car 模块，并创建一辆普通汽车和一辆电动汽车：
'''
import car
my_beetle = car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())



'''
9.4.5 　导入模块中的所有类
要导入模块中的每个类，可使用下面的语法：
'''
from module_name import *
# 不推荐使用这种导入方式，其原因有二。
# 首先，如果只要看一下文件开头的 import 语句，就能清楚地知道程序使用了哪些类，将大有裨益；
# 但这种导入方式没有明确地指出你使用了模块中的哪些类。这种导入方式还可能引发名称方面的困惑。
# 如果你不小心导入了一个与程序文件中其他东西同名的类，将引发难以诊断的错误。
# 这里之所以介绍这种导入方式，是因为虽然不推荐使用这种方式，但你可能会在别人编写的代码中见到它。
# 需要从一个模块中导入很多类时，最好导入整个模块，并使用 module_name.class_name  语法来访问类。
# 这样做时，虽然文件开头并没有列出用到的所有类，但你清楚地知道在程序的哪些地方使用了导入的模块；
# 你还避免了导入模块中的每个类可能引发的名称冲突。



'''
9.4.6 　在一个模块中导入另一个模块
有时候，需要将类分散到多个模块中，以免模块太大，或在同一个模块中存储不相关的类。
将类存储在多个模块中时，你可能会发现一个模块中的类依赖于另一个模块中的类。
在这种情况下，可在前一个模块中导入必要的类。
例如，下面将 Car 类存储在一个模块中，并将 ElectricCar 和 Battery 类存储在另一个模块中。
我们将第二个模块命名为 electric_car.py （这将覆盖前面创建的文件electric_car.py ），
并将 Battery 和 ElectricCar 类复制到这个模块中：
'''
from car import Car
from electric_car import ElectricCar
my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())