'''
------------

取 1/3

     /\  
    /  \            一次科赫曲线
---      ---        四段1/3长
    60度
'''


import turtle
def koch(size, n):  # size 每一个直线长度  n 阶数，次数
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]: # 先循环angle=0的[0,60,-120,60]，再循环angle=60的[0,60,-120,60]，……
            turtle.left(angle)
            koch(size/3, n-1)

def main():
    turtle.setup(800,400)
    turtle.penup()
    turtle.goto(-300,-50)   # 使海龟到达某点
    turtle.pendown()
    turtle.pensize(2)
    level = 2   # 3阶科赫曲线，阶数
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.hideturtle() # 隐藏乌龟，可以提高速度
    turtle.done()

main()