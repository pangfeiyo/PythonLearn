'''
BMI = 体重(kg) / 身高^2(m^2)

分类        国际        国内
偏瘦       <18.5       <18.5
正常      18.5~25     18.5~24
偏胖       25～30      24～28
肥胖        >=30        >=28
'''

# 输入：给定体重和身高
# 输出：BMI指标分类信息（国际和国外）
height, weight = eval(input("请输入身高（米）和体重（公斤）[逗号隔开]："))
bmi = weight / pow(height, 2)
print("BMI 数值为：{:.2f}".format(bmi))
who, nat = "", ""
if bmi < 18.5:
    who, nat ="偏瘦", "偏瘦"
elif 18.5 <= bmi < 24:
    who, nat = "正常", "正常"
elif 24 <= bmi < 25:
    who, nat = "正常", "偏胖"
elif 25 <= bmi < 28:
    who, nat = "偏胖", "偏胖"
elif 28 <= bmi < 30:
    who, nat = "偏胖", "肥胖"
else:
    who, nat = "肥胖", "肥胖"
print("BMI 指标为：国际'{0}'，国内'{1}'".format(who,nat))
