# 7-4  比萨配料 ：编写一个循环，提示用户输入一系列的比萨配料，并在用户输入 'quit' 时结束循环。
# 每当用户输入一种配料后，都打印一条消息，说我们会在比萨中添加这种配料。
exit = True
pizza = []
while exit:
    mixed_ingredients = input("请输入披萨配料：")
    if mixed_ingredients != 'quit':
        pizza.append(mixed_ingredients)
        print("已有配料：")
        print("\t"+ str(pizza))
        continue
    else:
        break


# 7-5  电影票 ：有家电影院根据观众的年龄收取不同的票价：不到 3 岁的观众免费；
# 3~12 岁的观众为 10 美元；超过 12 岁的观众为 15 美元。请编写一个循环，在其中询问用户的年龄，并指出其票价。
piaojia = 0
while True:
    age = input("请输入年龄：")
    # .isdigit()  如果全是数字返回True
    while not age.isdigit():
        age = input("请输入数字：")

    age = int(age)

    if age < 3:
        print("票价为：", piaojia, "元")
    elif 3 <= age <= 12:
        piaojia = 10
        print("票价为：", piaojia, "元")
    elif age > 12:
        piaojia = 15
        print("票价为：", piaojia, "元")


# 7-6  三个出口 ：以另一种方式完成练习 7-4 或练习 7-5 ，在程序中采取如下所有做法。
# 在 while 循环中使用条件测试来结束循环。
# 使用变量 active 来控制循环结束的时机。
# 使用 break 语句在用户输入 'quit' 时退出循环。
piaojia = 0
active = True
while active:
    age = input("请输入年龄：")
    if age == 'quit':
        active = False
        break
    # .isdigit()  如果全是数字返回True
    while not age.isdigit():
        age = input("请输入数字：")
    age = int(age)
    if age < 3:
        print("票价为：", piaojia, "元")
    elif 3 <= age <= 12:
        piaojia = 10
        print("票价为：", piaojia, "元")
    elif age > 12:
        piaojia = 15
        print("票价为：", piaojia, "元")

# 7-7  无限循环 ：编写一个没完没了的循环，并运行它（要结束该循环，可按 Ctrl +C ，也可关闭显示输出的窗口）。
# num = 1
# while True:
#     num += 1
#     print(num)