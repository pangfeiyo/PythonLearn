# 使用这个类来创建图表前，先来掷D6骰子，将结果打印，并检查结果是否合理
from die import Die
import pygal

# 创建一个D6
die = Die()

# 掷几次骰子，并将结果存到一个列表中
results = [die.roll() for roll_num in range(1000)]  # 列表解析
'''
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
'''
print(results)

# 分析结果
frequencies = [results.count(value) for value in range(1, die.num_sides+1)] # 列表解析
'''
for value in range(1, die.num_sides+1): # 1~6
    # count() 统计字符串里某个字符出现的次数
    frequency = results.count(value)
    frequencies.append(frequency)
'''

# 对结果进行可视化
# 绘制直方图
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = [str(x) for x in range(1, die.num_sides+1)] # ['1','2','3','4','5','6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

# 我们使用 add() 将一系列值添加到图表中（向它传递要给添加的值指定的标签，还有一个列表，其中包含将出现在图表中的值）
hist.add("D6",frequencies)
# 最后，我们将这个图表渲染为一个 SVG 文件，这种文件的扩展名必须为 .svg
hist.render_to_file("die_visual.svg")