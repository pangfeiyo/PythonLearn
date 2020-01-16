# if else  要么怎样，要么不怎么样
# for/while else  干完了能怎样，干不完就别想怎样
# try except else 没有问题，那就干吧

# while else   当 while 循环体完全执行完后才会执行else
# 在 while 体中若break等跳出循环则不会执行else
# for 同理
def showMaxFactor(num):
    count = num // 2
    while count > 1:
        if num % count == 0:
            print("%d最大的约数是%d" % (num, count))
            break
        count -= 1
    else:
        print("%d是素数！" % num)
num = int(input("输入一个数："))
showMaxFactor(num)


# 在 try 中加else
try:
    # int('abc')    # 出错
    int(123)    # 没有问题
except ValueError as reason:
    print('\n出错啦', str(reason))
else:
    print("\n没有问题")


# 简洁的 with 语句
# 有一些任务，可能事先需要设置，事后做清理工作。对于这种场景，Python的with语句提供了一种非常方便的处理方式。
# 一个很好的例子是文件处理，你需要获取一个文件句柄，从文件中读取数据，然后关闭文件句柄。
# 有效避免打开文件后忘记关的情况
# with语句会自动处理文件的打开和关闭，如果中途出现异常，会执行清理代码，然后确保文件自动关闭
''' 正常情况
try:
    f = open("data.txt",'w') # 这个文件并不存在 
    for each_line in f :
        print(each_line)
except OSError as reason:
    print("出错啦", reason)
finally:
    f.close() # 如果 f 要打开的文件并不存在，即使f.close()在finall中，一样要报错
'''
# 使用 with 可以避免这样的问题
try:
    with open('data.txt','w') as f:
        for each_line in f:
            print(each_line)
except OSError as reason:
    print("出错啦", reason)