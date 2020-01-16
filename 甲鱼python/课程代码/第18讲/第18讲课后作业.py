def MyFun(x):
    return x ** 3

y =3
print(MyFun(y))

#编写一个符合以下要求的函数：
#1）计算打印所有参数的和乘以基数（base = 3）的结果
#2）如果参数中最后一个参数为（base = 5），则设定基数为5，基数不参与求和计算
def mFun(*param,base = 3):
    result = 0
    for each in param:
        result += each

    result = result * base


    print('结果是：',result)
mFun(1,2,3,4,5,base=5)


#寻找水仙花数
#如果一个3位数等于其各位数字的立方和，则称这个数为水仙花数。例如153 = 1 ^ 3 + 5 ^ 3 + 3 ^ 3，因为153是一个水仙花数。编写一个程序，找出所有水仙花数
def Narcissus():
    for each in range(100,1000):
        sum = 0
        temp = each
        while temp:
            sum = sum + (temp % 10) ** 3  #取余，得到个位数字，再 ** 3
            temp = temp // 10  #取整

        if sum == each:
            print(sum,end=" ")

print("所有水仙花数是：",end="")
Narcissus()

print(),print()
print(list(range(7)))

#编写一段函数findstr()，该函数统计一个长度为 2 的子字符串在另一个字符串中出现的次数。
#例如：假定输入的字符串为“You cannot improve your past,but you can improve your future.Once time is wasted,life is wasted”
#子字符串为"im"，函数执行后打印“子字符串在目标字符串中共出现3次”
def findstr(desStr='输入的字符串',subStr='查找的子字符串'):
    count = 0  #次数
    deslength = len(desStr)         #记录输入的字符串的长度
    sublength = len(subStr) - 1     #记录查找的子字符串的长度，这样可以随便输入多长都可以查找   。-1 的目的，因为下面是下标为0开始加的，已经有了最开始的下标
    if subStr not in desStr:
        print("在目标字符串中未找到该字符串！")
    else:
        for each in range(deslength):
            if desStr[each] == subStr[0]:
                if desStr[each + sublength] == subStr[0 + sublength]:
                    count += 1
        print('子字符串在目标字符串中共出现 %d 次' % count)
desStr = input('请输入目标字符串：')
subStr = input('请输入子字符串：')
#该程序还可以进一步修改，完善为不区分大小写
findstr(desStr.lower(),subStr.lower())          #s.lower()，将所有字符串转为小写
                                                #s.upper()，将所有字符串转为大写


