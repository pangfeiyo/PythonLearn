import datetime
imyear = input("请输入您的出生年份：")	
nowyear = datetime.datetime.now().year	# 当年年份

age = nowyear - int(imyear)
print("您的年龄为:" + str(age) + "岁")

if age < 18:
	print("您现在为未成年人")
if age >= 18 and age < 66:
	print("您现在为青年人")
if age >= 66 and age < 80:
	print("您现在为中年人")
if age >= 80 :
	print("您现在为老年人")