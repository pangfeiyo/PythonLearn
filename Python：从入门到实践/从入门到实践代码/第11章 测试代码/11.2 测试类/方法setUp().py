# 11.2.4 　方法 setUp()
# 在前面的 test_survey.py 中，
# 我们在每个测试方法中都创建了一个 AnonymousSurvey 实例，并在每个方法中都创建了答案。
# unittest.TestCase 类包含方法 setUp() ，
# 让我们只需创建这些对象一次，并在每个测试方法中使用它们。
# 如果你在 TestCase 类中包含了方法 setUp() ， 
# Python 将先运行它，再运行各个以 test_ 打头的方法。
# 这样，在你编写的每个测试方法中都可使用在方法 setUp() 中创建的对象了。
# 下面使用 setUp() 来创建一个调查对象和一组答案，供方法 test_store_single_response() 和 test_store_three_responses() 使用：
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonysSurvey类的测试"""
    def setUp(self):
        """
        创建一个调查对象和一组答案，供使用的测试方法使用
        """
        question = 'WHat language did you first learn to speak?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English','Spanish','Mandarin']

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
unittest.main()