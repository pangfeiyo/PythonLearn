# 0.尝试将文件（OpenMe.mp3）打印到屏幕上
# 直接使用打开文本文件的形式打开即可，至于为什么？打开后会告诉你
f = open('C:\\Users\\PangFei\\Desktop\\Python学习\\甲鱼python\\课程代码\\第28讲\\OpenMe.mp3')
for each_line in f:
    print(each_line)
f.close()


# 1.编写代码，将上一题中的文件（OpenMe.mp3）保存为新文件（OpenMe.txt）
f1 = open('C:\\Users\\PangFei\\Desktop\\Python学习\\甲鱼python\\课程代码\\第28讲\\OpenMe.mp3')
# 使用 'x' 打开更安全，如果文件已存在则会抛出异常。如果不存在，则创建
f2 = open('C:\\Users\\PangFei\\Desktop\\Python学习\\甲鱼python\\课程代码\\第28讲\\OpenMe.txt','x')
f2.write(f1.read())     # f2.写入(f1.读取)
f2.close()
f1.close()