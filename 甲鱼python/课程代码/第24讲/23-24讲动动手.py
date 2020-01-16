# 0.使用递归编写一个十进制转换为二进制的函数
# （要求采用“除2取余”的方式，结果与调用bin()一样返回字符串形式）
def Dec2Bin(dec):
    result = ''
    if dec:
        result = Dec2Bin(dec//2)    #  dec // 2 ，取整
        return result + str(dec%2)
    else:
        return result 
number = int(input("请输入一个整数：")) # 这里已定义将键盘输入的内容转换为int，不需要再if判定
result = Dec2Bin(number)
print(result)

# 1.写一个函数get_digits(n)，将参数n分解出每个位的数字并按顺序存放到列表中。
# 举例：get_digits(12345) ==> [1,2,3,4,5]
# 解题思路：利用除以10取余数的方式，每次调用get_digits(n//10)，并将余数存放到列表中即可。要注意的是结束条件设置正确
result1=[]
def get_digits(n):
    if n > 0:
        result1.insert(0, n % 10)   # n % 10，可以取出最后一位数字，使用方法insert()可在列表的任何位置添加新元素。为此，你需要指定新元素的索引和值
        get_digits(n // 10) # n // 10，取整
number = int(input("请输入一串数字："))
get_digits(number)
print(result1)

# 2.求回文字符串，现在使用递归
# 解题思路：有好多种方法，利用递归每次索引前后两个字符进行对比，当start > end 的时候，也正是首尾下标“碰面”的时候，即作为结束递归的条件。
def is_palindrome(n, start, end):
    if start > end:
        return 1     
    else:
        return is_palindrome(n, start+1, end-1) if n[start] == n[end] else 0
        
string = input('请输入一串字符串：')
length = len(string)-1  # -1的目的：下标是从0开始，但计数是从1开始，为了对齐下标这里要-1

if is_palindrome(string, 0, length):
    print('\"%s\"是回文字符串!' % string)
else:
    print('\"%s\"不是回文字符串!' % string)


# 3.使用递归解决以下问题：
# 有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。
# 问第三个人，又说比第2个人大2岁。问第2个人，说比第一个人大2岁。
# 最后问第一个人，他说是10岁。请问第五个人多大？
# 解题思路：利用递归方法，递归分为回推和递推两个阶段。要想知道第五个人岁数，需知道第四个人的岁数，依次类推，推到第一个人（10）岁，再往回推
def age(n):
    if n == 1:
        return 10
    else:
        return age(n-1)+2
number = int(input("请输入人数总和："))
result = age(number)
print("第{0}个人的年龄是{1}".format(number, age(number)))


#递归解析
#def age(5):
#    if n == 1:
#        return 10
#    else:
#        return age(5-1)+2
#          --def age(4)
#                return age(4-1)+2
#                  --def age(3)
#                        return age(3-1)+2
#                          --def age(n=2)
#                                if n == 1:
#                                    return 10
#                                else:
#                                    return age(n=2 - 1) +2
#                                      --def age(n=1):
#                                            if n == 1:
#                                                return 10