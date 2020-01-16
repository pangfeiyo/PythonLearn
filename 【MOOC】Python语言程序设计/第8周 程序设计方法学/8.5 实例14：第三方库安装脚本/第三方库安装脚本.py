'''
第三方库自动安装脚本
  - 需求：批量安装第三方库需要人工干预，能否自动安装？
  - 自动执行pip逐一根据安装需求安装

  如何自动执行一个程序？例如：pip？

  库名                用途                          pip安装指令
NumPy               N维数据表示和运算               pip install numpy
Matplotlib          二维数据可视化                  pip install matplotlib
PIL                 图像处理                        pip install pillow
Scikit-Learn        机器学习和数据挖掘              pip install skleran
Requests            Http协议访问及网络爬虫          pip install requests

Jieba               中文分词                        pip install jieba
Beautiful Soup      HTML和XML解析器                 pip install beautifulsoup4
Wheel               Python第三方库文件打包工具      pip install wheel
PyInstaller         打包Python源文件为可执行文件    pip install pyinstaller
Django              Python最流行的WEB开发框架       pip install django

Flask               轻量级Web开发框架               pip install flask
WeRoBot             微信机器人开发框架              pip install werobot
SymPy               数学符号计算工具                pip install sympy
Pandas              高效数据分析和计算              pip install pandas
Networkx            复杂网络和图结构的建模和分析    pip install networkx

PyQt5               基于Qt的专业级GUI开发框架       pip install pyqt5
PyOpenGL            多平台OpenGL开发接口            pip install pyopengl
PyPDF2              PDF文件内容提取及处理           pip install pypdf2
docopt              Python命令行解析                pip install docopt
PyGame              简单小游戏开发框架              pip install pygame
'''
import os
libs = {"numpy",'matplotlib','pillow','sklearn','requests',
        'jieba','beautifulsoup4','wheel','pyinstaller','django',
        "flask",'werobot','sympy','pandas','networkx',
        'pyqt5','pyopengl','pypdf2','docopt','pygame',}

try:
    for lib in libs:
        # 没有管理员权限  安装失败
        os.system("pip install " + lib)
    print("Successful")
except:
    print("Failed Somehow")