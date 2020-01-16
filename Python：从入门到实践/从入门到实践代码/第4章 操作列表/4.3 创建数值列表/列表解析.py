#列表解析

#正常代码
squares= []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

#列表解析代码
# 要使用这种语法，首先指定一个描述性的列表名，如 squares ；然后，指定一个左方括号，并定义一个表达式，用于生成你要存储到列表中的值。在这个示例中，表达式
# 为 value**2 ，它计算平方值。接下来，编写一个 for 循环，用于给表达式提供值，再加上右方括号。在这个示例中， for 循环为 for value in range(1,11) ，它将值
# 1~10 提供给表达式 value**2 。请注意，这里的 for 语句末尾没有冒号。
squares = [value ** 2 for value in range(1,11)]
print(squares)