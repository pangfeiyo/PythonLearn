"""
遍历某个结构形成的循环运行方式
for <循环变量> in  <遍历结构>:
    <语句块>
"""

# 计算循环（N次）
for i in range(5):
    print(i)

for i in range(5):
    print("hello:",i)

# 计算循环（特定次）
for i in range(1,6):
    print(i)

for i in range(1,6,2): # 步长2
    print("hello:",i)

# 字符串遍历循环
for c in "python123":
    print(c,end=",")

# 列表遍历循环
print()
for item in [123,"py",456]:
    print(item,end=",")

# 文件遍历循环
# for line in fi:
#    <语句块>
# -fi是一个文件标识符，遍历其每行，产生循环


# 无限循环
# 由条件控制的循环运行方式
print()
a = 3
while a>0:
    a=a-1
    print(a)


# 循环控制保留字
# break：跳出并结束当前整个循环，执行循环后的语句
# continue：结束当次循环，继续执行后续次数循环
for c in "PYTHON":
    if c =="T":
        continue
    print(c,end="")

print()
for c in "PYTHON":
    if c =="T":
        break
    print(c,end="")


print()
s = "PYTHON"
while s != "":
    for c in s:
        print(c,end="")
    s = s[:-1]  # 从第一个到倒数第二个，不包含最后一个字符

print()
s = "PYTHON"
while s != "":
    for c in s:
        if c == "T":
            break
        print(c,end="")
    s = s[:-1]




# 循环的扩展  循环与else
# -当循环没有被break语句退出时，执行else
# -else语句块作为“正常”完成循环的奖励
print()
for c in "PYTHON":
    if c =="T":
        continue
    print(c,end="")
else:
    print("正常退出")
