a = range(1,6,1)
for b in a :
    print(b,end=" ")

print()
print()

# 修改下列代码 ，提高效率
'''
i = 0
string = 'ILoveFishC.com'
print("string的长度是：",len(string))
while i < len(string):    #len 长度
    print(i)
    i += 1
'''

#修改后的代码，原代码之所以效率低，因为每次循环都要调用一次len()函数
i = 0
string = 'ILoveFishC.com'
length = len(string)
print("修改后的结果：")
while i <= length:
    print(i,end=" ")
    i += 1

print()
print()

#设计一个验证用户密码程序，用户只有三次机会输入错误，不过如果用户输入的内容包含“*”则不计算在次数内

count = 3  #次数
password = "FishC.com"

#python中默认0为false
while count:
    passwd = input("请输入密码：")
    if passwd == password:
        print("密码正确，进入程序中……")
        break
    elif '*' in passwd:   # in ，成员资格运算符  也可以用在for以外的地方
        print("密码中不能含有“*”号！您还有",count,'次机会',end=" ")
        continue
    else:
        print("密码输入错误！您还有",count - 1,'次机会！',end=" ")
    count -= 1



#编写一个程序，求100~999之间的所有水仙花数
#如果一个3位数等于其他各数的立方和，则称这个数为水仙花数。
#例：153=1^3 + 5^3 + 3^3，因此153就是一个水仙花数
#以下是系统自动列出，手动输入大同小异，判断是不是输入的全数字，看第四讲的猜数字.py  用 .isdigit()

print("水仙花数字是：",end=" ")
for i in range(100, 1000):                  #temp = 153 ,   153 % 10 = 3,3**3
    sum = 0                                 #153 // 10 = 15   取整   temp = 15
    temp = i                                #sum = 3**3 + (15 % 10) = 5 ** 3
    while temp:                            #    = 3**3 + 5**3
        sum = sum + (temp%10) ** 3          #temp = 15      15 // 10 = 1
        temp //= 10                         #sum = 3**3 + 5**5 + (1 % 10 ) = 1 ** 3
    if sum == i:                           #     = 3**3 + 5**5 + 1**3   while temp循环结束
        print(i,end=" ")

print(),print()

#有红、黄、绿三种颜色的球，其中红球3个，黄球3个，绿球6个。先将这12个球混合放在一个盒子中
#从中任意摸出8个球，编程计算摸出球的各种颜色搭配。
print('red\tyellow\tgreen')
for red in range(0, 4):
    for yellow in range(0, 4):
        #rang(2,7)是产生[2,3,4,5,6]这5个数，绿球不能是1个，因为如果是1个的话，红+黄需要有7个球才符合题意，所以这里绿球至少要有2个
        for green in range(2, 7):
            if red + yellow + green == 8:
                # 注意，下边不是字符串拼接，因此不用“+”哦~
                print(red, '\t', yellow, '\t', green)