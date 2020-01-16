# 9-13  使用 OrderedDict ：
# 在练习 6-4 中，你使用了一个标准字典来表示词汇表。
# 请使用 OrderedDict 类来重写这个程序，并确认输出的顺序与你在字典中添加键— 值对的顺序一致。
from collections import OrderedDict

glossary = OrderedDict()

glossary['string'] = 'A series of characters.'
glossary['comment'] = 'A note in a program that the Python interpreter ignores.'
glossary['list'] = 'A collection of items in a particular order.'
glossary['loop'] = 'Work through a collection of items, one at a time.'
glossary['dictionary'] = "A collection of key-value pairs."
glossary['key'] = 'The first item in a key-value pair in a dictionary.'
glossary['value'] = 'An item associated with a key in a dictionary.'
glossary['conditional test'] = 'A comparison between two values.'
glossary['float'] = 'A numerical value with a decimal component.'
glossary['boolean expression'] = 'An expression that evaluates to True or False.'

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)



# 9-14  骰子 ：
# 模块 random 包含以各种方式生成随机数的函数，
# 其中的 randint() 返回一个位于指定范围内的整数，
# 例如，下面的代码返回一个 1~6 内的整数：
'''
from random import randint 
x = randint(1,6)
'''
# 请创建一个 Die 类，它包含一个名为 sides 的属性，该属性的默认值为 6 。
# 编写一个名为 roll_die() 的方法，它打印位于 1 和骰子面数之间的随机数。
# 创建一个 6 面的骰子，再掷 10 次。
# 创建一个 10 面的骰子和一个 20 面的骰子，并将它们都掷 10 次。
from random import randint
class Die():
    '''代表一个可以滚动的模具'''
    def __init__(self, sides = 6):
        '''初始化模具'''
        self.sides = sides
    def roll_die(self):
        '''返回一个数在1和边数之间'''
        return randint(1, self.sides)
# 做6面模具，并显示结果10次
d6 = Die()
results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("\n10 rolls of a 6-sided die.py:")
print(results)

# 做10面模具，并显示结果10次
d10 = Die(sides = 10)
results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sided die.py:")
print(results)

# 做20面模具，并显示结果10次
d10 = Die(sides = 20)
results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 rolls of a 20-sided die.py:")
print(results)