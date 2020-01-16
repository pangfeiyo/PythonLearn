# exception 异常
# # file_name = input("请输入需要打开的文件名：")
# file_name = 'record.txt'
# f = open(file_name)
# print("文件的内容是：")
# for each_line in f:
#     print(each_line,end="")


my_list = ['小甲鱼']
# 断言 assert  ， 当后面条件为假时，程序自动崩溃并抛出AssertionError
assert len(my_list) > 0
# # 报错 AssertionError
# my_list2 = []
# assert len(my_list2) > 0

# # 不存在的方法
# 报错 AttributeError: 'list' object has no attribute 'fishc'
# my_list.fishc

# # 超出索引 IndexError: list index out of range
# my_list3 = [1,2,3]
# print(my_list3[3])

# # 字典中找不到关键字 KeyError: 'four'
# my_dict = {'one':1, 'two':2, 'three':3}
# print(my_dict['one'])   # 正常
# print(my_dict['four'])  # 错误

# # 尝试访问一个不存在的变量 NameError: name 'oo' is not defined
# print(oo)

# # 操作系统产生的异常（例如打开的文件不存在）   OSError
# # FileNotFoundError: [Errno 2] No such file or directory: 'text11'
# f = open('text11')

# # 语法错误  SyntaxError: Missing parentheses in call to 'print'
# print 'I love fishc'    # 这是python 2.x 的语法

# # 不同类型间的错误操作
# # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(1 + "1")

# # 除数为零    ZeroDivisionError: division by zero
print(5 / 0)