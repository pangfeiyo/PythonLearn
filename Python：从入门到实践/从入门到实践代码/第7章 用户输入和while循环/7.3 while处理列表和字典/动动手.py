# 动手试一试
# 7-8  熟食店 ：创建一个名为 sandwich_orders 的列表，在其中包含各种三明治的名字；再创建一个名为 finished_sandwiches 的空列表。
# 遍历列表 sandwich_orders ，对于其中的每种三明治，都打印一条消息，如 I made your tuna sandwich ，并将其移到列表 finished_sandwiches 。
# 所有三明治都制作好后，打印一条消息，将这些三明治列出来。
sandwich_orders = ['tudou','niurou','huotui','jidan']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your",current_sandwich,"sandwich.")
    finished_sandwiches.append(current_sandwich)
print("\nAll sandwichs"),print()
for sandwich in finished_sandwiches:
    print("I made a",sandwich ,"sandwich.")
print("……")

# 7-9  五香烟熏牛肉（ pastrami ）卖完了 ：
# 使用为完成练习 7-8 而创建的列表 sandwich_orders ，并确保 'pastrami' 在其中至少出现了三次。
# 在程序开头附近添加这样的代码：
# 打印一条消息，指出熟食店的五香烟熏牛肉卖完了；再使用一个 while 循环将列表 sandwich_orders 中的 'pastrami' 都删除。
# 确认最终的列表 finished_sandwiches 中不包含 'pastrami' 。
print("I'm sorry, but the spiced beef is sold out")
sandwich_orders = ['tudou', 'pastrami','pastrami','niurou', 'huotui', 'jidan','pastrami']
finished_sandwiches = []
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print()
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)
print()
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")

# 7-10  梦想的度假胜地 ：编写一个程序，调查用户梦想的度假胜地。
# 使用类似于 “If you could visit one place in the world, where would you go?” 的提示，并编写一个打印调查结果的代码块
name_prompt = "\nWhat your name?"
place_prompt = "If you could visit one place in the world, where would you go?"
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "
# Responses will be stored in the form {name: place}.
# 响应（字典）将以{name：place}的形式存储。
responses = {}
while True:
    # Ask the user where they'd like to go.    询问用户
    name = input(name_prompt)
    place = input(place_prompt)
    # Store the response.   存储在字典中
    responses[name] = place
    # Ask if there's anyone else responding.    询问有没有其他人要回答
    repeat = input(continue_prompt)
    if repeat.lower() == 'yes':
        break
# Show results of the survey.   显示调查结果
print("\n--- Result ---")
for name,place in responses.items():
    print(name.title(),"would like to visit",place.title(),".")