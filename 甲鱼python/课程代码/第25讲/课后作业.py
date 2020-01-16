# 1.尝试将数据 …… 创建为一个字典并访问键'C'对应的值
MyDict = dict((('F', 70), ('i',105), ('s',115), ('h',104), ('C',67)))
MyDict_2 = {'F':70, 'i':105, 's':115, 'h':104, 'C':67}

#print(type(MyDict))
# <class 'dict'>

#print(type(MyDict_2))
# <class 'dict'>

print(MyDict['C'])
print(MyDict_2['C'])



# 5.完善代码
print("\n-- 5 --")
data = '1000,小甲鱼,男'
MyDict = {}
#这里用的是字符串分割方法
MyDict['id'], MyDict['name'], MyDict['sex'] = data.split(',')

print("ID:   " + MyDict['id'])
print("Name: " + MyDict['name'])
print("Sex:  " + MyDict['sex'])