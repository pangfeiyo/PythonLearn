# 修改 rw_visual.py ，将其中的 plt.scatter() 替换为 plt.plot() 。
# 为模拟花粉在水滴表面的运动路径，向 plt.plot() 传递 rw.x_values和 rw.y_values ，
# 并指定实参值 linewidth 。使用 5000 个点而不是 50 000 个点。

import matplotlib.pyplot as plt

# 若不在同一目录，python查找不到，必须进行查找路径的设置，将模块所在的文件夹加入系统查找路径
import sys
sys.path.append('..')
from random_walk import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:

    # 创建一个RandomWalk 实例，并将其包含的点都绘制出来
    rw = RandomWalk(5000)  # 增加点数，初始5000
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    '''
    函数 figure() 用于指定图表的宽度、高度、分辨率和背景色。
    你需要给形参 figsize 指定一个元组，向 matplotlib 指出绘图窗口的尺寸，单位为英寸。
    Python 假定屏幕分辨率为 80 像素 / 英寸，如果上述代码指定的图表尺寸不合适，可根据需要调整其中的数字。
    如果你知道自己的系统的分辨率，可使用形参 dpi 向 figure() 传递该分辨率，以有效地利用可用的屏幕空间，如下所示：
    plt.figure(dpi=128, figsize=(10,6))    
    '''
    plt.figure(figsize = (6,4))

    '''
    我们将使用颜色映射来指出漫步中各点的先后顺序，并删除每个点的黑色轮廓，让它们的颜色更明显。
    为根据漫步中各点的先后顺序进行着色，我们传递参数 c ，并将其设置为一个列表，
    其中包含各点的先后顺序。由于这些点是按顺序绘制的，因此给参数 c 指定的列表只需包含数字 1~5000
    '''
    point_numbers = list(range(rw.num_points))
    # zorder 层级，较高的放在较低的顶层
    plt.plot(rw.x_values, rw.y_values, linewidth=1, zorder=1) # 增加点数之后，调小每个点的大小

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
                edgecolors='none', s=100, zorder=2)

    plt.show()

    keep_running = input("Make another walk? (y/n) :")
    if keep_running == "n":
        break