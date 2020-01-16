# 10-6  加法运算 ：
# 提示用户提供数值输入时，常出现的一个问题是，用户提供的是文本而不是数字。
# 在这种情况下，当你尝试将输入转换为整数时，将引发 TypeError 异常。
# 编写一个程序，提示用户输入两个数字，再将它们相加并打印结果。
# 在用户输入的任何一个值不是数字时都捕获 TypeError 异常，并打印一条友好的错误消息。
# 对你编写的程序进行测试：先输入两个数字，再输入一些文本而不是数字。
'''
while True:
    try:
        x = input("Give me a number;")
        if x == 'quit':
            print("Thinks")
            break
        else:
            x = int(x)

        y = input("Give me another number:")
        if y == 'quit':
            print("Thinks")
            break
        else:
            y = int(y)
    except ValueError:
        print("Soory, I really needed a number.")
    else:
            sum = x + y
            print("The sum of " + str(x) + " and " + str(y) + " is " + str(sum) + ".")
            '''


# 10-7  加法计算器 ：
# 将你为完成练习 10-6 而编写的代码放在一个 while 循环中，让用户犯错（输入的是文本而不是数字）后能够继续输入数字。
'''上面已经有了'''



# 10-8  猫和狗 ：
# 创建两个文件 cats.txt 和 dogs.txt ，
# 在第一个文件中至少存储三只猫的名字，在第二个文件中至少存储三条狗的名字。
# 编写一个程序，尝试读取这些文件，并将其内容打印到屏幕上。
# 将这些代码放在一个 try-except 代码块中，以便在文件不存在时捕获 FileNotFound 错误，并打印一条友好的消息。
# 将其中一个文件移到另一个地方，并确认 except 代码块中的代码将正确地执行。
filenames = ['cats.txt','dogs.txt','fishs.txt']
for filename in filenames:
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
            msg = ("The " + filename + ".txt : \n" + contents)
            print(msg)
    except:
        print("  Sorry, I can't find " + filename)
        


# 10-9  沉默的猫和狗 ：修改你在练习 10-8 中编写的 except 代码块，让程序在文件不存在时一言不发。
print("\n-- 10-9 --")
filenames = ['cats.txt','dogs.txt','fishs.txt']
for filename in filenames:
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
            msg = ("The " + filename + ".txt : \n" + contents)
            print(msg)
    except:
        pass



# 10-10  常见单词 ：
# 访问项目 Gutenberg （ http://gutenberg.org/  ），并找一些你想分析的图书。
# 下载这些作品的文本文件或将浏览器中的原始文本复制到文本文件中。
# 你可以使用方法 count() 来确定特定的单词或短语在字符串中出现了多少次。
# 例如，下面的代码计算 'row' 在一个字符串中出现了多少次：
'''
>>> line = 'Row, row, row your boat'
>>> line.count('row')
2
>>> line.lower().count('row')
3
'''
print("\n-- 10-10 --")
filenames = ['Alice in Wonderland.txt','Little Women.txt','Moby Dick.txt','Siddhartha.txt']
findtxt = 'and'
count_list = []
count_number = 0
try:
    for filename in filenames:
        with open(filename) as f_obj:
            contents = f_obj.read()
            count = contents.count(findtxt)
            count_list.append(count)
except FileNotFoundError:
    print("No find that txt:" + filename)
    filenames.remove(filename)
    print()
for filename in filenames:
    print("In "+ filename + " have " + findtxt + " number is : " + str(count_list[count_number]))
    count_number += 1
