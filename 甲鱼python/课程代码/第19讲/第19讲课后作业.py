# 在函数中，若主体中的全局变量与局部变量同名，那么函数便会使用局部变量而不使用主体的全局变量
var = ' Hi '

def fun1():
    # global  使全局变量在局部变量中改变
    global var
    var = ' Baby '
    return fun2(var)

def fun2(var):
    var += 'I love you'
    fun3(var)
    return var
    # return fun3(var)

def fun3(var):
    var = ' 小甲鱼 '
    return var

print(fun1())


# 动动手
# 编写一个函数，判断传入的字符串参数是否为“回文联”
# # （回文联即用回文形式写成的对联，即可顺读，也可倒读。例如：上海自来水来自海上）
print("\n方法一：")
string = input("请输入对联：")

def palindrome(string):
    length = len(string)
    last = length - 1

    length = length // 2   # 结果为 9 // 2 = 4

    flag = 1
    for each in range(length):
        if string[each] != string[last]:
            flag = 0
        last -= 1

    if flag == 1:
        return 1
    else:
        return 0

if palindrome(string) == 1:
    print("是回文！")
else:
    print("不是回文！")

# 方法二
print("\n方法二")
def palindrome(string):
    list1 = list(string)
    list2 = reversed(list1)
    if list1 == list(list2):
        return "是回文"
    else:
        return "不是回文"
print(palindrome("上海自来水来自海上"))


# 分别统计出传入字符串参数（可能不只是一个参数）的英文字母、空格、数字和其他字符的个数。
# count(*param)  收集参数   把标志是收集参数的参数把他用元组给打包起来
def count(*param):
    length = len(param)
    for i in range(length):
        letters = 0     #字母数
        space = 0       # 空格数
        digit = 0       # 数字数
        others = 0      # 其他数
        for each in param[i]:
            if each.isalpha():  # 是否为全部字母
                letters += 1
            elif each.isdigit():    # 是否为全部数字
                digit += 1
            elif each == " ":    # 是否为空格
                space += 1
            else:
                others += 1     # 其他
        print("第 %d 个字符串共有：英文字母 %d 个，数字 %d 个，空格 %d 个，其他字符 %d 个。" %
              (i+1, letters, digit, space, others))
count('I love fishc.com' , 'i love you, you love me.')