import csv
from matplotlib import pyplot as plt
from datetime import datetime   # 导入模块datetime 中的datetime类

filename = "sitka_weather_07-2014.csv"

# 这个with open 是用来看的
# 导入模块 csv 后，我们将要使用的文件的名称存储在 filename 中。接下来，我们打开这个文件，并将结果文件对象存储在 f 中
with open(filename) as f:

    #我们调用csv.reader() ，并将前面存储的文件对象作为实参传递给它，从而创建一个与该文件相关联的阅读器（ reader ）对象
    reader = csv.reader(f)

    # 模块 csv 包含函数 next() ，调用它并将阅读器对象传递给它时，它将返回文件中的下一行。
    # 在前面的代码中，我们只调用了 next() 一次，因此得到的是文件的第一行，其中包含文件头
    header_row = next(reader)

    # 为让文件头容易理解，将列表中的每个文件头及其位置打印出来
    # 调用 enumerate() 来获取每个元素的索引及其值
    for index, column_header in enumerate(header_row):
        print(index, column_header) # 从而可知，日期和最高温分别存储在第0列和第1列



# 提取并读取数据
# 知道需要哪些列中的数据后，我们来读取一些数据。首先读取每天的最高气温：
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 创建空列表用来存放日期和最高温
    dates, highs = [], []
    # 遍历余下各行
    for row in reader:

        # 将包含日期信息的数据（ row[0] ）转换为 datetime 对象
        current_date = datetime.strptime(row[0], "%Y/%m/%d")
        dates.append(current_date)

        # 阅读器对象从其停留的地方继续往下读取 CSV 文件，每次都自动返回当前所处位置的下一行。（读了一整行）
        # 由于我们已经读取了文件头行，这个循环将从第二行开始 —— 从这行开始包含的是实际数据。
        # 每次执行该循环时，我们都将索引 1 处（第 2 列）的数据附加到 highs 末尾
        high = int(row[1]) # 转换为int ，可以让matplotlib读取
        highs.append(high)

    print(highs)


# 根据数据绘制图形
'''
    函数 figure() 用于指定图表的宽度、高度、分辨率和背景色。
    你需要给形参 figsize 指定一个元组，向 matplotlib 指出绘图窗口的尺寸，单位为英寸。
    Python 假定屏幕分辨率为 80 像素 / 英寸，如果上述代码指定的图表尺寸不合适，可根据需要调整其中的数字。
    如果你知道自己的系统的分辨率，可使用形参 dpi 向 figure() 传递该分辨率，以有效地利用可用的屏幕空间，如下所示：
    plt.figure(dpi=128, figsize=(10,6))    
    '''
fig = plt.figure(dpi=128, figsize =(10,6))   # 自定义窗口
# 将日期和最高气温值传递给 plot()
plt.plot(dates, highs, c="red")    # .plot 一种图表类型

# 设置图表的格式
plt.title("Daily high temperatures, July 2014", fontsize = 24)
plt.xlabel("", fontsize = 16)
# 调用了 fig.autofmt_xdate() 来绘制斜的日期标签，以免它们彼此重叠
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)

# 设置刻度标记的大小
# 函数 tick_params() 设置刻度的样式，
# 其中指定的实参将影响 x  轴和 y  轴上的刻度（ axes='both' ）
plt.tick_params(axis='both', which='major', labelsize = 16)

plt.show()

# 调用strptime()方法，前者为实参，后者为设置日期的格式
# '%Y-' 让 Python 将字符串中第一个连字符前面的部分视为四位的年份；
# '%m-' 让 Python 将第二个连字符前面的部分视为表示月份的数字；而 '%d' 让 Python 将字符串的最后一部分视为月份中的一天（ 1~31 ）
# first_date = datetime.strptime('2014-7-1', '%Y-%m-%d')  # %Y 四位的年份，2015     %y 两位的年份，15
# print(first_date)