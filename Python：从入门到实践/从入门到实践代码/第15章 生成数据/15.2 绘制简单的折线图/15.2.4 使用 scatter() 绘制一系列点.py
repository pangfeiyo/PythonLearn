# 要绘制一系列的点，可向 scatter() 传递两个分别包含 x  值和 y  值的列表

import matplotlib.pyplot as plt

# 包含要计算平方的数字
x_values = [1,2,3,4,5]
# 包含前述每个数字的平方值
y_values = [1,4,9,16,25]

plt.scatter(x_values, y_values, s = 100)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

# 设置刻度标记的大小
plt.tick_params(axis = "both", which = "major", labelsize = 14)


plt.show()