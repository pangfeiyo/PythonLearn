# 数字的三次方被称为其立方。
# 请绘制一个图形，显示前 5 个整数的立方值，再绘制一个图形，显示前 5000 个整数的立方值。
import matplotlib.pyplot as plt

x_values = [1,2,3,4,5]
values = []
for i in range(1,6):
    values.append(i ** 3)
plt.scatter(x_values, values, edgecolors='none', s=40)

plt.title("Cubes", fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Cube of Value', fontsize=14)
plt.tick_params(axis='both', labelsize=14)

plt.show()

# 绘制5000个
x_values = list(range(1,5001))
values2 = [ x**3 for x in x_values]
plt.scatter(x_values, values2, edgecolors='none', s=40)

plt.title("Cubes", fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Cube of Value', fontsize=14)
plt.tick_params(axis='both', labelsize=14)

plt.show()