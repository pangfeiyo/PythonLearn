#d = open('C:\\Users\\PangFei\\Desktop\\file.txt','w')     # w 如果没有就新建，如果有就覆盖
#d.write('hello world!')
#d.close()

with open('C:\\Users\\PangFei\\Desktop\\file.txt','w') as f:
    f.write('hello')
f.close()


#两种都可以，新建一个文件，然后写入内容
