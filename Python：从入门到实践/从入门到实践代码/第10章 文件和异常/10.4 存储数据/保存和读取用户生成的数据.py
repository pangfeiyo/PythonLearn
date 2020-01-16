# 10.4.2 　保存和读取用户生成的数据
# 对于用户生成的数据，使用 json 保存它们大有裨益，因为如果不以某种方式进行存储，等程序停止运行时用户的信息将丢失。
# 下面来看一个这样的例子：
# 用户首次运行程序时被提示输入自己的名字，这样再次运行程序时就记住他了。
# 我们先来存储用户的名字：
import json
'''
username = input("what is your name?\n")
filename = 'username.json'
with open(filename,'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")
'''

# 现在再编写一个程序，向其名字被存储的用户发出问候：
'''
with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username)
'''


# 我们需要将这两个程序合并到一个程序（ remember_me.py ）中。
# 这个程序运行时，我们将尝试从文件 username.json 中获取用户名，
# 因此我们首先编写一个尝试恢复用户名的 try 代码块。
# 如果这个文件不存在，我们就在 except 代码块中提示用户输入用户名，
# 并将其存储在 username.json 中，以便程序再次运行时能够获取它：
'''
如果以前存储了用户名，就加载它
  否则，就提示用户输入用户名并存储它
'''
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What's your name?\n")
    with open(filename,'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print('Welcome back, ' + username + "!")