#TempConvert.py
TempStr = input("请输入带有符号的温度值：")
if TempStr[-1] in ['f','F']:
    C = (eval(TempStr[0:-1]) - 32) / 1.8
    print("转换后的温度是{:.2f}C".format(C))

elif TempStr[-1] in ['c','C']:
    F = 1.8 * eval(TempStr[0:-1]) + 32
    print("转换后的温度是{:.2f}F".format(F))

else:
    print("输入格式错误")


'''
eval()  去掉参数最外侧引号并执行余下语句的函数


>>> eval("1")
1

>>> eval("1+2")
3

>>> eval('"1+2"')
1+2

>>> eval('print("Hello")')
Hello 


'''
