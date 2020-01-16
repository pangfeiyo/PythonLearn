# 使用这个类来创建图表前，先来掷D6骰子，将结果打印，并检查结果是否合理
from die import Die
import pygal

# 创建两个D6骰子
die_1 = Die()
die_2 = Die()

# 掷骰子多次，并将结果存到一个列表中
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)] # 列表解析
'''
for roll_num in range(1000):
    # 计算每次的总点数
    result = die_1.roll() + die_2.roll()
    results.append(result)
'''
print(results)

# 分析结果
# 可能出现的最大点数 12 为两个骰子的最大可能点数之和，我们将这个值存储在了 max_result 中
max_result = die_1.num_sides + die_2.num_sides
# 本可以使用range(2,13)，但这只适合两个D6骰子。现在这种做法可以模拟任何两个骰子，而不管有几个面
frequencies = [results.count(value) for value in range(2, max_result+1)]    # 2~12  两个骰子最低和为2
'''
for value in range(2, max_result+1): # 2~12  两个骰子最低和为2
    # count() 统计字符串里某个字符出现的次数
    frequency = results.count(value)
    frequencies.append(frequency)
'''

# 对结果进行可视化
# 绘制直方图
hist = pygal.Bar()

hist.title = "Results of rolling one D6 dice 1000 times."
hist.x_labels = [str(x) for x in range(2, max_result+1)]    # ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

# 我们使用 add() 将一系列值添加到图表中（向它传递要给添加的值指定的标签，还有一个列表，其中包含将出现在图表中的值）
hist.add("D6 + D6", frequencies)
# 最后，我们将这个图表渲染为一个 SVG 文件，这种文件的扩展名必须为 .svg
hist.render_to_file("dice_visual.svg")