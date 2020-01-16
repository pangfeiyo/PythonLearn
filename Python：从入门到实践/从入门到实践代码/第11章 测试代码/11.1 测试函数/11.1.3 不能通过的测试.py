import unittest
# 11.1.3 　不能通过的测试
# 测试未通过时结果是什么样的呢？我们来修改 get_formatted_name() ，使其能够处理中间名，
# 但这样做时，故意让这个函数无法正确地处理像 Janis Joplin 这样只有名和姓的姓名。
# 下面是函数 get_formatted_name() 的新版本，它要求通过一个实参指定中间名：
def get_formatted_name(first, middle, last):
    full_name = first + " " + middle + " " + last
    return full_name.title()

class NameTestCase(unittest.TestCase):  # ①
    '''测试get_formatted_name'''
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis','joplin')   # ②
        self.assertEqual(formatted_name,'Janis Joplin') # ③
unittest.main()