# 请模拟同时掷两个 8 面骰子 1000 次的结果。逐渐增加掷骰子的次数，直到系统不堪重负为止。
import pygal

# 若不在同一目录，python查找不到，必须进行查找路径的设置，将模块所在的文件夹加入系统查找路径
import sys
sys.path.append("..")   # 上级目录
from die import Die

die_1 = Die(8)
die_2 = Die(8)

result = [die_1.roll() + die_2.roll() for roll_num in range(1000000)]

# 两个骰子面和
max_result = die_1.num_sides + die_2.num_sides

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
hist.render_to_file('15-7.svg')