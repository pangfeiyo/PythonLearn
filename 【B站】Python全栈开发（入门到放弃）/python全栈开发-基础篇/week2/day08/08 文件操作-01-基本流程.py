# 只读   'r'
f = open('小重山.txt','r')
data = f.read()
print(data)

f.close()


# 写操作  'w'
# 会清空原有内容（格式化）
f = open('小重山.txt','w') # 在创建对象的同时就已经清空了内容
f.write('hello world')
f.write('alex')
f.close()
# 如果找不到这个文件，就创建一个


# 写操作 'a'     在最后加入
f = open('小重山.txt','a')
f.write('昨夜寒蛩不住鸣。\n')
f.write('惊回千里梦，已三更。')


'''
昨夜寒蛩不住鸣。
惊回千里梦，已三更。
起来独自绕阶行。
人悄悄，帘外月胧明。
白首为功名。
旧山松竹老，阻归程。
欲将心事付瑶琴。
知音少，弦断有谁听？
'''