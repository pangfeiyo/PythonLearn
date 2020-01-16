# 0.给猜数小游戏加上界面
import random
import easygui as g

# g.msgbox("欢迎进入第一个界面小游戏")
# secret = random.randint(1,10)
#
# msg = "猜一下现在在想什么数字（1~10）："
# title = "数字小游戏"
# # integerbox() 为用户提供一个简单的输入框，用户只能输入范围内（lowerbround参数设置最小值，upperbound设置最大值）的整型参数，否则会要求用户重新输入
# guess = g.integerbox(msg, title, lowerbound=1, upperbound=10)
#
# while True:
#     if guess == secret:
#         g.msgbox("猜对了")
#         break
#     else:
#         if guess > secret:
#             g.msgbox("大了")
#         else:
#             g.msgbox("小了")
#         guess = g.integerbox(msg, title, lowerbound=1, upperbound=10)
# g.msgbox("游戏结束")


# 1.实现一个用于登记用户账号信息的界面（带*是必填，要求一定要有输入并且不能是空格）
# msg = "请填写以下联系方式"
# title = "账号中心"
# fieldNames = [' *用户名',' *真实姓名',' 固定电话',' *手机号码',' QQ',' E-mail']
# fieldValues = []
# fieldValues = g.multenterbox(msg, title, fieldNames)
#
# while 1:
#     if fieldValues == None:
#         break
#     errmsg = ""
#     for i in range(len(fieldNames)):
#         option = fieldNames[i].strip()  # strip() 移除字符串头尾指定的字符（默认空格）
#         if fieldValues[i].strip() =="" and option[0] == "*":
#             errmsg += ('[%s]为必填项。\n\n' % fieldNames[i])
#     if errmsg == "":
#         break
#     fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues)
# print("用户资料如下：%s" % str(fieldValues))


# 2.提供一个文件夹浏览框，让用户选择需要打开的文本文件，打开并显示文件内容
import os
#file_path = g.fileopenbox(default="*.txt")
#with open(file_path) as f:
#    # os.path.basename() 去掉目录路径，单独返回文件名
#    title = os.path.basename(file_path)
#    msg = '文件[%s]的内容如下：' % title
#    text = f.read()
#    g.textbox(msg, title, text)


# 3.在上一题的基础上增强功能：当用户点击“OK”的时候，比较当前文件是否修改过，
# 如果修改过，则提示“覆盖保存”、“放弃保存”或“另存为...”并实现相应功能
# 过程中会出现一个小问题
# easygui.textbox函数会在返回的字符串后边追加一个行结束符（"\n"），因此在比较字符串是否发生改变的时候需要人工将这个行结束符忽略
#file_path = g.fileopenbox(default="*.txt")

#with open(file_path) as old_file:
#    title = os.path.basename(file_path)
#    msg = "文件【%s】的内容如下：" % title
#    text = old_file.read()
#    text_after = g.textbox(msg, title, text)
    
#if text != text_after[:-1]:
#    # textbox 的返回值会追加一个换行符
#    choice = g.buttonbox("检测到文件内容发生改变，请选择以下操作：", "警告", ("覆盖保存", "放弃保存", "另存为..."))
#    if choice == "覆盖保存":
#        with open(file_path, "w") as old_file:
#            old_file.write(text_after[:-1])
#    if choice == "放弃保存":
#        pass
#    if choice == "另存为...":
#        another_path = g.filesavebox(default=".txt")
#        if os.path.splitext(another_path)[1] != '.txt':
#            another_path += '.txt'
#        with open(another_path, "w") as new_file:
#            new_file.write(text_after[:-1])




# 4.写一个程序统计你当前代码量总和，并显示离十万行代码还有多远
import easygui as g
import os

def show_result(start_dir):
    lines = 0
    total = 0
    text = ""

    for i in source_list:
        lines = source_list[i]
        total += lines
        text += "【%s】源文件 %d 个，源代码 %d 行\n" % (i, file_list[i], lines)
    title = '统计结果'
    msg = '您目前共累积编写了 %d 行代码，完成进度：%.2f %%\n离 10 万行代码还差 %d 行，请继续努力！' % (total, total/100000, 100000-total)
    g.textbox(msg, title, text)

def calc_code(file_name):
    lines = 0
    with open(file_name) as f:
        print('正在分析文件：%s ...' % file_name)
        try:
            for each_line in f:
                lines += 1
        except UnicodeDecodeError:
            pass # 不可避免会遇到格式不兼容的文件，这里忽略掉......
    return lines

def search_file(start_dir) :
    # 改变工作目录
    os.chdir(start_dir)
    # os.listdir() 列举出指定目录中的文件名
    for each_file in os.listdir(os.curdir) :
        # os.path.splitext() 分离文件名与扩展名，返回元组
        ext = os.path.splitext(each_file)[1]
        if ext in target :
            lines = calc_code(each_file) # 统计行数
            # 还记得异常的用法吗？如果字典中不存，抛出 KeyError，则添加字典键
            # 统计文件数
            try:
                file_list[ext] += 1
            except KeyError:
                file_list[ext] = 1      
            # 统计源代码行数
            try:
                source_list[ext] += lines
            except KeyError:
                source_list[ext] = lines
        
        # os.path.isdir() 判断指定路径是否存在且是一个目录
        if os.path.isdir(each_file) :
            search_file(each_file) # 递归调用
            os.chdir(os.pardir) # 递归调用后切记返回上一层目录
            
target = ['.c', '.cpp', '.py', '.cc', '.java', '.pas', '.asm']
file_list = {}
source_list = {}

g.msgbox("请打开您存放所有代码的文件夹......", "统计代码量")
path = g.diropenbox("请选择您的代码库：")

search_file(path)
show_result(path)
