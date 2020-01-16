# 10-1 Python 学习笔记 ：
# 在文本编辑器中新建一个文件，写几句话来总结一下你至此学到的 Python 知识，
# 其中每一行都以 “In Python you can” 打头。
# 将这个文件命名为learning_python.txt ，并将其存储到为完成本章练习而编写的程序所在的目录中。
# 编写一个程序，它读取这个文件，并将你所写的内容打印三次：
# 第一次打印时读取整个文件；
# 第二次打印时遍历文件对象；
# 第三次打印时将各行存储在一个列表中，再在 with 代码块外打印它们。
filename = 'learning_python.txt'
print("--- Reading in the entire file:")
with open(filename) as f:
    contents = f.read()
print(contents)

print("\n--- Looping over the lines:")
with open(filename) as f:
    for line in f:
        print(line.rstrip())

print("\n--- Storing the lines in a list;")
with open(filename) as f:
    lines = f.readlines()
for line in lines:
    print(line.rstrip())



print("\n\n")
# 10-2 C 语言学习笔记 ：可使用方法 replace() 将字符串中的特定单词都替换为另一个单词。
# 下面是一个简单的示例，演示了如何将句子中的 'dog' 替换为 'cat':
message = "I really like dogs."
message = message.replace('dog','cat')
print(message)
# 读取你刚创建的文件 learning_python.txt 中的每一行，将其中的 Python 都替换为另一门语言的名称，如 C 。
# 将修改后的各行都打印到屏幕上。
filename = 'learning_python.txt'
with open(filename) as f:
    lines = f.readlines()
for line in lines:
    line = line.rstrip()
    line = line.replace('Python','C')
    print(line)
