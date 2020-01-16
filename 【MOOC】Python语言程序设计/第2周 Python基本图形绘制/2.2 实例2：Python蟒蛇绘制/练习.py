import turtle

# 方法一：使用海龟相对坐标 left 或 right
def 相对坐标正方形():
    turtle.setup(650,350)
    turtle.penup()
    turtle.fd(-250)
    turtle.pendown()
    turtle.fd(100)
    turtle.right(90)
    turtle.fd(100)
    turtle.right(90)
    turtle.fd(100)
    turtle.right(90)
    turtle.fd(100)
    turtle.done()
	

# 方法二：使用屏幕绝对坐标 turtle.seth
def 绝对坐标正方形():
    turtle.setup(650,350)
    turtle.penup()
    turtle.fd(-250)
    turtle.pendown()
    turtle.fd(100)
    turtle.seth(-90)
    turtle.fd(100)
    turtle.seth(-180)
    turtle.fd(100)
    turtle.seth(-270)
    turtle.fd(100)
	

def 六边形():
    turtle.setup(650,350)
    turtle.penup()
    turtle.left(90)
    turtle.fd(100)
    turtle.right(90)
    turtle.pendown()
    turtle.fd(100)
    for i in range(5):
        turtle.right(60)
        turtle.fd(100)
		
		
def 叠边形():
    for i in range(9):
        turtle.fd(100) 
        turtle.left(80)
    turtle.mainloop()
		
				
def 同切圆():
    turtle.circle(20)
    turtle.circle(40)
    turtle.circle(60)
    turtle.circle(80)
    turtle.mainloop()

def 长度转换():
    """米和英寸之间的长度转换"""
    lenc = input("请输入带有符号的长度值：")
    if lenc[-1] in ['m','M']:
        I = eval(lenc[0:-1]) * 39.37
        print("{:.3f}in".format(I))
    elif lenc[-2:] in ["in","IN","In","iN"]:
        M = eval(lenc[0:-2]) / 39.37
        print("{:.3f}m".format(M))
    else:
        print("输入错误")
    

num = int(input("请输入要运行的程序："))
if num == 1:
    相对坐标正方形()
if num == 2:
    绝对坐标正方形()
if num == 3:
    六边形()
if num == 4:
    叠边形()
if num == 5:
    同切圆()
if num == 6:
    长度转换()
