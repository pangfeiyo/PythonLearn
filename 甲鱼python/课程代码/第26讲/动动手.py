#尝试编写一个用户登录程序（这次尝试将功能封闭成函数）
user_data = {}

def new_user():
    '''注册'''
    prompt = "请输入用户名："
    while True:
        name = input(prompt)
        if name == 'quit':
            showmenu()
        if name in user_data:
            prompt = "该用户名已存在，请重新输入："
            continue
        else:
            break
    passwd = input("请输入密码：")
    user_data[name] = passwd
    print("注册成功，赶紧谢谢登录吧！")

def old_user():
    '''登录'''
    prompt = "请输入用户名："
    while True:
        name = input(prompt)
        if name == 'quit':
            showmenu()
        if name not in user_data:
            prompt = '您输入的用户名不存在，请重新输入：'
            continue
        else:
            break
    passwd = input("请输入密码：")
    pwd = user_data.get(name)
    if passwd == pwd:
        print("欢迎进入xxoo系统，请点击右上角的X结束程序！")
    else:
        print("密码错误！")

def showmenu():
    prompt = '''|--- 新建用户：N/n ---|
|--- 登录帐户：E/e ---|
|--- 退出程序：Q/q ---|
|--- 请输入指令代码：'''
    while True:
        chosen = False
        while not chosen:
            choice = input(prompt)
            if choice == "quit":
                showmenu()
            if choice not in "NnEeQq":
                print("您输入的指令代码有误，请重新输入：")
            else:
                chosen = True

        if choice == 'q' or choice == 'Q':
             break
        if choice == 'n' or choice == 'N':
             new_user()
        if choice == 'e' or choice == 'E':
             old_user()

showmenu()