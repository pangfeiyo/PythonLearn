# 基本思路
# 步骤1：绘制单个数字对应的数码管
# 步骤2：获得一串数字，绘制对应的数码管
# 步骤3：获得当前系统时间，绘制对应的数码管
#        - 使用time库获得系统当前时间
#        - 增加年月日标记
#        - 年月日颜色不同
'''
步骤1
        6  
      -----
     |     |
    5|     |7     - 七段数码管由7个基本线条组成
     |  1  |      - 七段数码管可以有固定顺序 
  *>  -----       - 不同数字显示不同的线条
     |     |      - *> 是起点
    4|     |2
     |     |
      -----
        3
'''
import time
import turtle
def drawGap():  # 绘制数码管间隔
    turtle.penup()
    turtle.fd(5)

def drawLine(draw): # 绘制单段数码管
    drawGap()
    # 如果draw为True,笔落下，否则提起
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)

def drawDigit(digit): # 根据数字绘制七段数码管，根据不同数字，决定哪条线亮
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    # 经过四次绘制现在已经回到起点，再执行drawLine会右转
    # 所以要向左转，方便drawLine的右转
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    # 每一次drawLine执行后都会向右转90度
    # 第7次执行后是在7和1的交点处向左转，所以这里要右转180度
    turtle.left(180)
    turtle.penup()  # 为绘制后续数字确定位置
    turtle.fd(20)   # 为绘制后续数字确定位置

def drawDate(date): # data为日期，格式为"%Y-%m=%d+" 这里的-=+可以换成任何字符
    turtle.pencolor("red")
    for i in date:
        if i == "-":
            # normal 正常，应该是加粗等选项
            turtle.write('年', font=('Arial', 18, "normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == "=":
            turtle.write('月', font=('Arial', 18, "normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == "+":
            turtle.write("日", font=('Arial', 18, 'normal'))
        else:
            drawDigit(eval(i))  # 通过eval()函数将数字变为整数
            
def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    # time.strftime() 时间格式化
    # time.gmtime() 获得当前时间，表示为计算机可处理的时间格式
    drawDate(time.strftime('%Y-%m=%d+', time.gmtime()))
    turtle.hideturtle() # 隐藏乌龟
    turtle.done()
main()


'''
理解方法思维
  - 模块化思维：确定模块接口，封装功能
  - 规则化思维：抽象过程为规则，计算机自动执行
  - 化繁为简：将大功能变为小功能组合，分而治之
'''
