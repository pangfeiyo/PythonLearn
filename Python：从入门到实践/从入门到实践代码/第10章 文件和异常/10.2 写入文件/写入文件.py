# 10.2.1 　写入空文件
# 要将文本写入文件，你在调用 open() 时需要提供另一个实参，告诉 Python 你要写入打开的文件。
# 为明白其中的工作原理，我们来将一条简单的消息存储到文件中，而不是将其打=印到屏幕上：

filename = 'programing.txt'
with open(filename,'w') as file_object: # ①
    file_object.write("I love programing.") # ②
'''
在这个示例中，调用 open() 时提供了两个实参（见❶）。
第一个实参也是要打开的文件的名称；第二个实参（ 'w' ）告诉 Python ，我们要以 写入模式 打开这个文件。
打开文件时，可指定 读取模式 （ 'r' ）、 写入模式 （ 'w' ）、 附加模式 （ 'a' ）
或让你能够读取和写入文件的模式（ 'r+' ）。
如果你省略了模式实参， Python 将以默认的只读模式打开文件。
如果你要写入的文件不存在，函数 open() 将自动创建它。
然而，以写入（ 'w' ）模式打开文件时千万要小心，因为如果指定的文件已经存在， Python 将在返回文件对象前清空该文件。
在❷处，我们使用文件对象的方法 write() 将一个字符串写入文件。
这个程序没有终端输出，但如果你打开文件 programming.txt ，将看到其中包含如下一行内容：
I love programming.
'''
# 注意 　
#  Python 只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数 str() 将其转换为字符串格式。




# 写入多行
# 函数 write() 不会在你写入的文本末尾添加换行符，因此如果你写入多行时没有指定换行符，文件看起来可能不是你希望的那样：
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")

# 要让每个字符串都单独占一行，需要在 write() 语句中包含换行符：
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
# 像显示到终端的输出一样，还可以使用空格、制表符和空行来设置这些输出的格式。



# 10.2.3 　附加到文件
# 如果你要给文件添加内容，而不是覆盖原有的内容，可以 附加模式 打开文件。
# 你以附加模式打开文件时， Python 不会在返回文件对象前清空文件，而你写入到文件的行都将添加到文件末尾。
# 如果指定的文件不存在， Python 将为你创建一个空文件。
# 下面来修改 write_message.py ，在既有文件 programming.txt 中再添加一些你酷爱编程的原因：
filename = 'programming.txt'
with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")