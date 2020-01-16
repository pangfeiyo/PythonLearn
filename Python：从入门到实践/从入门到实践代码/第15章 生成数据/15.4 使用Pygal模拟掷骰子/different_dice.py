# 两个不同的骰子

from die import Die
import pygal

# 创建一个D6和D10
die_1 = Die()
die_2 = Die(10)

# 掷骰子多次，并将结果存到一个列表中
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    print(result)
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides  # 计算所有的面
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 可视化结果
hist = pygal.Bar()

hist.title = "Result of rolling a D6 and D10 50,000 times."
x_labels_num = range(2,17)
hist.x_labels = x_labels_num
hist._x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6 + D10", frequencies)
hist.render_to_file('dice2_visual.svg')