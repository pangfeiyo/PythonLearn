dic = {1:'alex', 'age':35, 'hobby':{'girl_name':'铁锤', 'age':45}, 'is_handsome':True}

print(dic['hobby'])

dic1 = {'name':'alex'}
dic1['age'] = 18
print(dic1)

# setdefault 如果已存在这个键，不做任何操作，如果没有，增加
# 如果存在会返回这个键的值
ret = dic1.setdefault('age',34)
print(ret)

dic1.setdefault('hobby','girl')
print(dic1)



# 查  通过键去查找
print("\n查")
dic3 = {'age':18, 'name':'alex', 'hobby':'girl'}
print(dic3['name'])
print(dic3.keys())  # 所有键
print(list(dic3.keys()))    # 转换成列表并打印
print(dic3.values())    # 所有值



# 改
print("\n改")
dic3 = {'age':18, 'name':'alex', 'hobby':'girl'}
dic3['age'] = 55
print(dic3)


# update 更新，  如果有重复则覆盖
dic4 = {'age':18, 'name':'alex', 'hobby':'girl'}
dic5 = {'1':'111', 'name':'222'}
dic4.update(dic5)
print('dic4',dic4)
print('dic5',dic5)




# 删
print('\n删')
dic5 = {'name':'alex', 'age':18, 'class':1, 'hobby':'gril', 'girl_name':'铁锤'}
print(dic5.pop('age'))  # pop() 删除字典中指定的键值对，并返回该键值对的值

del dic5['name']    # 删除字典中指定的键值对
print(dic5)

print(dic5.popitem())   # 随机删除某组键值对，并以元组方式返回值

dic5.clear()    # 清空字典内容
print(dic5)

del dic5 # 删除整个字典，内存中也不存在