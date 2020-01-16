# 8-15  打印模型 ：
# 将示例 print_models.py (8.4)中的函数放在另一个名为 printing_functions.py 的文件中；
# 在 print_models.py 的开头编写一条 import 语句，并修改这个文件以使用导入的函数。
import printing_functions as pf

unprinted_designs = ['LGD','IG','LFY']
completed_models = []
pf.print_models(unprinted_designs,completed_models)
pf.show_completed_models(completed_models)


# 8-16  导入 ：选择一个你编写的且只包含一个函数的程序，并将这个函数放在另一个文件中。
# 在主程序文件中，使用下述各种方法导入这个函数，再调用它
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *