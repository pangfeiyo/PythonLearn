'''
try:
    检测范围
except Exception[as reason]:
    出现异常（Exception）后的处理代码
finally:
    无论如何都会被执行的代码
'''

# 在try中，有一句出错直接跳过剩下代码，进入except
try:
    # int('abc') # 没有关注有关这个的异常，所以是正常报错，如果想给用户提示，可以方便些使用不加任意异常名的except，但不推荐这么做
    sum = 1 + '1'
    f = open("这是一个文件.txt")
    print(f.read())
    f.close()
# OSError可以省略（默认捕捉所有异常），但如果要加上as，就不能省略
# as reason(reason是个变量名，可以随意更改) 错误原因
# except (OSError, TypeError) as reason:    # 也可以这么写
except OSError as reason:
    print("1文件出错，可能是找不到\n错误的原因是：", str(reason))  # 这里的str也可以不加，暂时没有看出不同
except TypeError as reason:
    print("2文件出错，可能是找不到\n错误的原因是：", str(reason))  # 这里的str也可以不加，暂时没有看出不同


# 自己引发异常
raise