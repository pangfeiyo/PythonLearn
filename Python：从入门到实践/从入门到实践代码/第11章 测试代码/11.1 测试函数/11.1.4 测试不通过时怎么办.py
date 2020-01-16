import unittest
# 11.1.4 　测试未通过时怎么办
# 测试未通过时怎么办呢？如果你检查的条件没错，测试通过了意味着函数的行为是对的，
# 而测试未通过意味着你编写的新代码有错。
# 因此，测试未通过时，不要修改测试，而应修复导致测试不能通过的代码：
# 检查刚对函数所做的修改，找出导致函数行为不符合预期的修改。
# 在这个示例中， get_formatted_name() 以前只需要两个实参 —— 名和姓，
# 但现在它要求提供名、中间名和姓。
# 新增的中间名参数是必不可少的，这导致 get_formatted_name() 的行为不符合预期。
# 就这里而言，最佳的选择是让中间名变为可选的。
# 这样做后，使用类似于 Janis Joplin 的姓名进行测试时，测试就会通过了，同时这个函数还能接受中间名。
# 下面来修改 get_formatted_name() ，将中间名设置为可选的，然后再次运行这个测试用例。
# 如果通过了，我们接着确认这个函数能够妥善地处理中间名。
# 要将中间名设置为可选的，可在函数定义中将形参 middle 移到形参列表末尾，并将其默认值指定为一个空字符串。
# 我们还要添加一个 if 测试，以便根据是否提供了中间名相应地创建姓名：

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
unittest.main()