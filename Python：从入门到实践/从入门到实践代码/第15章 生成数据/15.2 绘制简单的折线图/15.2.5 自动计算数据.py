# 手工计算列表要包含的值可能效率低下，需要绘制的点很多时尤其如此。
# 可以不必手工计算包含点坐标的列表，而让 Python 循环来替我们完成这种计算。
# 下面是绘制 1000 个点的代码：

import matplotlib.pyplot as plt

# 包含数字 1 ~ 1000
x_values = list(range(1,1001))
# 遍历 x 值 （for x in x_values），计算其值平方
y_values = [x**2 for x in x_values]

# s = 40  应该是点的尺寸大小
plt.scatter(x_values, y_values, s = 40)

# 设置每个坐标轴的取值范围
# 由于这个数据集较大，我们将点设置得较小，并使用函数 axis() 指定了每个坐标轴的取值范围
# 函数 axis() 要求提供四个值： x  和 y  坐标轴的最小值和最大值。
plt.axis([0,1100,0,1100000])

plt.show()