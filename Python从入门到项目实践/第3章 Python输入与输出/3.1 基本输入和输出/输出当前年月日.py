import datetime
print("当前年份：" + str(datetime.datetime.now().year))	# 输出当前年份

# 输出当前日期和时间
print("当前日期时间：" + datetime.datetime.now().
	strftime('%y-%m-%d %H:%M:%S'))