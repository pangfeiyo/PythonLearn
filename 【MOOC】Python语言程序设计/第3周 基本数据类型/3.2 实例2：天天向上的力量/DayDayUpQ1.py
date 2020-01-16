# 1‰的力量，每天增加和减少1‰，持续365天
dayup = pow(1.001, 365)
daydown = pow(0.999, 365)
print("向上：{:.2f}，向下：{:.2f}".format(dayup, daydown))


# 每天增加5‰或1%的力量，每天减少5‰或1%的力量
dayfactor = 0.005
dayup = pow(1+dayfactor, 365)
daydown = pow(1-dayfactor, 365)
print("向上：{:.2f}，向下：{:.2f}".format(dayup, daydown))

dayfactor = 0.01
dayup = pow(1+dayfactor, 365)
daydown = pow(1-dayfactor, 365)
print("向上：{:.2f}，向下：{:.2f}".format(dayup, daydown))


# 一年365天，一周5个工作日，每天进步1%
# 一年365天，一周2个休息日，每天退休1%
dayup = 1.0
dayfactor = 0.01
for i in range(365):
    if i % 7 in [6,0]:
        dayup = dayup * (1 - dayfactor)
    else:
        dayup = dayup * (1 + dayfactor)

print("工作日的力量：{:.2f}".format(dayup))


# 工作日模式要努力到什么水平，才能与每天努力1%结果一样
# A君：一年365天，每天进步1%，不停歇
# B君：一年365天，每周工作5天休息2天，休息日下降1%，要多努力？
def dayUP(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6,0]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + df)
    return dayup
dayfactor = 0.01
while dayUP(dayfactor) < 37.78:
    dayfactor += 0.001
print("工作日要努力参数是：{:.3f}".format(dayfactor))
