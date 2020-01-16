'''
10.1 　从文件中读取数据
文本文件可存储的数据量多得难以置信：天气数据、交通数据、社会经济数据、文学作品等。
每当需要分析或修改存储在文件中的信息时，读取文件都很有用，对数据分析应用程序来说尤其如此。
例如，你可以编写一个这样的程序：读取一个文本文件的内容，重新设置这些数据的格式并将其写入文件，让浏览器能够显示这些内容。
要使用文本文件中的信息，首先需要将信息读取到内存中。为此，你可以一次性读取文件的全部内容，也可以以每次一行的方式逐步读取。

10.1.1 　读取整个文件
要读取文件，需要一个包含几行文本的文件。下面首先来创建一个文件，它包含精确到小数点后 30 位的圆周率值，且在小数点后每 10 位处都换行：
'''
# 下面的程序打开并读取这个文件，再将其内容显示到屏幕上：
# 关键字 with 在不再需要访问文件后将其关闭
with open("pi_digits.txt") as file_object:
    contents = file_object.read()
    print(contents)

# 相比于原始文件，该输出唯一不同的地方是末尾多了一个空行。
# 为何会多出这个空行呢？因为 read() 到达文件末尾时返回一个空字符串，
# 而将这个空字符串显示出来时就是一个空行。
# 要删除多出来的空行，可在 print 语句中使用 rstrip() ：
'''retrip 指定删除的字符（默认为空格）'''
with open("pi_digits.txt") as file_object:
    contents = file_object.read()
    print(contents.rstrip())



'''
10.1.2 　文件路径
当你将类似 pi_digits.txt 这样的简单文件名传递给函数 open() 时， Python 将在当前执行的文件（即 .py 程序文件）所在的目录中查找文件。
根据你组织文件的方式，有时可能要打开不在程序文件所属目录中的文件。
例如，你可能将程序文件存储在了文件夹 python_work 中，
而在文件夹 python_work 中，有一个名为text_files 的文件夹，用于存储程序文件操作的文本文件。
虽然文件夹 text_files 包含在文件夹 python_work 中，但仅向 open() 传递位于该文件夹中的文件的名称也不可行，
因为 Python只在文件夹 python_work 中查找，而不会在其子文件夹 text_files 中查找。
要让 Python 打开不与程序文件位于同一个目录中的文件，需要提供 文件路径 ，它让 Python 到系统的特定位置去查找。
由于文件夹 text_files 位于文件夹 python_work 中，因此可使用 相对文件路 径来打开该文件夹中的文件。
相对文件路径让 Python 到指定的位置去查找，而该位置是相对于当前运行的程序所在目录的。

在 Linux 和 OS X 中，你可以这样编写代码：
with open('text_files/filename.txt') as file_object:
这行代码让 Python 到文件夹 python_work 下的文件夹 text_files 中去查找指定的 .txt 文件。

在 Windows 系统中，在文件路径中使用反斜杠（ \ ）而不是斜杠（ / ）：
with open('text_files\filename.txt') as file_object:  
'''


# 你还可以将文件在计算机中的准确位置告诉 Python ，这样就不用关心当前运行的程序存储在什么地方了。
# 这称为 绝对文件路径 。在相对路径行不通时，可使用绝对路径。例如，
# 如果 text_files 并不在文件夹 python_work 中，而在文件夹 other_files 中，
# 则向 open() 传递路径 'text_files/ filename.txt' 行不通，因为 Python 只在文件夹 python_work 中查找该位置。
# 为明确地指出你希望 Python 到哪里去查找，你需要提供完整的路径。
# 绝对路径通常比相对路径更长，因此将其存储在一个变量中，再将该变量传递给 open() 会有所帮助。
# 在 Linux 和 OS X 中，绝对路径类似于下面这样：
# file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
# with open(file_path) as file_object:
# 而在 Windows 系统中，它们类似于下面这样：
# file_path = 'C:\Users\ehmatthes\other_files\text_files\filename.txt'
# with open(file_path) as file_object:
# 通过使用绝对路径，可读取系统任何地方的文件。
# 就目前而言，最简单的做法是，要么将数据文件存储在程序文件所在的目录，
# 要么将其存储在程序文件所在目录下的一个文件夹（如 text_files ）中。
# 注意 　 Windows 系统有时能够正确地解读文件路径中的斜杠。
# 如果你使用的是 Windows 系统，且结果不符合预期，请确保在文件路径中使用的是反斜杠。

