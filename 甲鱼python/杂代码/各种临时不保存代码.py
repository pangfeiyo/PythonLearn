import random
secret = random.randint(1,10)
print(secret)
print('------------无双凌风工作室-------------')
temp = input("不妨猜猜凌风现在心里想的那个数：")

guess = int(temp)
while guess != secret:

    if guess > secret:
        print("dale")
        guess = int(input("不妨猜猜凌风现在心里想的那个数："))
    else:
        print("xiaole")
        guess = int(input("不妨猜猜凌风现在心里想的那个数："))
print("zhenghao")
