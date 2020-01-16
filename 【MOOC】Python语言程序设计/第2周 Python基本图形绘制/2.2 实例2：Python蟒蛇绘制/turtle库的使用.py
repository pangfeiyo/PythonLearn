import turtle


def 绝对坐标():
    # 绝对坐标  turtle.goto()  使海龟(turtle)到处该位置
    turtle.goto(100,100)
    turtle.goto(100,-100)
    turtle.goto(-100,-100)
    turtle.goto(-100,100)
    turtle.goto(0,0)


def 角度():
    turtle.seth(-135)   # turtle.seth(angle) 改变海龟行进角度。只改变方向，不行进
                        # turtle.left(angle) 向左或向右改变行进方向
                        # turtle.right(angle)
# 海龟方向：海龟当前前进方向不论朝向哪个方向，都是前进方向


def Z():
    turtle.left(45)
    turtle.fd(150)
    turtle.right(135)
    turtle.fd(300)
    turtle.left(135)
    turtle.fd(150)


num = int(input("""请输出要 运行的程序——
1、绝对坐标
2、角度
3、Z
"""))

if num == 1:
    绝对坐标()
if num == 2:
    角度()
if num == 3:
    Z()

'''
turtle.fd() 向海龟的正前方运行
turtle.bk() 反方向运行

turtle.cricle(r, extent=None) 以海龟当前位置左侧的某一个点为圆心，曲线行进
    根据半径r，绘制extent角度的弧形
    海龟默认在圆心左侧，r若为负数，海龟在右侧 
'''
