# 11.1 　测试函数
# 要学习测试，得有要测试的代码。下面是一个简单的函数，它接受名和姓并返回整洁的姓名：
def get_formatted_name(first, last):
    full_name = first + " " + last
    return full_name.title()

# 函数 get_formatted_name() 将名和姓合并成姓名，在名和姓之间加上一个空格，
# 并将它们的首字母都大写，再返回结果。
# 为核实 get_formatted_name() 像期望的那样工作，
# 我们来编写一个使用这个函数的程序。
# 程序 names.py 让用户输入名和姓，并显示整洁的全名：
print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name:")
    if first == 'q':
        break
    last = input("Please give me a last name;")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first,last)
    print("\tNeatly formatted name: " + formatted_name + ".")




# 下面是一个只包含一个方法的测试用例，它检查函数 get_formatted_name() 在给定名和姓时能否正确地工作：
import unittest
class NameTestCase(unittest.TestCase):  # ①
    '''测试get_formatted_name'''
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis','joplin')   # ②
        self.assertEqual(formatted_name,'Janis Joplin') # ③
unittest.main()




