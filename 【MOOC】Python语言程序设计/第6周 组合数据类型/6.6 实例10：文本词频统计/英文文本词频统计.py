# 需求：一篇文章，出现了哪些单词？哪些单词出现的最多？
# 英文文本：Hamet  分析词频
# http://python123.io/resources/pye/hamlet.txt
# 中文文本：《三国演义》 分析人物
# http://python123.io/resources/pye/threekingdoms.txt

# 英文文本
def getEnglishText():
    txt = open("hamlet.txt",'r').read()
    # 将所有英文字符转为小写
    txt = txt.lower()
    # 替换所有特殊符号
    for ch in '!#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
        txt = txt.replace(ch, " ")
    return txt

hamletTxt = getEnglishText()
# 通过指定分隔符对字符串进行切片，默认是空字符 
words = hamletTxt.split()

# 创建空字典
counts ={}

for word in words:
    # get() 若键word存在，则返回相应值，不在则返回0
    counts[word] = counts.get(word, 0) + 1
# 转换成列表
items = list(counts.items())
# 排序，对列表按照键值对的两个元素的第二个元素进行排序，由大到小
items.sort(key = lambda x:x[1], reverse=True)
# 取出前10个
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))