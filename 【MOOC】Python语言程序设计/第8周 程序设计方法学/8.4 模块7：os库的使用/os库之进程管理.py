'''
os.system(command)

执行程序或命令command
在windows中，返回值为cmd的调用返回信息

'''
import os

# 调用windows自带的计算器程序 
# 返回值为0，表示正在调用
#os.system("c:\\Windows\\System32\\calc.exe")

# 路径这里有个空格 导致无法打开图画后在图画里打开这个路径下的图片
mspaint = r'C:/Windows/System32/mspaint.exe'
gc = r'D:/pythonlearn/PythonLearn/【mooc】Python语言程序设计/第7周 文件和数据格式化/7.6 实例12：政府工作报告词云/grwordcloud1.png'
commond = "{} {}".format(mspaint, gc)
os.system(commond)
