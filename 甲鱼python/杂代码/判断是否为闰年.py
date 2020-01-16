temp = input("请输入一个年份：")
while not temp.isdigit():    #isdigit() 判断输入是否为全数字，是返回ture，不是返回FALSE
    temp = input("抱歉，您的输入有误，请重新输入：")

year = int(temp)
if year/400 == int(year/400):
    print(temp + '是闰年!')
    
