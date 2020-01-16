# 重复字符串
print("hello" *2)

# 通过索引获取字符串中字符，和列表切片是相同的
print("helloworld"[2:])

# in 成员运算符   如果字符串中包含给定的字符则返回True
print( 123 in [23,45,123])
print( 'el' in 'hello' )

# 格式字符串
print("\n格式字符串：")
print('alex is a good teacher')
print('%s is a good teacher' % 'alex')


# 字符串拼接
print("\n字符串拼接")
a = '123'
b = 'abc'
c = a + b
print(c)

# join方法拼接
c = "".join([a,b])
print(c)
c = "*****".join([a,b])
print(c)
c = "---".join([a,b])
print(c)

d = '44'
c = "---".join([a,b,d])
print(c)



# 字符串的内置方法
print("\n\n字符串内置方法：")
st = "he\tllo kitty"
print(st.count("l"))	# 统计元素个数
print(st.capitalize())	# 字符串首字母大写
print(st.center(20, '-'))	# 字符串居中，20总宽度，其他位置用"-"补充

print("")
print(st.endswith('y'))	# 判断是否以某个字符串为结尾，如果是返回True，不是返回False。 可以加范围start,end
print(st.startswith('he'))	# 判断是否以某个内容开头
print(st.expandtabs(tabsize=10))	# 控制\t的长度  \t:tab

print("")
print(st.find("t"))	# 查找到第一个元素并将索引值返回。返回"-1"代表没有找到
st2 ="hello kitty {name} is {age}"
print(st2.format(name='alex', age=37))	# 格式化输出的另一种方式	
print(st2.format_map({'name':"alex", 'age':22}))  # format和format_map的区别是map用的是字典

print("")
print(st.index('o'))	# 返回索引，找不到就报错。find()不会报错
print("abc123".isalnum())	# 判断这个字符串是否包含数字或字母（中文也行）
print("123169".isdecimal())	# 判断是不是一个十进制数
print("123169".isdigit())	# 判断是不是一个整型
print("126.9999".isnumeric())	# 判断是不是一个数字
print("1269999".isidentifier())	# 判断是不是非法标志字符，如数字开头就False
print("abC".islower())	# 判断是否为字母全小写
print("ABC".isupper())	# 判断是否为字母全大写
print("  e".isspace())	# 判断是否为全空格
print("My Title".istitle())	# 判断是否标题格式，即每个单词首字母大写

print("\nMy Title".lower())	# 转为小写
print("My Title".upper())	# 转为大写
print("My Title".swapcase())	# 大小写互转

print()
print("My Title".ljust(20, "*"))	# 只向右填充
print("My Title".rjust(20, "*"))	# 只向左填充
print("     My Title \n".strip())	# 去掉开头和结尾的空格、换行符
print("     My Title \n".lstrip())	# 去掉左边的空格、换行符
print("     My Title \n".rstrip())	# 去掉右边的空格、换行符

print()
print("My title".replace("itle", "lesson"))	# 替换
print("My title title".rfind('t'))	# 从右往左找
print("My title title".split(' '))	# 对字符串做分割，返回一个列表
print("My title title".rsplit('t',1))	# 从右开始对字符串做分割，只分割1次
print("My title title".title())	# 每个单词首字母大写




'''
一些重要的字符串方法：
print(st.count("l"))	# 统计元素个数
print(st.center(20, '-'))	# 字符串居中，20总宽度，其他位置用"-"补充
print(st.startswith('he'))	# 判断是否以某个内容开头
print(st.find("t"))	# 查找到第一个元素并将索引值返回。返回"-1"代表没有找到
print(st2.format(name='alex', age=37))	# 格式化输出的另一种方式	
print("\nMy Title".lower())	# 转为小写
print("My Title".upper())	# 转为大写
print("     My Title \n".strip())	# 去掉开头和结尾的空格、换行符
print("My title".replace("itle", "lesson"))	# 替换
print("My title title".split(' '))	# 对字符串做分割，返回一个列表
'''
