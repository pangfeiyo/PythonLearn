import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
# 决定绘制的线条的粗细
plt.plot(squares, linewidth = 5)

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