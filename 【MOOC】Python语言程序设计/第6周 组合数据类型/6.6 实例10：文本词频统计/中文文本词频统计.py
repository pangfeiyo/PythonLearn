# 需求：一篇文章，出现了哪些单词？哪些单词出现的最多？
# 英文文本：Hamet  分析词频
# http://python123.io/resources/pye/hamlet.txt
# 中文文本：《三国演义》 分析人物
# http://python123.io/resources/pye/threekingdoms.txt
import jieba

# 中文文本
text = open("threekingdoms.txt",'r', encoding='utf-8').read()
# 不是人名但次数靠前的词
excludes = {"将军","却说","荆州",'二人','不可','不能','如此','商议',
            '如何','主公','军士','左右','军马','引兵','次日','大喜',
            '天下','东吴','于是','今日','不敢','魏兵','一人','陛下',
            '都督','人马','不知','汉中','只见','众将','蜀兵','上马',
            '大叫','太守','此人','夫人','后人','背后','城中'}
# 精确模式
words = jieba.lcut(text)
# 建空字典
counts = {}

for word in words:
    # 长度为一，肯定不是词
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相曰" or word == "丞相":
        rword = "曹操"
    elif word == '后主':
        rword = "刘禅"
    elif word == '先主':
        rword = "刘备"
    elif word == "天子":
        rword = "刘协"
    else:
        rword = word
    # get() 若键word存在，则返回相应值，不在则返回0
    counts[rword] = counts.get(rword, 0) + 1

# 删除不是人名但次数靠前的词
for word in excludes:
    del counts[word]

items = list(counts.items())

# 排序，对列表按照键值对的两个元素的第二个元素进行排序，由大到小
items.sort(key = lambda x:x[1], reverse=True)
for i in range(15):
    word, count = items[i]
    if len(word) > 2:
        print("{0:<9}{1:>5}".format(word, count))
    else:
        print("{0:<10}{1:>5}".format(word, count))