# 10.4 　存储数据
# 很多程序都要求用户输入某种信息，如让用户存储游戏首选项或提供要可视化的数据。
# 不管专注的是什么，程序都把用户提供的信息存储在列表和字典等数据结构中。
# 用户关闭程序时，你几乎总是要保存他们提供的信息；一种简单的方式是使用模块 json 来存储数据。
# 模块 json 让你能够将简单的 Python 数据结构转储到文件中，并在程序再次运行时加载该文件中的数据。
# 你还可以使用 json 在 Python 程序之间分享数据。
# 更重要的是， JSON 数据格式并非 Python 专用的，这让你能够将以 JSON 格式存储的数据与使用其他编程语言的人分享。
# 这是一种轻便格式，很有用，也易于学习。
# 注意 　 JSON （ JavaScript Object Notation ）格式最初是为 JavaScript 开发的，但随后成了一种常见格式，被包括 Python 在内的众多语言采用。



# 10.4.1 　使用 json.dump()  和 json.load()
# 我们来编写一个存储一组数字的简短程序，再编写一个将这些数字读取到内存中的程序。
# 第一个程序将使用 json.dump() 来存储这组数字，而第二个程序将使用 json.load() 。
# 函数 json.dump() 接受两个实参：要存储的数据以及可用于存储数据的文件对象。
# 下面演示了如何使用 json.dump() 来存储数字列表：
import json

numbers = [2,3,5,7,11,13]
filename = 'numbers.json'   # ⑤
with open(filename,'w') as f_obj:   # ②
    json.dump(numbers, f_obj)   # ③ 
# 我们先导入模块 json ，再创建一个数字列表。
# 在❶处，我们指定了要将该数字列表存储到其中的文件的名称。通常使用文件扩展名 .json 来指出文件存储的数据为 JSON 格式。
# 接下来，我们以写入模式打开这个文件，让 json 能够将数据写入其中（见❷）。
# 在❸处，我们使用函数 json.dump() 将数字列表存储到文件 numbers.json 中。

# 下面再编写一个程序，使用 json.load() 将这个列表读取到内存中：
numbers2 = []
print(numbers2)
with open(filename) as f_obj:
    numbers2 = json.load(f_obj)
print(numbers2)