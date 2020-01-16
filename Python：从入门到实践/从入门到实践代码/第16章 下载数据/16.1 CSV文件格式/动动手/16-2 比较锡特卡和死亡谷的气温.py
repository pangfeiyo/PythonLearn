# 在有关锡特卡和死亡谷的图表中，气温刻度反映了数据范围的不同。
# 为准确地比较锡特卡和死亡谷的气温范围，需要在 y  轴上使用相同的刻度。
# 为此，请修改图 16-5 和图 16-6 所示图表的 y  轴设置，对锡特卡和死亡谷的气温范围进行直接比较（你也可以对任何两个地方的气温范围进行比较）。
# 你还可以尝试在一个图表中呈现这两个数据集。

import csv
from datetime import datetime
from matplotlib import pyplot as plt

'''
# 从文件中获取日期，最高和最低温
filename = "../sitka_weather_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y/%m/%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "missing date")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

title = "Daily high and low temperatures - 2014\nSitka, AK"
plt.title(title, fontsize=20)
plt.xlabel("", fontsize=20)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(10,120)

plt.show()
'''

def get_weather_data(filename, dates, highs, lows):
    """ 从数据文件中获取高点和低点"""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # dates, highs, lows = [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y/%m/%d")
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(current_date, "missing data")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

# 获取天气数据
dates, highs, lows = [], [], []
get_weather_data("../sitka_weather_2014.csv", dates, highs, lows)

# 绘制天气数据
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red', alpha=0.6)
plt.plot(dates, highs, c='blue', alpha=0.6)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.15)

# 获取死亡谷数据
dates, highs, lows = [], [], []
get_weather_data('../death_valley_2014.csv', dates, highs, lows)

# Add Death Valley data to current plot.
plt.plot(dates, highs, c='red', alpha=0.3)
plt.plot(dates, lows, c='blue', alpha=0.3)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.05)

# 将死亡谷数据添加到当前的图中.
title = "Daily high and low temperatures - 2014"
title += "\nSitka, AK and Death Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(10, 120)

plt.show()
