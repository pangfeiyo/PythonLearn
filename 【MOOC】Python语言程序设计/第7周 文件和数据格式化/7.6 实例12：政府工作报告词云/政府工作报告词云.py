'''
《决胜全面建成小康社会 夺取新时代中国特色社会主义伟大胜利》
在中国共产党第十九次全国代表大会上的报告
（2017年10月18日）
习近平
https://python123.io/resources/pye/新时代中国特色社会主义.txt

《中共中央 国务院关于实施乡村振兴战略的意见》
2018一号文件
（2018年01月02日）
中共中央 国务院
https://python123.io/resources/pye/关于实施乡村振兴战略的意见.txt


基本思路：
  - 步骤1：读取文件、分词整理
  - 步骤2：设置并输出词云
  - 步骤3：观察结果，优化迭代

'''
import jieba
import wordcloud
from scipy.misc import imread    # 能够读取一个图片文件

def func1():
    f = open("新时代中国特色社会主义.txt", 'r', encoding="utf-8")
    t = f.read()
    f.close()

    # 对中文文本进行分词，精准模式
    ls = jieba.lcut(t)
    # 用空格把列表元素连接起来，形成一个长字符串
    txt = " ".join(ls)

    # max_words=15 词云中最多显示15个单词
    w = wordcloud.WordCloud(width=1000, height=700,
                            background_color='white',
                            max_words=15)
    # 向WordCloud对象w中加载文本txt
    w.generate(txt)
    w.to_file("grwordcloud1.png")

def func2():
    f = open("关于实施乡村振兴战略的意见.txt", 'r', encoding="utf-8")
    t = f.read()
    f.close()

    # 对中文文本进行分词，精准模式
    ls = jieba.lcut(t)
    # 用空格把列表元素连接起来，形成一个长字符串
    txt = " ".join(ls)

    # max_words=15 词云中最多显示15个单词
    w = wordcloud.WordCloud(width=1000, height=700,
                            background_color='white',
                            max_words=15)
    # 向WordCloud对象w中加载文本txt
    w.generate(txt)
    w.to_file("grwordcloud2.png")

def func3():
    '''改变图片布局'''
    # 把图片变成一个图片表达的内部变量
    mask = imread("fivestart.png")

    f = open("新时代中国特色社会主义.txt", 'r', encoding="utf-8")
    t = f.read()
    f.close()

    # 对中文文本进行分词，精准模式
    ls = jieba.lcut(t)
    # 用空格把列表元素连接起来，形成一个长字符串
    txt = " ".join(ls)

    # max_words=15 词云中最多显示15个单词
    # mask 可以改变wordcloud图片
    w = wordcloud.WordCloud(width=1000, height=700, mask=mask,
                            background_color='white',
                            )
    # 向WordCloud对象w中加载文本txt
    w.generate(txt)
    w.to_file("grwordcloud3.png")

def func4():
    '''改变图片布局'''
    # 把图片变成一个图片表达的内部变量
    mask = imread("chinamap.png")

    f = open("新时代中国特色社会主义.txt", 'r', encoding="utf-8")
    t = f.read()
    f.close()

    # 对中文文本进行分词，精准模式
    ls = jieba.lcut(t)
    # 用空格把列表元素连接起来，形成一个长字符串
    txt = " ".join(ls)

    # max_words=15 词云中最多显示15个单词
    # mask 可以改变wordcloud图片
    w = wordcloud.WordCloud(width=1000, height=700, mask=mask,
                            background_color='white',
                            )
    # 向WordCloud对象w中加载文本txt
    w.generate(txt)
    w.to_file("grwordcloud4.png")


#func1()
#func2()
#func3()
func4()