import unittest
from survey import AnonymousSurvey

# 11.2.3 　测试 AnonymousSurvey  类
# 下面来编写一个测试，对 AnonymousSurvey 类的行为的一个方面进行验证：
# 如果用户面对调查问题时只提供了一个答案，这个答案也能被妥善地存储。
# 为此，我们将在这个答案被存储后，使用方法 assertIn() 来核实它包含在答案列表中：

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的调试"""
    def test_store_single_response(self):
        """调试单个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)

    # 这很好，但只能收集一个答案的调查用途不大。
    # 下面来核实用户提供三个答案时，它们也将被妥善地存储。
    # 为此，我们在 TestAnonymousSurvey 中再添加一个方法：
    def test_store_three_responses(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English','Spanish','Mandarin']
        for response in responses:
            my_survey.store_response(response)
        
        for response in responses:
            # assertIn 核实前者在后者中
            self.assertIn(response, my_survey.responses)
unittest.main()