# 10.4.3 　重构
# 你经常会遇到这样的情况：
# 代码能够正确地运行，但可做进一步的改进 
# —— 将代码划分为一系列完成具体工作的函数。
# 这样的过程被称为 重构 。重构让代码更清晰、更易于理解、更容易扩展。
# 要重构 remember_me.py（保存和读取用户生成的数据） ，可将其大部分逻辑放到一个或多个函数中。 
# remember_me.py 的重点是问候用户，因此我们将其所有代码都放到一个名为 greet_user() 的函数中：
import json
'''
def greet_user():
    """问候用户，并指出其名字"""
    filename = "username.json"
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What's your name?\n")
        with open(filename,'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")

greet_user()
'''

# 这个程序更清晰些，但函数 greet_user() 所做的不仅仅是问候用户，
# 还在存储了用户名时获取它，而在没有存储用户名时提示用户输入一个。
# 下面来重构 greet_user() ，让它不执行这么多任务。
# 为此，我们首先将获取存储的用户名的代码移到另一个函数中：
'''
def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    """问候用户，并指出其姓名"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = input("What's your name?\n")
        filename = 'username.json'
        with open(filename,'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")

greet_user()
'''

# 我们还需将 greet_user() 中的另一个代码块提取出来：将没有存储用户名时提示用户输入的代码放在一个独立的函数中：
def get_stored_username():
    '''如果存储了用户名，就获取它'''
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    username = input("What's your name?\n")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    '''问候用户，并指出其姓名'''
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()