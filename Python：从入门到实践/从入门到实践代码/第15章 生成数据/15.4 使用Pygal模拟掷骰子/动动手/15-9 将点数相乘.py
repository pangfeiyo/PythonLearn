# 同时掷两个骰子时，通常将它们的点数相加。请通过可视化展示将两个骰子的点数相乘的结果。
import sys
sys.path.append("..")
import pygal
from die import Die

die_1 = Die()
die_2 = Die()

# 两个骰子投掷结果相乘
result = [die_1.roll() * die_2.roll() for roll_num in range(1000)]

# 两个骰子面乘
max_result = die_1.num_sides * die_2.num_sides

# 统计每个合有多少个
frequencies = [result.count(value) for value in range(2, max_result+1)]

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling two D8 dice 1,000,000 times."
hist.x_labels = [str(x) for x in range(2, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

# 将值添加到表中
hist.add("D8 + D8", frequencies)
hist.render_to_file('15-9.svg')