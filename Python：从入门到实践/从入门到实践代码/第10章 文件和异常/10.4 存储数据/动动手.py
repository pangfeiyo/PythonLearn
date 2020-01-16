import json
# 10-11  喜欢的数字 ：
# 编写一个程序，提示用户输入他喜欢的数字，并使用 json.dump() 将这个数字存储到文件中。
# 再编写一个程序，从文件中读取这个值，并打印消息 “I know your favorite number! It's _____.” 。
'''
filename = 'likenumber.json'
number = input("What's your like number?\nI like number is: ")
with open(filename,'w') as f:
    json.dump(number,f)

with open(filename) as f:
    pn = json.load(f)
print("I know your favorite number! it's : " + pn)
'''

# 10-12  记住喜欢的数字 ：将练习 10-11 中的两个程序合而为一。
# 如果存储了用户喜欢的数字，就向用户显示它，否则提示用户输入他喜欢的数字并将其存储到文件中。
# 运行这个程序两次，看看它是否像预期的那样工作。
'''
filename = 'likenumber.json'
try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("What's your like number?\nI like number is: ")
    with open(filename,'w') as f:
        json.dump(number, f)
    print("Thanks, I'll remember that.")
else:
    print("I know your favorite number! it's : " + number)
'''

# 10-13  验证用户 ：
# 最后一个 remember_me.py 版本假设用户要么已输入其用户名，要么是首次运行该程序。
# 我们应修改这个程序，以应对这样的情形：当前和最后一次运行该程序的用户并非同一个人。
# 为此，在 greet_user() 中打印欢迎用户回来的消息前，先询问他用户名是否是对的。
# 如果不对，就调用 get_new_username() 让用户输入正确的用户名。
filename = 'userinfo.json'
userinfo = []
def get_stored_username():
    """获取用户名"""
    try:
        with open(filename) as f:
            userinfo = json.load(f)
    except FileNotFoundError:
        None
    else:
        return userinfo
    
def get_new_username():
    """新用户登录"""
    username = input("Please tell me your name.\n")
    userinfo.append(username)
    usernumber = input("Please tell me your like number is:\n")
    userinfo.append(usernumber)
    with open(filename,'w') as f:
        json.dump(userinfo, f)
    

def get_user():
    userinfo = get_stored_username()
    if userinfo:
        correct = input("Are you " + userinfo[0] + " ? (y/n)\n")
        if correct == "y":
            print("Welcome back," + userinfo[0] + " !")
            print("You like number is : " + userinfo[1])
        else:
            get_new_username()
            userinfo = get_stored_username()
            print("New user name is : " + userinfo[0] + " !")
            print("You like number is : " + userinfo[1])
    else:
        get_new_username()
        print("We'll remember you when you come back, " + userinfo[0] + " !")
        print("You like number is : " + userinfo[1])

get_user()