# 给你前面绘制的立方图指定颜色映射。

# 绘制5000个
import matplotlib.pyplot as plt

# 绘制5000个
x_values = list(range(1,5001))
values2 = [ x**3 for x in x_values]
plt.scatter(x_values, values2, c = values2, cmap=plt.cm.BuGn, edgecolors='none', s=40)

plt.title("Cubes", fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Cube of Value', fontsize=14)
plt.tick_params(axis='both', labelsize=14)

plt.show()