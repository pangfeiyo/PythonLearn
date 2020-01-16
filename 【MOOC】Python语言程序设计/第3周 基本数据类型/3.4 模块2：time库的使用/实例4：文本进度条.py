# 文本进度条
# - 采用字符串方式打印可以动态变化的文本进度条
# - 进度条需要能在一行中逐渐变化
import time
'''
scale = 10 # 进度条大概宽度
print("-----执行开始-----")

for i in range(scale+1):
    a = "*" * i
    b = "." * (scale - i)
    c = (i / scale) * 100
    # ^ 居中，3 宽度  0.f 0个浮点数
    print("{:^3.0f}%[{}->{}]".format(c, a, b))
    time.sleep(0.1)

print("-----执行结束-----")



# 单行动态刷新
# - 刷新本质：用后打印的字符覆盖之前的字符
# - 不能换行：print()需要被控制
# - 要能回退：打印后光际退回到之前的位置 \r
for i in range(101):
    print("\r{:3}%".format(i),end="")
    time.sleep(0.1)
# 在idle环境下，会屏蔽掉\r，可以用cmd来调用
'''


# 完整效果
scale = 50
print("执行开始".center(scale//2, "-"))
start = time.perf_counter()
for i in range(scale + 1):
    a = "*" * i
    b = "." * (scale - i)
    c = (i/scale) * 100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur), end="")
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2, "-"))


'''
举一反三   文本进度条的不同设计函数
设计名称               趋势          设计函数
Liner               Constant         f(x) = x
Early Pause         Speeds up        f(x) = x + (1-sin(x*π*2 + π/2)/-8
Late Pause          Slows down       f(x) = x + (1-sin(x*π*2 + π/2)/8
Slow Wavy           constant         f(x) = x + sin(x*π*5)/20
Fast Wavy           constant         f(x) = x + sin(x*π*20)/80
Power               speeds up        f(x) = (x + (1-x)*0.03)^2
Inverse Power       Slows down       f(x) = 1 + (1-x)^1.5 * -1
Fast Power          Speeds up        f(x) = (x+(1-x)/2)^8
Inverse Fast Power  Slows down       f(x) = 1 + (1-x)^3 * -1
'''
