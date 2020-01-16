# 颜色映射 （ colormap ）是一系列颜色，它们从起始颜色渐变到结束颜色。
# 在可视化中，颜色映射用于突出数据的规律，
# 例如，你可能用较浅的颜色来显示较小的值，并使用较深的颜色来显示较大的值。
# 模块 pyplot 内置了一组颜色映射。
# 要使用这些颜色映射，你需要告诉 pyplot 该如何设置数据集中每个点的颜色。
# 下面演示了如何根据每个点的 y  值来设置其颜色：

import matplotlib.pyplot as plt

# 包含数字 1 ~ 1000
x_values = list(range(1,1001))
# 遍历 x 值 （for x in x_values），计算其值平方
y_values = [x**2 for x in x_values]


# matplotlib 允许你给散点图中的各个点指定颜色。
# 默认为蓝色点和黑色轮廓，在散点图包含的数据点不多时效果很好。但绘制很多点时，黑色轮廓可能会粘连在一起。
# 要删除数据点的轮廓，可在调用 scatter() 时传递实参 edgecolor='none' ：
# 我们将参数 c 设置成了一个 y  值列表，并使用参数 cmap 告诉 pyplot 使用哪个颜色映射。
# 这些代码将 y  值较小的点显示为浅蓝色，并将 y  值较大的点显示为深蓝色，生成的图形
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
            edgecolors='none', s=40)

# 设置每个坐标轴的取值范围
# 由于这个数据集较大，我们将点设置得较小，并使用函数 axis() 指定了每个坐标轴的取值范围
# 函数 axis() 要求提供四个值： x  和 y  坐标轴的最小值和最大值。
plt.axis([0,1100,0,1100000])

plt.show()