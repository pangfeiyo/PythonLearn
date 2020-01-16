# 有时候，你预先不知道函数需要接受多少个实参，好在 Python 允许函数从调用语句中收集任意数量的实参。
# 例如，来看一个制作比萨的函数，它需要接受很多配料，但你无法预先确定顾客要多少种配料。
# 下面的函数只有一个形参 *toppings ，但不管调用语句提供了多少实参，这个形参都将它们统统收入囊中：
def make_pizza(*toppings):
    '''打印顾客点的所有配料'''
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
# 形参名 *toppings 中的星号让 Python 创建一个名为 toppings 的空元组，并将收到的所有值都封装到这个元组中。
# 函数体内的 print 语句通过生成输出来证明 Python 能够处理使用一个值调用函数的情形，也能处理使用三个值来调用函数的情形。
# 它以类似的方式处理不同的调用，注意， Python 将实参封装到一个元组中，即便函数只收到一个值也如此

# 现在，我们可以将这条 print 语句替换为一个循环，对配料列表进行遍历，并对顾客点的比萨进行描述：
def make_pizza(*toppings):
    '''概述要制作的比萨'''
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print('- ' + topping)
make_pizza('pepperoni')
make_pizza('mushromms','green peppers','extra cheese')
# 不管函数收到的实参是多少个，这种语法都管用。


# 8.5.1 　结合使用位置实参和任意数量实参
# 如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。
# Python 先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。
# 例如，如果前面的函数还需要一个表示比萨尺寸的实参，必须将该形参放在形参 *toppings 的前面：
def make_pizza(size, *toppings):
    """ 概述要制作的比萨 """
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# 基于上述函数定义， Python 将收到的第一个值存储在形参 size 中，并将其他的所有值都存储在元组 toppings 中。
# 在函数调用中，首先指定表示比萨尺寸的实参，然后根据需要指定任意数量的配料。
# 现在，每个比萨都有了尺寸和一系列配料，这些信息按正确的顺序打印出来了 —— 首先是尺寸，然后是配料



# 8.5.2 　使用任意数量的关键字实参
# 有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。
# 在这种情况下，可将函数编写成能够接受任意数量的键 — 值对 —— 调用语句提供了多少就接受多少。
# 一个这样的示例是创建用户简介：你知道你将收到有关用户的信息，但不确定会是什么样的信息。
# 在下面的示例中，函数 build_profile() 接受名和姓，同时还接受任意数量的关键字实参：
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert','einstein',
                             location = 'princeton',
                             field = 'physlcs')
print(user_profile)
