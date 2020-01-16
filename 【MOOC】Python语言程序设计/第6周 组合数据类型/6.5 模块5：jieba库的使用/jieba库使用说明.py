# jieba是优秀的中文分词第三方库
# - 中文文本需要通过分词获得单个的词语
# - 需要额外安装
# - jieba提供三种分词模式，最简单只需要掌握一种


# - 利用一个中文词库，确定汉字之间的关联概率
# - 汉字间概率大的组成词组，形成分词结果
# - 除了分词，用户还可以添加自定义的词组


# - 精确模式、全模式、搜索引擎模式
# 精确模式：jieba.lcut(s) 把文本精确的切分开，不存在冗余单词
# 全模式：jieba.lcut(s, cut_all=true) 把文本中所有可能的词语都扫描出来，有冗余
# 搜索引擎模式：jieba.lcut_for_search(s) 在精确模式基础上，对长词再次切分
import jieba
print(jieba.lcut("中国是一个伟大的国家"))

print(jieba.lcut("中国是一个伟大的国家", cut_all=True))

print(jieba.lcut_for_search("中华人民共和国是伟大的"))

# 向分词词典增加新词
jieba.add_word("蟒蛇语言")