print("\n-- 10.1.3 逐行读取 --")
'''
10.1.3 　逐行读取
读取文件时，常常需要检查其中的每一行：
你可能要在文件中查找特定的信息，或者要以某种方式修改文件中的文本。
例如，你可能要遍历一个包含天气数据的文件，并使用天气描述中包含字样 sunny 的行。
在新闻报道中，你可能会查找包含标签 <headline> 的行，并按特定的格式设置它。
要以每次一行的方式检查文件，可对文件对象使用 for 循环：
'''
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)
# 我们打印每一行时，发现空白行更多了
# 为何会出现这些空白行呢？因为在这个文件中，每行的末尾都有一个看不见的换行符，
# 而 print 语句也会加上一个换行符，因此每行末尾都有两个换行符：
# 一个来自文件，另一个来自 print 语句。
# 要消除这些多余的空白行，可在 print 语句中使用 rstrip() ：
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())



print("\n-- 10.1.4 --")
'''
10.1.4 　创建一个包含文件各行内容的列表
使用关键字 with 时， open() 返回的文件对象只在 with 代码块内可用。
如果要在 with 代码块外访问文件的内容，可在 with 代码块内将文件的各行存储在一个列表中，
并在 with 代码块外使用该列表：你可以立即处理文件的各个部分，也可推迟到程序后面再处理。
下面的示例在 with 代码块中将文件 pi_digits.txt 的各行存储在一个列表中，再在 with 代码块外打印它们：
'''
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())




print("\n-- 10.1.5 使用文件的内容 --")
'''
10.1.5 　使用文件的内容
将文件读取到内存中后，就可以以任何方式使用这些数据了。
下面以简单的方式使用圆周率的值。
首先，我们将创建一个字符串，它包含文件中存储的所有数字，且没有任何空格：
'''
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ""
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))
'''在变量 pi_string 存储的字符串中，包含原来位于每行左边的空格，为删除这些空格，可使用 strip() 而不是 rstrip() ：'''
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ""
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))


# 注意 　读取文本文件时， Python 将其中的所有文本都解读为字符串。
# 如果你读取的是数字，并要将其作为数值使用，就必须使用函数 int() 将其转换为整数，
# 或使用函数 float() 将其转换为浮点数。


print("\n--10.1.6 --")
'''
10.1.6 　包含一百万位的大型文件
前面我们分析的都是一个只有三行的文本文件，但这些代码示例也可处理大得多的文件。
如果我们有一个文本文件，其中包含精确到小数点后 1 000 000 位而不是 30 位的圆周率值，
也可创建一个包含所有这些数字的字符串。
为此，我们无需对前面的程序做任何修改，只需将这个文件传递给它即可。
在这里，我们只打印到小数点后 50 位，以免终端为显示全部 1 000 000 位而不断地翻滚：
'''
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string[:52] + "...")
print(len(pi_string))



print("\n-- 10.1.7 --")
'''
10.1.7 　圆周率值中包含你的生日吗
我一直想知道自己的生日是否包含在圆周率值中。
下面来扩展刚才编写的程序，以确定某个人的生日是否包含在圆周率值的前 1 000 000 位中。
为此，可将生日表示为一个由数字组成的字符串，再检查这个字符串是否包含在 pi_string 中：
'''
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ""
for line in lines:
    pi_string += line.rstrip()
birthday = input("Enter your birthday, in the from mmddyy:")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
