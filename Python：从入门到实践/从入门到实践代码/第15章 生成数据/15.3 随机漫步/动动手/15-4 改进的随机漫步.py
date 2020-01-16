# 在类 RandomWalk 中， x_step 和 y_step 是根据相同的条件生成的：
# 从列表 [1, -1] 中随机地选择方向，并从列表 [0, 1, 2, 3, 4]中随机地选择距离。
# 请修改这些列表中的值，看看对随机漫步路径有何影响。
# 尝试使用更长的距离选择列表，如 0~8 ；或者将 -1 从 x  或 y  方向列表中删除。

from random import choice
import matplotlib.pyplot as plt

class RandomWalk():
    """生成一个随机漫步数据的类"""

    def __init__(self, num_points = 5000):  # point 点/指向   points 要点
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 所有随机漫步都要始于(0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        # 不断漫步，直到列表达到指定的长度
        '''
        建立了一个循环，这个循环不断运行，直到漫步包含所需数量的点。
        这个方法的主要部分告诉 Python 如何模拟四种漫步决定：向右走还是向左走？
        沿指定的方向走多远？向上走还是向下走？沿选定的方向走多远？
        '''
        while len(self.x_values) < self.num_points:

            # 决定前进方向以及沿这个方向前进的距离
            x_direction = choice([1])   # 结果要么向右走1，要么向左走-1
            x_distance = choice([0, 1, 2, 3, 4,5,6,7,8])    # 随机走多远（包含0，不仅能沿两个轴移动，还能沿y轴移动）
            '''
            将移动方向乘以移动距离，以确定沿 x  和 y  轴移动的距离。
            如果 x_step 为正，将向右移动，为负将向左移动，而为零将垂直移动；
            如果 y_step 为正，就意味着向上移动，为负意味着向下移动，而为零意味着水平移动。
            如果 x_step 和 y_step 都为零，则意味着原地踏步，我们拒绝这样的情况，接着执行下一次循环
            '''
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0, 1, 2, 3, 4,5,6,7,8])
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的 x 和 y 值
            '''
            为获取漫步中下一个点的 x  值，我们将 x_step 与 x_values 中的最后一个值相加，对于 y  值也做相同的处理。
            获得下一个点的 x  值和 y  值后，我们将它们分别附加到列表 x_values 和 y_values 的末尾
            这里用 [-1]，因为后面用了 .append() 
            '''
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


while True:

    # 创建一个RandomWalk 实例，并将其包含的点都绘制出来
    rw = RandomWalk(50000)  # 增加点数，初始5000
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
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolors='none', s=1) # 增加点数之后，调小每个点的大小

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
                edgecolors='none', s=100)

    plt.show()

    keep_running = input("Make another walk? (y/n) :")
    if keep_running == "n":
        break