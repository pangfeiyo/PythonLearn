# 用来处理pdf文件的工具
from PyPDF2 import PdfFileReader, PdfFileMerger

merger = PdfFileMerger()
input1 = open("document1.pdf", 'rb')
input2 = open("document2.pdf", 'rb')
merger.append(fileobj=input1, pages=(0,3))
merger.merge(position=2, fileobj=input2, pages=(0,1))
output = open("document-output.pdf", "wb")
merger.write(output)


'''
NLTK：自然语言处理第三方库
  - 提供了一批简单易用的自然语言文本处理功能
  - 支持语言文本分类、标记、语法句法、语义分析等
  - 最优秀的Python自然语言处理库

'''