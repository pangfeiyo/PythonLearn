    #PythonDraw.py
import turtle

def 海龟turtle演示():
    # turtle.setup(width, height, startx, starty)
     # 设置窗体大小及位置，后两参数可选（不写则默认居中）
    turtle.setup(650,350,200,200)
    turtle.penup()  # 抬起画笔
    turtle.fd(-250) # 向海龟的正前方运行
    turtle.pendown()    # 落下画笔
    turtle.pensize(25)
    turtle.pencolor("purple")
    turtle.seth(-40)    # 改变行进角度，逆时针为正

    for i in range(4):
        turtle.circle(40,80)
        turtle.circle(-40,80)

    turtle.circle(40, 80/2)
    turtle.fd(40)
    turtle.circle(16, 180)
    turtle.fd(40 * 2 /3)
    turtle.done()   # 运行之后需要手动关闭窗体


海龟turtle演示()


'''
from  import *
setup(650,350,200,200)
penup()
fd(-250)
pendown()
pensize(25)
pencolor("purple")
seth(-40)

for i in range(4):
    circle(40,80)
    circle(-40,80)

circle(40, 80/2)
fd(40)
circle(16, 180)
fd(40 * 2 /3)
done()
'''
