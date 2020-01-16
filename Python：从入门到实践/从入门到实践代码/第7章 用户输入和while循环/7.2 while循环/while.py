# 7.2 　 while 循环简介
# for 循环用于针对集合中的每个元素都一个代码块，而 while 循环不断地运行，直到指定的条件不满足为止。
#
# 7.2.1 　使用 while  循环
# 你可以使用 while 循环来数数，例如，下面的 while 循环从 1 数到 5 ：
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


# 7.2.2 　让用户选择何时退出
# 可使用 while 循环让程序在用户愿意时不断地运行，如下面的程序 parrot.py 所示。
# 我们在其中定义了一个退出值，只要用户输入的不是这个值，程序就接着运行：
prompt = "\nTell me something, and i will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
# 这个程序很好，唯一美中不足的是，它将单词 'quit' 也作为一条消息打印了出来。为修复这种问题，只需使用一个简单的 if 测试：
    if message != 'quit':
        print(message)



# 7.2.3 　使用标志
# 在前一个示例中，我们让程序在满足指定条件时就执行特定的任务。但在更复杂的程序中，很多不同的事件都会导致程序停止运行；在这种情况下，该怎么办呢？
# 例如，在游戏中，多种事件都可能导致游戏结束，如玩家一艘飞船都没有了或要保护的城市都被摧毁了。导致程序结束的事件有很多时，如果在一条 while 语句中检查所有这些
# 条件，将既复杂又困难。
# 在要求很多条件都满足才继续运行的程序中，可定义一个变量，用于判断整个程序是否处于活动状态。这个变量被称为 标志 ，充当了程序的交通信号灯。你可让程序在标志
# 为 True 时继续运行，并在任何事件导致标志的值为 False 时让程序停止运行。这样，在 while 语句中就只需检查一个条件 —— 标志的当前值是否为 True ，并将所有测试（是
# 否发生了应将标志设置为 False 的事件）都放在其他地方，从而让程序变得更为整洁。
# 下面来在前一节的程序 parrot.py 中添加一个标志。我们把这个标志命名为 active （可给它指定任何名称），它将用于判断程序是否应继续运行：
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    if message == "quit":
        active = False
    else:
        print(message)


# 7.2.4 　使用 break  退出循环
# 要立即退出 while 循环，不再运行循环中余下的代码，也不管条件测试的结果如何，可使用 break 语句。
# break 语句用于控制程序流程，可使用它来控制哪些代码行将执行，哪些代码行不执行，从而让程序按你的要求执行你要执行的代码。
# 例如，来看一个让用户指出他到过哪些地方的程序。在这个程序中，我们可以在用户输入 'quit' 后使用 break 语句立即退出 while 循环：
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

# 7.2.5 　在循环中使用 continue
# 要返回到循环开头，并根据条件测试结果决定是否继续执行循环，可使用 continue 语句，它不像 break 语句那样不再执行余下的代码并退出整个循环。
# 例如，来看一个从 1 数到 10 ，但只打印其中偶数的循环：
current_number = 0
while current_number < 11:
    current_number += 1
    if current_number % 2 != 0:
        continue
    print(current_number)


