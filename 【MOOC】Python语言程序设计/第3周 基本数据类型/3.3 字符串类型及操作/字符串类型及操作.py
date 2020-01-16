# 获取星期字符串
# -输入：1-7的整数，表示星期几
# -输出：输入整数对应的星期字符串
# -例如：输入3，输出 星期三

# 方法一：
weekStr = "星期一星期二星期三星期四星期五星期六星期天"
weekId = eval(input("请输入星期数字(1-7)："))
pos = (weekId - 1) *3
print(weekStr[pos:pos+3])

# 方法二：
weekStr = "一二三四五六日"
weekId = eval(input("请输入星期数字(1-7)："))
print("星期" + weekStr[weekId-1])


'''
字符串处理函数：
  hex(x) 或 oct(x)  整数x的十六进制或八进制小写形式字符串
  hex(425) 结果为"0x1a9"   oct(425) 结果为"0o651"

  chr(u)  x为unicode编码，返回其对应的字符
  ord(x)  x为字符，返回其对应的Unicode编码
'''
print("1+1=2" + chr(10004)) # 对号
print("这个字符♉的Unicode值是：" + str(ord("♉")))   # 金牛是9801，是第二个星座

# 输出所有星座的符号
for i in range(12):
    print(chr(9800 + i), end=" ")



"""
字符串处理方法：
  str.lower() 或 str.upper() 返回字符串的副本，全部字符小写/大写
                             "abFdefGG".lower() 结果为 "abfdefgg"
  str.split(sep=None) 返回一个列表，由str根据sep被分隔的部分组成
                      "A,B,C".split(",") 结果为["A","B","C"]
  str.count(sub) 返回子串sub在str中出现的次数
                 "a apple a day".count("a") 结果为4
  str.replace(old, new) 返回字符串str副本，所有old子串被替换为new
                        "python".replace("n", "n123.io") 结果为 "python123.io"
  str.center(width [,fillchar]) 字符串str根据宽度width居中，fillchar可选
                                "python".center(20,"=") 结果为
                                "=======python======="
  str.strip(chars) 从str中去掉在其左侧和右侧chars中列出的字符
                   "= python= ".strip(" =np") 结果为"ytho"
  str.join(iter) 在iter变量除最后元素外每个元素后增加一个str
                 ",".join("12345") 结果为
                 "1,2,3,4,5"  # 主要用于字符串分隔等
"""
