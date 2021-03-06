#和硬盘的格式化不一样
#format有两种参数，位置与关键字
#位置
print("{0} love {1}.{2}".format("i","fishc","com"))
#关键字
print("{a} love {b}.{c}".format(a="i",b="fishc",c="com"))
#两者结合
#位置必须在关键字之前
print("{0} love {b}.{c}".format("i",b="fishc",c="com"))

print("\ta")
print(r"\ta")
print("\\ta")
#想打印"{0}"，再套一层 {} 即可，但这样位置参数{0}就被解释掉了，所以后面的“不打印”无法打印出
print("{{0}}".format("不打印"))

# ：后面接的就是格式化符号
# .1 意思就是四舍五入，f 就是打印定点数（和符点数差不多，都是打印小数）
print("{0:.1f}{1}".format(27.658,"GB"))

#格式化字符及其ASCII码，97的ASCII码是a
print("%c" % 97)
print("%c %c %c" % (97,98,99))
#格式化字符串，相当于把%s 替换成i love
print("%s" % "i love fishc.com")
#格式化整数
print("%d+%d=%d" % (4,5,4+5))
#格式化无符号八进制数 %o
print("%o" % 10)
#%x %X 十六进制  小写与大写区别
print("%x" % 10)
print("%X" % 10)
#格式化定点数，指定小数点精度。默认精确到6位小数往
print("%f" % 27.658)
#用科学计数法格式化定点数，#e 与#E 相同
print("%e" % 27.658)
print("%E" % 27.658)
#根据值的大小决定使用%f 或%e，#g 与#G 相同
print("%g" % 27.658)
print("%G" % 27.658)

print(),print("格式化操作辅助命令")
#格式化操作辅助命令
# m.n  m是显示的最小总宽度，n是小数点后的位数
print("%5.1f" % 27.658) #如果不够，前面会自动补上
#精确到两位小数
print("%.2e" % 27.658)
# m.n 小数点左边指一共占多少位
print("%10d"%5)
#左对齐
print("%-10d" % 5)
#打印出一个八进制
print("%#o" % 10)
#打印十六进制
print("%#x" % 108)
#打印十进制
print("%#d" %108)
#前面用0 补上
print("%010d"%5)
#5在开头，后面用0 补，因为 -  号为左对齐
print("%-010d"% 5)