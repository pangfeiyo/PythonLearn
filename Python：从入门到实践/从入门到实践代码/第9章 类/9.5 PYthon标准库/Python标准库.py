"""
9.5 　 Python 标准库
Python 标准库 是一组模块，安装的 Python 都包含它。你现在对类的工作原理已有大致的了解，可以开始使用其他程序员编写好的模块了。
可使用标准库中的任何函数和类，为此只需在程序开头包含一条简单的 import 语句。
下面来看模块 collections 中的一个类 —— OrderedDict 。
字典让你能够将信息关联起来，但它们不记录你添加键 — 值对的顺序。
要创建字典并记录其中的键 — 值对的添加顺序，可使用模块 collections 中的 OrderedDict类。 
OrderedDict 实例的行为几乎与字典相同，区别只在于记录了键 — 值对的添加顺序。
我们再来看一看第 6 章的 favorite_languages.py 示例，但这次将记录被调查者参与调查的顺序：
"""
from collections import OrderedDict # ❶
favorite_languages = OrderedDict()  # ❷

favorite_languages['jen'] = 'python'    # ❸
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():   # ❹
    print(name.title() + "'s favorite language is " + language.title() + ".")

'''
我们首先从模块 collections 中导入了 OrderedDict 类（见❶）。
在❷处，我们创建了 OrderedDict 类的一个实例，并将其存储到 favorite_languages 中。
请注意，这里没有使用花括号，而是调用 OrderedDict() 来创建一个空的有序字典，并将其存储在 favorite_languages 中。
接下来，我们以每次一对的方式添加名字 — 语言对。
在❹处，我们遍历 favorite_languages ，但知道将以添加的顺序获取调查结果
'''
'''
这是一个很不错的类，它兼具列表和字典的主要优点（在将信息关联起来的同时保留原来的顺序）。
等你开始对关心的现实情形建模时，可能会发现有序字典正好能够满足需求。
随着你对标准库的了解越来越深入，将熟悉大量可帮助你处理常见情形的模块。
注意 　你还可以从其他地方下载外部模块。本书第二部分的每个项目都需要使用外部模块，届时你将看到很多这样的示例。
'''


'''
9-15 Python Module of the Week  ：
要了解 Python 标准库，一个很不错的资源是网站 Python Module of the Week 。
请访问 http://pymotw.com/  并查看其中的目录，在其中找一个你感兴趣的模块进行探索，或阅读模块 collections 和 random 的文档。
'''