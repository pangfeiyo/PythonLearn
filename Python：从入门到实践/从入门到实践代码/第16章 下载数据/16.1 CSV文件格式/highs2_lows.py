import csv
from matplotlib import pyplot as plt
from datetime import datetime   # 导入模块datetime 中的datetime类

# 涵盖更长的时间，以成一幅更复杂的锡特卡天气图
# 并添加最低温
file_num = input("请输入文件编号（1.阿拉斯加  2.锡特卡  3.死亡谷）：")
if file_num == "1":
    filename = "sitka_weather_07-2014.csv"
if file_num == "2":
    filename = "sitka_weather_2014.csv"
elif file_num == "3":
    filename = 'death_valley_2014.csv'

# 提取并读取数据
# 知道需要哪些列中的数据后，我们来读取一些数据。首先读取每天的最高气温：
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 创建空列表用来存放日期、最高温、最低温
    dates, highs, lows = [], [], []
    # 遍历余下各行
    for row in reader:
        try:
            # 将包含日期信息的数据（ row[0] ）转换为 datetime 对象
            current_date = datetime.strptime(row[0], "%Y/%m/%d")
            high = int(row[1])  # 转换为int ，可以让matplotlib读取
            low = int(row[3])

        except ValueError:
            print(current_date, "missing data")

        else:
            dates.append(current_date)

            # 阅读器对象从其停留的地方继续往下读取 CSV 文件，每次都自动返回当前所处位置的下一行。（读了一整行）
            # 由于我们已经读取了文件头行，这个循环将从第二行开始 —— 从这行开始包含的是实际数据。
            # 每次执行该循环时，我们都将索引 1 处（第 2 列）的数据附加到 highs 末尾
            # 这两条移到上面了 high = int(row[1])  # 转换为int ，可以让matplotlib读取
            # low = int(row[3])
            highs.append(high)
            lows.append(low)

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
# 给图表区域着色
# alpha 指定颜色的透明度, 0为完全透明， 1（默认）完全不透明。设置0.5可让红色和蓝色折线颜色看起来更浅
plt.plot(dates, highs, c="red", alpha = 0.5)    # .plot 一种图表类型  最高温
plt.plot(dates, lows, c= "blue", alpha = 0.5)    # 最低温
# 方法 fill_between() ，它接受一个 x  值系列和两个 y  值系列，并填充两个 y  值系列之间的空间
# 向 fill_between() 传递了一个 x  值系列：列表 dates ，还传递了两个 y  值系列： highs 和 lows 。
# 实参 facecolor 指定了填充区域的颜色，我们还将 alpha设置成了较小的值 0.1 ，让填充区域将两个数据系列连接起来的同时不分散观察者的注意力
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# 设置图表的格式
title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize = 24)
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