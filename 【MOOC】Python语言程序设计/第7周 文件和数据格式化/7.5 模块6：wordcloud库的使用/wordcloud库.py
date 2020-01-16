'''
wordcloud库把词云当作一个WordCloud对象
  - wordcloud.WordCloud()代表一个文本对应的词云
  - 可以根据文本词语出现的频率等参数绘制词云
  - 绘制词云的形状、尺寸和颜色都可以设定

w = wordcloud.WordCloud()
  - 以WordCloud对象为基础
  - 配置参数、加载文本、输出文件

w.generate(txt)         向WordCloud对象w中加载文本txt， w.generate("Python and WordCloud")
w.to_file(filename)     将词云输出为图像文件， .png 或 .jpg格式， w.to_file("outfile.png")


步骤1：配置对象参数
步骤2：加载词云文本
步骤3：输出词去文件
'''
import wordcloud

c = wordcloud.WordCloud()
c.generate("wordcloud by python")
c.to_file("pywordcloud.png")    # 默认400*200
'''
1.分隔：以空格分隔单词
2.统计：单词出现次数并过滤
3.字体：根据统计配置字号
4.布局：颜色环境尺寸


配置参数对象
width               指定词云对象生成图片的宽度，默认400像素。 w = wordcloud.WordCloud(width=600)
height              指定词云对象生成图片的高度，默认200像素。 w = wordcloud.WordCloud(height=400)
min_font_size       指定词云中字体最小字号，默认4号。 w = wordcloud.WordCloud(min_font_size=10)
max_font_size       指定词云中字体最大字号，根据高度自动调节。 w = wordcloud.WordCloud(min_font_size=20)
font_step           指定词云中字体字号的步进间隔，默认为1。 w = wordcloud.WordCloud(font_step=2)
font_path           指定字体文件的路径，默认None。 w = wordcloud.WordCloud(font_path="msyh.ttc")
max_words           指定词云显示的最大单词数量，默认20。 w = wordcloud.WordCloud(max_words=20)
stop_words          指定词云的排除词列表，即不显示的单词列表。 w = wordcloud.WordCloud(stop_words={"python"})
mask                指定词云形状，默认为长方形，需要引用imread()函数
                    from scipy.misc import imread
                    mk = imread('pic.png')
                    w = wordcloud.WordCloud(mask=mk)
background_color    指定词云图片的背景颜色，默认为黑色。 w = wordcloud.WordCloud(background_color="white")
'''
txt = "life is short, you need python"
w = wordcloud.WordCloud(
    background_color='white')
w.generate(txt)
w.to_file("pywcloud2.png")


# 中文词云
import jieba
txt = '程序设计语言是计算机能够理解和识别用户操作意图的种交互体系，\
它按照特定规则组织计算机指令，使计算机能够自动进行各种运算处理。'
w = wordcloud.WordCloud(width=1000, height=700)
# 中文需要先分词并组成空格分隔字符串
# clut 精确模式，会生成一个列表变量，其中的每一个元素是分隔之后的单词
# 需要将这些单词以文本的形式，以空格来分隔
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("pywcloud3.png")