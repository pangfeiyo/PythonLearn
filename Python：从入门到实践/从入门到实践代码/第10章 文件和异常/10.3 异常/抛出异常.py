'''
10.3 　异常
Python 使用被称为 异常 的特殊对象来管理程序执行期间发生的错误。
每当发生让 Python 不知所措的错误时，它都会创建一个异常对象。
如果你编写了处理该异常的代码，程序将继续运行；
如果你未对异常进行处理，程序将停止，并显示一个 traceback ，其中包含有关异常的报告。
异常是使用 try-except 代码块处理的。
try-except 代码块让 Python 执行指定的操作，同时告诉 Python 发生异常时怎么办。
使用了 try-except 代码块时，即便出现异常，程序也将继续运行：
显示你编写的友好的错误消息，而不是令用户迷惑的 traceback 。
'''

# 10.3.1 　处理 ZeroDivisionError  异常
# 下面来看一种导致 Python 引发异常的简单错误。
# 你可能知道不能将一个数字除以 0 ，但我们还是让 Python 这样做吧：
'''
print(5/0)
'''


# 10.3.2 　使用 try-except  代码块
# 当你认为可能发生了错误时，可编写一个 try-except 代码块来处理可能引发的异常。
# 你让 Python 尝试运行一些代码，并告诉它如果这些代码引发了指定的异常，该怎么办。
# 处理 ZeroDivisionError 异常的 try-except 代码块类似于下面这样：
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")



# 10.3.3 　使用异常避免崩溃
# 发生错误时，如果程序还有工作没有完成，妥善地处理错误就尤其重要。
# 这种情况经常会出现在要求用户提供输入的程序中；
# 如果程序能够妥善地处理无效输入，就能再提示用户提供有效输入，而不至于崩溃。
# 下面来创建一个只执行除法运算的简单计算器：
'''
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("Second number:")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)
'''
# 这个程序没有采取任何处理错误的措施，因此让它执行除数为 0 的除法运算时，它将崩溃




# 10.3.4 　 else  代码块
# 通过将可能引发错误的代码放在 try-except 代码块中，可提高这个程序抵御错误的能力。
# 错误是执行除法运算的代码行导致的，因此我们需要将它放到 try-except 代码块中。
# 这个示例还包含一个 else 代码块；依赖于 try 代码块成功执行的代码都应放到 else 代码块中：
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("Second number:")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)