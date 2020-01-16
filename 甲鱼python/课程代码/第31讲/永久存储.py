# pickle 将要存储的内容转为二进制
# 存放：pickling
# 读取：unpickling
import pickle
my_list = [123, 3.14, '甲鱼','another list']
# 这里可以写任意后缀名
# 创建或打开
pickle_file = open('my_list.pkl','wb')  # 'b' 以二进制模式打开文件
# 将内容放进入
pickle.dump(my_list, pickle_file)
pickle_file.close()

# 读取
pickle_file = open('my_list.pkl','rb')
my_list2 = pickle.load(pickle_file)
print(my_list2)