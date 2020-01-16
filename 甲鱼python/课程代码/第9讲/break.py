bingo="小甲鱼"
answer = input("请输入一句话：")

while True:
    if answer == bingo:
        break
    answer = input("抱歉，错了，请重新输入：")

print("哎哟，帅哦~")
print("猜的真对")
