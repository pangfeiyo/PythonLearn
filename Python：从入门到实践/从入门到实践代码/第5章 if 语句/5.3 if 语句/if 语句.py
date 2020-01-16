# 假设有一个表示某人年龄的变量，而你想知道这个人是否够投票的年龄，可使用如下代码：
age = 19
if age >= 18:
    print('You are old enough to vote!')

age = 19
if age >= 18:
    print("\nYou are old enough to vote!")
    print("Have you registered to vote yet?")


# 5.3.2 　 if-else  语句
# 经常需要在条件测试通过了时执行一个操作，并在没有通过时执行另一个操作；
# 在这种情况下，可使用 Python 提供的 if-else 语句。
# if-else 语句块类似于简单的 if 语句，但其中的 else 语句让你能够指定条件测试未通过时要执行的操作。
# 下面的代码在一个人够投票的年龄时显示与前面相同的消息，同时在这个人不够投票的年龄时也显示一条消息：
age = 17
if age >= 18:
    print("\nYou are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("\nSorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")


# 5.3.3 　 if-elif-else  结构
# 经常需要检查超过两个的情形，为此可使用 Python 提供的 if-elif-else 结构。
# Python 只执行 if-elif-else 结构中的一个代码块，它依次检查每个条件测试，直到遇到通过了的条件测试。
# 测试通过后， Python 将执行紧跟在它后面的代码，并跳过余下的测试。
# 在现实世界中，很多情况下需要考虑的情形都超过两个。例如，来看一个根据年龄段收费的游乐场：
# 4 岁以下免费；
# 4~18 岁收费 5 美元；
# 18 岁（含）以上收费 10 美元。
age =  12
if age <4 :
    print('免费')
elif 4 <= age <= 18:
    print('5元')
else:
    print('10元')
# 为让代码更简洁，可不在 if-elif-else 代码块中打印门票价格，而只在其中设置门票价格，并在它后面添加一条简单的 print 语句：
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")
# 这些代码的输出与前一个示例相同，但 if-elif-else 结构的作用更小，它只确定门票价格，而不是在确定门票价格的同时打印一条消息。
# 除效率更高外，这些修订后的代码还更容易修改：要调整输出消息的内容，只需修改一条而不是三条 print 语句。


# 5.3.4 　使用多个 elif  代码块
# 可根据需要使用任意数量的 elif 代码块，例如，假设前述游乐场要给老年人打折，可再添加一个条件测试，判断顾客是否符合打折条件。
# 下面假设对于 65 岁（含）以上的老人，可以半价（即 5 美元）购买门票：
age = 12
if age <4:
    price =0
elif age < 18:
    price =5
elif age < 65:
    price = 10
else:
    price = 5
print("You admission cost is $" + str(price) + ".")


# 5.3.5 　省略 else  代码块
# Python 并不要求 if-elif 结构后面必须有 else 代码块。
# 在有些情况下， else 代码块很有用；而在其他一些情况下，使用一条 elif 语句来处理特定的情形更清晰：
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:   # ❶
    price = 5
print("You admission cost is $" + str(price) + ".")
# ❶处的 elif 代码块在顾客的年龄超过 65 （含）时，将价格设置为 5 美元，这比使用 else 代码块更清晰些。
# 经过这样的修改后，每个代码块都仅在通过了相应的测试时才会执行。
# else 是一条包罗万象的语句，只要不满足任何 if 或 elif 中的条件测试，其中的代码就会执行，这可能会引入无效甚至恶意的数据。
# 如果知道最终要测试的条件，应考虑使用一个 elif 代码块来代替 else 代码块。
# 这样，你就可以肯定，仅当满足相应的条件时，你的代码才会执行。

print()

# 5.3.6 　测试多个条件
# if-elif-else 结构功能强大，但仅适合用于只有一个条件满足的情况：
# 遇到通过了的测试后， Python 就跳过余下的测试。这种行为很好，效率很高，让你能够测试一个特定的条件。
# 然而，有时候必须检查你关心的所有条件。在这种情况下，应使用一系列不包含 elif 和 else 代码块的简单 if 语句。
# 在可能有多个条件为 True ，且你需要在每个条件为 True时都采取相应措施时，适合使用这种方法。
# 下面再来看前面的比萨店示例。如果顾客点了两种配料，就需要确保在其比萨中包含这些配料：
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("Finished making your pizza!")