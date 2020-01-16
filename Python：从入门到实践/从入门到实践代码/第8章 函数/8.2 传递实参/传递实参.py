# 8.2 　传递实参
# 鉴于函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参。
# 向函数传递实参的方式很多，可使用 位置实参 ，这要求实参的顺序与形参的顺序相同；
# 也可使用 关键字实参 ，其中每个实参都由变量名和值组成；还可使用列表和字典。
# 下面来依次介绍这些方式。

# 8.2.1 　位置实参
# 你调用函数时， Python 必须将函数调用中的每个实参都关联到函数定义中的一个形参。为此，最简单的关联方式是基于实参的顺序。
# 这种关联方式被称为 位置实参 。为明白其中的工作原理，来看一个显示宠物信息的函数。
# 这个函数指出一个宠物属于哪种动物以及它叫什么名字，如下所示：
def describe_pet(animal_type, pet_name):
    '''显示宠物信息'''
    print("I have a", animal_type.title())
    print("Its name is", pet_name.title())
describe_pet('hamster','harry')
print("……")
# 1.  调用函数多次
# 你可以根据需要调用函数任意次。要再描述一个宠物，只需再次调用 describe_pet() 即可：
def describe_pet(animal_type, pet_name):
    '''显示宠物信息'''
    print("I have a", animal_type.title())
    print("Its name is", pet_name.title())
describe_pet('hamster','harry')
describe_pet('dog','willie')
print("……")

# 8.2.2 　关键字实参
# 关键字实参 是传递给函数的名称 — 值对。
# 你直接在实参中将名称和值关联起来了，因此向函数传递实参时不会混淆（不会得到名为 Hamster 的 harry 这样的结果）。
# 关键字实参让你无需考虑函数调用中的实参顺序，还清楚地指出了函数调用中各个值的用途。
# 下面来重新编写 pets.py ，在其中使用关键字实参来调用 describe_pet() ：
def describe_pet(animal_type, pet_name):
    '''显示宠物信息'''
    print("I have a", animal_type.title())
    print("Its name is", pet_name.title())
describe_pet(animal_type='Hamster',pet_name='harry')
print("……")

# 8.2.3 　默认值
# 编写函数时，可给每个形参指定 默认值 。在调用函数中给形参提供了实参时， Python 将使用指定的实参值；
# 否则，将使用形参的默认值。因此，给形参指定默认值后，可在函数调用中省略相应的实参。
# 使用默认值可简化函数调用，还可清楚地指出函数的典型用法。
# 例如，如果你发现调用 describe_pet() 时，描述的大都是小狗，就可将形参 animal_type 的默认值设置为 'dog' 。
# 这样，调用 describe_pet() 来描述小狗时，就可不提供这种信息：
def describe_pet(pet_name, animal_type = 'dog'):
    '''显示宠物信息'''
    print("I have a", animal_type.title())
    print("Its name is", pet_name.title())
# describe_pet(pet_name='willie')
describe_pet('willie')
print("……")
# 注意 　使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的实参。这让 Python 依然能够正确地解读位置实参。


# 8.2.4 　等效的函数调用
# 鉴于可混合使用位置实参、关键字实参和默认值，通常有多种等效的函数调用方式。
# 请看下面的函数 describe_pets() 的定义，其中给一个形参提供了默认值：
def describe_pet(pet_name, animal_type = 'dog'):
    '''显示宠物信息'''
    print("I have a", animal_type.title())
    print("Its name is", pet_name.title())
# 基于这种定义，在任何情况下都必须给pet_name提供实参；指定该实参时可以使用位置方式，也可以使用关键字方式。
# 如果要描述的动物不是小狗，还必须在函数调用中给animal_type提供实参；同样，指定该实参时可以使用位置方式，也可以使用关键字方式。
# 下面对这个函数的所有调用都可行：
print("一条名为Willie的小狗")
describe_pet('willie')
describe_pet(pet_name='Willie')
print("一只名为Harry的仓鼠")
describe_pet('Harry','hamster')
describe_pet(pet_name='Harry',animal_type='hamster')
describe_pet(animal_type='hamster',pet_name='Harry')
# 这些函数调用的输出与前面的示例相同。
# 注意 　使用哪种调用方式无关紧要，只要函数调用能生成你希望的输出就行。使用对你来说最容易理解的调用方式即可。


# 8.2.5 　避免实参错误
# 等你开始使用函数后，如果遇到实参不匹配错误，不要大惊小怪。
# 你提供的实参多于或少于函数完成其工作所需的信息时，将出现实参不匹配错误。
# 例如，如果调用函数 describe_pet() 时没有指定任何实参，结果将如何呢？
