import unittest
# 11.1.5 　添加新测试
# 确定 get_formatted_name() 又能正确地处理简单的姓名后，我们再编写一个测试，
# 用于测试包含中间名的姓名。为此，我们在 NamesTestCase 类中再添加一个方法：
def get_formatted_name(first, last, middle=""):
    if middle:
        full_name = first + " " + middle + " " + last
    else:
        full_name = first + " " + last
    return full_name.title()

class NameTestCase(unittest.TestCase):  # ①
    '''测试get_formatted_name'''
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis','joplin')   # ②
        self.assertEqual(formatted_name,'Janis Joplin') # ③

    def test_first_last_middle_name(self):
        """能够正确处理像Wolfgang Amadeus Mozart这样的姓名吗？"""
        formatted_name = get_formatted_name(
            'wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')

unittest.main()