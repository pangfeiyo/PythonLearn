# 动手试一试
# 11-3  雇员 ：
# 编写一个名为 Employee 的类，其方法 __init__() 接受名、姓和年薪，并将它们都存储在属性中。
# 编写一个名为 give_raise() 的方法，它默认将年薪增加 5000 美元，但也能够接受其他的年薪增加量。
# 为 Employee 编写一个测试用例，其中包含两个测试方法： 
# test_give_default_raise() 和 test_give_custom_raise() 。
# 使用方法 setUp() ，以免在每个测试方法中都创建新的雇员实例。
# 运行这个测试用例，确认两个测试都通过了。
class Employee:
    def __init__(self, f_name, l_name, salary):
        self.f_name = f_name.title()
        self.l_name = l_name.title()
        self.salary = salary

    def give_raise(self, amount = 5000):
        self.salary += amount



# 编写测试用例
import unittest

class TestEmployee(unittest.TestCase):
    """对模块员工的测试"""
    def setUp(self):
        """使员工在测试中使用"""
        self.eric = Employee('eric','matthes',65000)

    def test_give_default_raise(self):
        """测试默认的年薪是正确的"""
        self.eric.give_raise()
        self.assertEqual(self.eric.salary, 70000)

    def test_give_custom_raise(self):
        """测试自定义提升年薪是正确"""
        self.eric.give_raise(10000)
        self.assertEqual(self.eric.salary, 75000)

unittest.main()