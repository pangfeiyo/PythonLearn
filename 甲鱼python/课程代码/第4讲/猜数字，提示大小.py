import random    #导入模块  随机
secret = random.randint(1,10)   #randint(1,10)  随机1到10
print(secret)
num = 0     #次数

print('--------猜数游戏----------')
#这里先给guess赋值（赋一个绝对不等于secret的值）
guess = 0
#print()默认是打印完字符串会自动添加一个换行符， end=" " 参数告诉print()用空格代替换行
print('猜我在想什么数：', end=" ")
while (guess != secret ) and (num <4):
    temp = input()
    while not temp.isdigit():    #isdigit()，全是数字返回True，否则返回False，默认返回为True
        temp =input('请输入数字：')
    guess = int(temp)   #如果temp输入的内容返回为True，这里转成int
    num = num + 1
    if guess == secret:
        print('哇，真厉害，猜对了！')
    else:
        if guess > secret:
            print("猜大了！")
        else:
            print('猜小了！')
        if num < 4:
            print("再试一次：",end=" ")
        else:
            print('机会用光了')
print("游戏结束")

