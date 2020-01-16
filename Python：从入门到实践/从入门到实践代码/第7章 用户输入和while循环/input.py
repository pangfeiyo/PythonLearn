# message = input("Tell me something, and i will repeat it back to your:")
# print(message)


# 动手试一试
# 7-1  汽车租赁 ：编写一个程序，询问用户要租赁什么样的汽车，并打印一条消息，如 “Let me see if I can find you a Subaru” 。
print("What kind of car do you want to rent?")
automobile = input("I want to :")
print("Let me see if i can find you a Subaru")

# 7-2  餐馆订位 ：编写一个程序，询问用户有多少人用餐。如果超过 8 人，就打印一条消息，指出没有空桌；否则指出有空桌。
print("How many people are there for dinner?")
people = input("I think we have:")
if int(people) > 8:
    print("Sorry, we don't have an empty table")
else:
    print("Welcome!")

# 7-3 10 的整数倍 ：让用户输入一个数字，并指出这个数字是否是 10 的整数倍。
input = input("请输入一个数：")
if int(input) % 10 == 0:
    print("这是10的整数倍")
else:
    print("这不是10的整数倍")
