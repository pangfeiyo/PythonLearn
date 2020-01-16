# 终极问题
# 修改字符串内容   
# 用程序在小重山.txt文件中第六行尾加一个alex

f_read = open("小重山.txt",'r', encoding='utf8')
f_write = open("小重山2.txt",'w', encoding='utf8')

number = 0

for line in f_read:
	number+=1
	if number == 5:
		# join()  字符串拼接
		# 这里一定要加strip()，去除首尾字符串，为空代表空格
		line = "".join([line.strip(),"alex\n"])

	# 把line的内容写进小重山2.txt中
	f_write.write(line)

f_read.close()
f_write.close()