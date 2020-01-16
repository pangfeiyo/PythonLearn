print("-- 10.3.5 --")
# 10.3.5 　处理 FileNotFoundError  异常
# 使用文件时，一种常见的问题是找不到文件：
# 你要查找的文件可能在其他地方、文件名可能不正确或者这个文件根本就不存在。
# 对于所有这些情形，都可使用 try-except 代码块以直观的方式进行处理。
# 我们来尝试读取一个不存在的文件。
# 下面的程序尝试读取文件 alice.txt 的内容，但我没有将这个文件存储在 alice.py 所在的目录中：
'''
filename = 'alice.txt'
with open(filename) as f_obj:
    contents = f_obj.read()
'''
# Python 无法读取不存在的文件，因此它引发一个异常：
# FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'

# 在上述 traceback 中，最后一行报告了 FileNotFoundError 异常，这是 Python 找不到要打开的文件时创建的异常。
# 在这个示例中，这个错误是函数 open() 导致的，因此要处理这个错误，必须将 try 语句放在包含 open() 的代码行之前：
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename +" does not exist."
    print(msg)
# 如果文件不存在，这个程序什么都不做，因此错误处理代码的意义不大。
# 下面来扩展这个示例，看看在你使用多个文件时，异常处理可提供什么样的帮助。


print("\n-- 10.3.6 --")
# 10.3.6 　分析文本
# 你可以分析包含整本书的文本文件。
# 很多经典文学作品都是以简单文本文件的方式提供的，因为它们不受版权限制。
# 本节使用的文本来自项目 Gutenberg （ http://gutenberg.org/  ），
# 这个项目提供了一系列不受版权限制的文学作品，如果你要在编程项目中使用文学文本，这是一个很不错的资源。
# 下面来提取童话 Alice in Wonderland  的文本，并尝试计算它包含多少个单词。
# 我们将使用方法 split() ，它根据一个字符串创建一个单词列表。
# 下面是对只包含童话名 "Alice in Wonderland" 的字符串调用方法 split() 的结果：
title = 'Alice in Wonderland'
print(title.split())
# 方法 split() 以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储到一个列表中。
# 结果是一个包含字符串中所有单词的列表，虽然有些单词可能包含标点。
# 为计算Alice in Wonderland  包含多少个单词，我们将对整篇小说调用 split() ，再计算得到的列表包含多少个元素，从而确定整篇童话大致包含多少个单词：

filename = "Alice in Wonderland.txt"
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # 计算文件大概包含多少个单词
    words = contents.split()    # ①
    num_words = len(words)  # ②
    print("The file " + filename + " has about " + str(num_words) + " words.")  # ③
# 我们把文件 alice.txt 移到了正确的目录中，让 try 代码块能够成功地执行。
# 在❶处，我们对变量 contents 
# （它现在是一个长长的字符串，包含童话 Alice in Wonderland  的全部文本）调用方法 split() ，以生成一个列表，其中包含这部童话中的所有单词。
# 当我们使用 len() 来确定这个列表的长度时，就知道了原始字符串大致包含多少个单词（见❷）。
# 在❸处，我们打印一条消息，指出文件包含多少个单词。
# 这些代码都放在 else 代码块中，因为仅当 try 代码块成功执行时才执行它们。
# 输出指出了文件 alice.txt 包含多少个单词
# 这个数字有点大，因为这里使用的文本文件包含出版商提供的额外信息，但与童话 Alice in Wonderland  的长度相当一致。





print("\n-- 10.3.7 --")
# 10.3.7 　使用多个文件
# 下面多分析几本书。
# 这样做之前，我们先将这个程序的大部分代码移到一个名为 count_words() 的函数中，这样对多本书进行分析时将更容易：
def count_words(filename):
    '''计算一个文件大概包含多少个单词'''
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        #计算文件大概包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about" + str(num_words) + " words.")
filename = "alice.txt"
count_words(filename)
# 现在可以编写一个简单的循环，计算要分析的任何文本包含多少个单词了。
# 为此，我们将要分析的文件的名称存储在一个列表中，然后对列表中的每个文件都调用 count_words() 。
# 我们将尝试计算 Alice in Wonderland  、 Siddhartha  、 Moby Dick  和 Little Women  分别包含多少个单词，它们都不受版权限制。
# 我故意没有将 siddhartha.txt 放到word_count.py 所在的目录中，让你能够看到这个程序在文件不存在时处理得有多出色：
print()
filenames = ['Alice in Wonderland.txt','Little Women.txt','Moby Dick.txt','Siddhartha.txt']
for filename in filenames:
    count_words(filename)

            

print("\n-- 10.3.8 --")
# 10.3.8 　失败时一声不吭
# 在前一个示例中，我们告诉用户有一个文件找不到。
# 但并非每次捕获到异常时都需要告诉用户，有时候你希望程序在发生异常时一声不吭，就像什么都没有发生一样继续运行。
# 要让程序在失败时一声不吭，可像通常那样编写 try 代码块，但在 except 代码块中明确地告诉 Python 什么都不要做。 
# Python 有一个 pass 语句，可在代码块中使用它来让 Python什么都不要做：
def count_words(filename):
    '''计算一个文件大概包含多少个单词'''
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        #计算文件大概包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about" + str(num_words) + " words.")
filenames = ['Alice in Wonderland.txt','Little Women.txt','Moby Dick.txt','Siddhartha.txt']
for filename in filenames:
    count_words(filename)

