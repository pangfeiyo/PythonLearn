# 如果你同时掷三个 D6 骰子，可能得到的最小点数为 3 ，而最大点数为 18 。请通过可视化展示同时掷三个 D6 骰子的结果。

import pygal
# 若不在同一目录，python查找不到，必须进行查找路径的设置，将模块所在的文件夹加入系统查找路径
import sys
sys.path.append("..")   # 上级目录
from die import Die

die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)

result = [die_1.roll() + die_2.roll() + die_3.roll() for roll_num in range(1000)]

# 两个骰子面和
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides

# 统计每个合有多少个
frequencies = [result.count(value) for value in range(3, max_result+1)] # 三个骰子最小和为3

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling two D8 dice 1000 times."
hist.x_labels = [str(x) for x in range(3, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

# 将值添加到表中
hist.add("D6 + D6 + D6", frequencies)
hist.render_to_file('15-8.svg')