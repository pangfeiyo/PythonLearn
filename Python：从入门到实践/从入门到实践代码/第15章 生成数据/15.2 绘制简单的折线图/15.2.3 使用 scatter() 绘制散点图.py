# 有时候，需要绘制散点图并设置各个数据点的样式。
# 例如，你可能想以一种颜色显示较小的值，而用另一种颜色显示较大的值。
# 绘制大型数据集时，你还可以对每个点都设置同样的样式，再使用不同的样式选项重新绘制某些点，以突出它们。
# 要绘制单个点，可使用函数 scatter() ，并向它传递一对 x  和 y  坐标，它将在指定位置绘制一个点：

import matplotlib.pyplot as plt

plt.scatter(2, 4, s = 200)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

# 设置刻度标记的大小
plt.tick_params(axis = "both", which = "major", labelsize = 14)

plt.show()
