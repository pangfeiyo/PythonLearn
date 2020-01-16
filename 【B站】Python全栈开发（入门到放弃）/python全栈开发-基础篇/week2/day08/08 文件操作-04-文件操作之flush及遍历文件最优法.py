"""要运行哪段，就给哪段取消注释"""


# f = open("hello",'w')
# f.write("alex is 35")
# f.write("hello world")
# f.flush()	# 把缓存里的数据转到磁盘上
# f.close()



# import sys,time
# for i in range(30):
# 	sys.stdout.write("*")	# stdout 终端屏幕上的输出
# 	sys.stdout.flush()
# 	time.sleep(0.1)	# 暂停0.2秒



# # truncate()   截断，截掉（删掉）一部分
# f = open("小重山.txt",'a')	# 'a' 只能写，追加写
# f.truncate(5)	# 默认参数 -1。 如果不加参数，就是从开始位置截，有多少截多少，
# f.close()	



# f = open("小重山.txt",'r+',encoding='utf8')	# r+   读写，写在最后
# print(f.readlines())
# f.write("\n岳飞")
# f.seek(0)	# 光标回到初始位置，为了下面打印所有内容
# print(f.readlines())


