# 8.6.1 　导入整个模块
# 要让函数是可导入的，得先创建模块。
# 模块 是扩展名为 .py 的文件，包含要导入到程序中的代码。
# 下面来创建一个包含函数 make_pizza() 的模块。
# 为此，我们将文件 pizza.py 中除函数 make_pizza() 之外的其他代码都删除：
import pizza

pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')



# 8.6.2 　导入特定的函数
# 你还可以导入模块中的特定函数，这种导入方法的语法如下：
# from module_name import function_name
# 通过用逗号分隔函数名，可根据需要从模块中导入任意数量的函数：
# from module_name import function_0, function_1, function_2
# 对于前面的 making_pizzas.py 示例，如果只想导入要使用的函数，代码将类似于下面这样：
print("\n-- 导入特定函数 --")
from pizza import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 8.6.3 　使用 as  给函数指定别名
print("\n-- 使用 as --")
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')


# 8.6.4 　使用 as  给模块指定别名
# import pizza as p
# p.make_pizza(16,'pepperoni')
# p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 8.6.5 　导入模块中的所有函数
# from pizza import *
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')