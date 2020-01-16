name = input("请输入要查找的用户名：")
score = [['迷途',85],['黑夜',80],['小布丁',65],['福禄娃娃',95],['怡静',90]]
IsFind = False

for each in score:
    if name in each:
        print(name + "的得分是：",each[1])
        IsFind = True
        break

if  IsFind == False:
    print("查找的数据不存在！")


#猜想一下 min() 这个BIF的实现过程
def min(x):
    least = x[0]

    for each in x:
        if each < least:
            least = each

    return least

print(min('123456789'))

#改善 sum() ，自动跳过字符串并返回正确的结果
#def  就是定义函数的意思   return 返回值
# http://www.cnblogs.com/nosnowwolf/archive/2012/05/23/2514997.html
def sum(x):
    result = 0
    for each in x:
        if  (type(each) == int) or (type(each) == float):
            result = result + each
        else:
            continue
    return result
print(sum([1,2,3,2.3,'a','1',True]))