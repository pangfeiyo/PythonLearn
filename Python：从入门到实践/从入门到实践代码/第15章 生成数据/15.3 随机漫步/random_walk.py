# 为模拟随机漫步，我们将创建一个名为 RandomWalk 的类，它随机地选择前进方向。
# 这个类需要三个属性，其中一个是存储随机漫步次数的变量，其他两个是列表，
# 分别存储随机漫步经过的每个点的 x  和 y  坐标。
# RandomWalk 类只包含两个方法： __init__() 和 fill_walk() ，其中后者计算随机漫步经过的所有点。

from random import choice

class RandomWalk():
    """生成一个随机漫步数据的类"""

    def __init__(self, num_points = 5000):  # point 点/指向   points 要点
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 所有随机漫步都要始于(0,0)
        self.x_values = [0]
        self.y_values = [0]

    def get_setp(self):
        """简化 方法fill_walk 中的 x_step 和 y_step 的过程"""
        # 不断漫步，直到列表达到指定的长度
        # 如果 x_step 和 y_step 一样的算法
        direction = choice([1,-1])  # 结果要么向右走1，要么向左走-1
        distance = choice([0,1,2,3,4])  # 随机走多远（包含0，不仅能沿两个轴移动，还能沿y轴移动）
        '''
        将移动方向乘以移动距离，以确定沿 x  和 y  轴移动的距离。
        如果 x_step 为正，将向右移动，为负将向左移动，而为零将垂直移动；
        如果 y_step 为正，就意味着向上移动，为负意味着向下移动，而为零意味着水平移动。
        如果 x_step 和 y_step 都为零，则意味着原地踏步，我们拒绝这样的情况，接着执行下一次循环
        '''
        step = direction * distance
        return step

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        while len(self.x_values) < self.num_points:

            # 决定前进方向以及沿这个方向前进的距离
            x_step = self.get_setp()
            y_step = self.get_setp()

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