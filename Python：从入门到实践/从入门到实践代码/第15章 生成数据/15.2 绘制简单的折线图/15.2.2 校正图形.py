# 上一个图形中，折线图的终点指出4.0的平方是25
# 现在来修复

#当你向 plot() 提供一系列数字时，它假设第一个数据点对应的 x  坐标值为 0 ，
# 但我们的第一个点对应的 x  值为 1 。
# 为改变这种默认行为，我们可以给 plot() 同时提供输入值和输出值：
import matplotlib.pyplot as plt
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]

plt.plot(input_values, squares, linewidth = 5)

# 设置图表标题，并给坐标轴加上标签
# 标题
plt.title("Squares Numbers", fontsize = 24)

# xlabel ylabel 让你能够为每条轴设置标题
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Squares of Value",fontsize = 14)

# 设置刻度标记的大小
# 函数 tick_params() 设置刻度的样式，
# 其中指定的实参将影响 x  轴和 y  轴上的刻度（ axes='both' ）
plt.tick_params(axis="both", labelsize = 14)



plt.show()