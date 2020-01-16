# 【扩展阅读】EasyGui 学习文档

# 一个简单的例子
import easygui as g
import sys
# import sys
#
# while 1:
#     g.msgbox("嗨，欢迎进入第一个界面小游戏^_^")
#
#     msg = "请问你希望在鱼C工作室学习到什么知识呢？"
#     title = "小游戏互动"
#     choices = ["谈恋爱", "编程", "OOXX", "琴棋书画"]
#
#     choice = g.choicebox(msg, title, choices)
#
#     # note that we convert choice to string, in case  注意，我们将选择转换为字符串，以防万一
#     # the user cancelled the choice, and we got None. 用户取消了选择，我们没有
#     g.msgbox("你的选择是: " + str(choice), "结果")
#
#     msg = "你希望重新开始小游戏吗？"
#     title = "请选择"
#
#     if g.ccbox(msg, title):  # show a Continue/Cancel dialog  显示继续 / 取消对话框
#         pass  # user chose Continue  用户选择继续
#     else:
#         sys.exit(0)  # user chose Cancel  用户选择取消



# EasyGui 的各种功能演示
# g.egdemo()



# 使用 EasyGui
# 两个参数，第一个是消息，第二个是标题
# g.msgbox("Hello,world","FishC")

# g.ccbox("选择哪一个")
# if ccbox():
#     pass    # 用户选择继续
# else:
#     return  #用户选择结束


# 7.使用关键字参数调用easygui的函数
# 假设使用一个按键组件（三个参数：内容、标题、选项），不想指定标题参数（第二个参数）
# choices = ['愿意', '不愿意', '有钱的时候愿意']
# reply = g.choicebox('你愿意购买资源打包支持小甲鱼吗？', choices = choices)


# 8.使用按钮组件
# 8.1 msgbox()
# msgbox(msg = '(Your message goes here)', title = '', ok_button = 'OK', image = None, root = None)
# msgbox()显示一个消息和提供一个"OK"按键，可以指定任意消息和标题，以及更改"ok"的内容
'''
实例函数：
def msgbox(msg = '(Your message goes here)', title = '', ok_button = 'OK'):
'''
# 重写OK
# g.msgbox("鱼C", ok_button="论坛")

# 8.2 ccbox()
'''
ccbox(msg='Shall i continue?', title='', choices=('Continue,','Cancel'), image=None) 
ccbox()提示一个选择：continue或cancel，并相应的返回1（选择continue）或者0（选择cancel）
注意：ccbox()是返回整型的1或0，不是布尔类型的True或False。但你仍然可以这么写 '''
# if g.ccbox("再来一次", choices=("要","不要")):
#     g.msgbox("算了")
# else:
#     sys.exit(0)

# 8.3 ynbox()
# ynbox(msg-'shall i continue?', title='', choices=('yes','no'), image=None)

# 8.4 buttonbox()
'''
buttonbox(msg='', title='', choices=('button1','button2','button3'), image=None, root=None)
当用户点击任意一个按钮时，返回按钮的文本内容。如果用户取消取消或关闭窗口，那么返回默认选项（第一个）'''
# choices=['1','2','3']
# g.buttonbox("buttonbox",choices= choices)

# 8.5 indexbox()
# indexbox(msg='shall i continue?', title='', choices=('yes','no'), image=None)
# 基本和上边一样，区别是当用户选择第一个按钮时返回序号0，选择第二个按钮的时候返回序号1

# 8.6 boolbox()
'''boolbox(msg='shall', title='', choices=('yes','no'), image=Nono)
如果选择第一个按钮返回1 ，否则返回0'''

# 9.如何在buttonbox里选择图片
# 这里仅支持.gif格式
g.buttonbox('这是个buttonbox',image='123.gif')