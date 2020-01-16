#简单实现
brand = ['李宁','耐克','阿迪达斯','鱼C工作室']
slogan = ['一切皆有可能','Just do it','Impossible is mothing','让编程改变世界']
print('鱼C工作室的口号是：',slogan[brand.index('鱼C工作室')])



# 创建和访问字典
dict1 = {'李宁':'让一切皆有可能','耐克':'Just do it',
         '阿迪达斯':'Impossbile is mothing','鱼C工作室':'让编程改变世界'}  # 字典是映射类型
print("鱼C工作室的口号是：",dict1['鱼C工作室'])

dict2 = {1:'one',2:'two',3:'three'}
print(dict2[2])

dict3 = {}
print(dict3)

#help(dict)

dict3 = dict((('F',70),('i',105),('s',115),('h',104),('C',67)))
print(dict3)

#这里可以不用给小甲鱼加''，加了反而会报错
dict4 = dict(小甲鱼='让编程改变世界', 苍井空='让AV征服所有宅男')
print(dict4)

# 查到原dict4中有'苍井空'这个键，这里会改变原键的值 
dict4['苍井空'] = '通过学习提高职业技能'
print(dict4)
# 查到原dict4中没有'爱迪生'这个键，这里会自动在字典中加入此键对值
dict4['爱迪生'] = '天才就是99汗水+1灵感'
print(dict4)