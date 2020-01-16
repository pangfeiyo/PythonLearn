# 11.2.1 　各种断言方法
# Python 在 unittest.TestCase 类中提供了很多断言方法。
# 前面说过，断言方法检查你认为应该满足的条件是否确实满足。
# 如果该条件确实满足，你对程序行为的假设就得到了确认，你就可以确信其中没有错误。
# 如果你认为应该满足的条件实际上并不满足， Python 将引发异常。
# 表 11-1 描述了 6 个常用的断言方法。
# 使用这些方法可核实返回的值等于或不等于预期的值、返回的值为 True 或 False 、返回的值在列表中或不在列表中。
# 你只能在继承 unittest.TestCase 的类中使用这些方法，下面来看看如何在测试类时使用其中的一个。
'''
表 11-1 　 unittest Module 中的断言方法
    方法                           用途
assertEqual(a, b)               核实a == b
assertNotEqual(a, b)            核实a != b
assertTrue(x)                   核实x 为True
assertFalse(x)                  核实x 为False
assertIn(item , list )          核实 item 在 list 中
assertNotIn(item , list )       核实 item 不在 list 中
'''



# 11.2.2 　一个要测试的类
# 类的测试与函数的测试相似 —— 你所做的大部分工作都是测试类中方法的行为，
# 但存在一些不同之处，下面来编写一个类进行测试。来看一个帮助管理匿名调查的类：
class AnonymousSurvey():
    '''收集茂名调查问卷的答案'''
    def __init__(self, question):
        """ 存储一个问题，并为存储答案做准备 """
        self.question = question
        self.responses = []
    def show_question(self):
        """ 显示调查问卷 """
        print(question)
    def store_response(self, new_response):
        """ 存储单份调查答卷 """
        self.responses.append(new_response)
    def show_results(self):
        """ 显示收集到的所有答卷 """
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)


# 为证明 AnonymousSurvey 类能够正确地工作，我们来编写一个使用它的程序：
# 定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# 显示问题并存储答案
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

#  显示调查结果
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()






