# 单分支  if <条件> :  <语句块1>
# 二分支  if <条件> :  <语句块1>    else:  <语句块2>


# 紧凑形式
# 适用于简单表达式的二分支结构
# <表达式1> if <条件> else <表达式2>
guess = eval(input("请输入要猜的数字："))
print("猜{}了".format("对" if guess == 99 else "错"))


# 多分支结构
score = eval(input("输入成绩："))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "不及格"
print("输入成绩属于级别{}".format(grade))



# 条件判断及组合
# > < >= <= == !=
# and or not
guess = eval(input("请输入要猜的数字："))
if guess > 99 or guess < 99:
    print("猜对了")
else:
    print("猜错了")



# 异常处理   try    except    else(不发生异常时执行)    finally(一定执行)
try:
    num = eval(input("输入一个整数："))
    pirnt(num**2)
except NameError:
    print("输入的不是整数")
    
