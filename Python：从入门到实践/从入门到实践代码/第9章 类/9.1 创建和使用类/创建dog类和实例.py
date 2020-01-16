# 使用类几乎可以模拟任何东西。下面来编写一个表示小狗的简单类 Dog —— 它表示的不是特定的小狗，而是任何小狗。
# 对于大多数宠物狗，我们都知道些什么呢？它们都有名字和年龄；
# 我们还知道，大多数小狗还会蹲下和打滚。
# 由于大多数小狗都具备上述两项信息（名字和年龄）和两种行为（蹲下和打滚），我们的 Dog 类将包含它们。
# 这个类让Python 知道如何创建表示小狗的对象。编写这个类后，我们将使用它来创建表示特定小狗的实例。

# 9.1.1 　创建 Dog  类
# 根据 Dog 类创建的每个实例都将存储名字和年龄。我们赋予了每条小狗蹲下（ sit() ）和打滚（ roll_over() ）的能力：
class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self, name, age):
        """初始化属性name 和 age """
        self.name = name
        self.age = age

    def sit(self):
        # 模拟小狗被命令时蹲下
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        # 模拟小狗被命令时打滚
        print(self.name.title() + " rolled over!.")



# 9.1.2 　根据类创建实例
# 可将类视为有关如何创建实例的说明。 Dog 类是一系列说明，让 Python 知道如何创建表示特定小狗的实例。
# 下面来创建一个表示特定小狗的实例
my_dog = Dog('willie',6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
# 调用方法
my_dog.sit()
my_dog.roll_over()


# 3.创建多个实例
your_dog = Dog('lucy',3)
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
your_dog.roll_over()