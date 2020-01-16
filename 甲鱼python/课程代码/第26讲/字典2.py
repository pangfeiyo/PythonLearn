dict1 = {}
# 如果不提供值（键值对中的值）的值，那么默认为none。这里的1，2，3是键
# fromkeys()方法是直接创建一个新字典
dict1 = dict1.fromkeys((1,2,3))
print(dict1)

dict1 = dict1.fromkeys((1,2,3),'Number')
print(dict1)

dict1 = dict1.fromkeys((1,2,3),('one','two','three'))
print(dict1)


dict1 = dict1.fromkeys(range(32),'赞')
print(dict1)
for eachKey in dict1.keys():   # keys 键（键值对中的键）
    print(eachKey)

for eachValue in dict1.values():    # values 值（键值对中的值）
    print(eachValue)

for eachItem in dict1.items():  #将字典中的键对值转换成元组
    print(eachItem)


print(),print(dict1[31])

# get() 函数返回指定键的值，如果值不在字典中返回默认值
# dict.get(key, default=None)
# key -- 字典中要查找的键。
# 如果用dict1[32]肯定会报错，这里用.get 如果没有找到，结果为None
print(dict1.get(32))    
# default -- 如果指定键的值不存在时，返回该默认值值。
print(dict1.get(33,"木有！"))
print(dict1.get(31,"木有！"))  # 因为存在名为31的键，所以会打印31的值

print("\n31在dict1中吗：",31 in dict1)
print("33在dict1中吗：",33 in dict1)




# 清空字典   clear
print("\n-- 清空字典 --")
dict1.clear()
print(dict1)

dict1 = {}  # 这么写也可以，但不严谨，下方举例
# 举例
a = {'姓名':'小甲鱼'}
b = a 
print("b=a时，b的值：",b)
a = {}
print("a={}时，a的值：",a)
print("a修改后，b的值：",b)

# 如果用clear的话
a = b 
print(a,b)
a.clear()
print(a,b)

print(dir(dict))



# copy  浅拷贝
print("-- copy --")
a = {1:'one', 2:'two', 3:'three'}
b = a.copy()    #浅拷贝
c = a   # 赋值
print(a,b,c)
print(id(a))
print(id(b))
print(id(c))
c[4] = 'four'
print(a,b,c)    
# 得出赋值和浅拷贝是不一样的， 赋值就是将同样的数值贴在不同的标签（a,c）上



# pop()和 popitem()的区别
# pop是给定键弹出对应的值，并删除该键对值
# popitem是弹出一个项，并删除
# 在字典中，每个键值对的存储顺序是无序的，所以popitem弹出的项是随机的
print("-- pop()和popitem()区别 --")
print(a.pop(2))
print(a)
print(a.popitem())
print(a)



# setdefault()
# 和get()有些类似，不同的是，如果找不到就新建一个项存进字典
a.setdefault('小白')
print(),print(a)
a.setdefault(5,'five')
print(a)



# update
# 利用一个字典或映射关系去更新另一个字典
print("\n-- update --")
b = {'小白':'狗'}
a.update(b)
print(a)




# 如果需要将字典1 dict1 = {1:'one', 2:'two', 3:'three'} 拷贝到dict2，怎么做
# 可以利用字典的copy()方法：dict2 = dict1.copy()
# 其他语言的习惯是直接用赋值的方法（dict2 = dict1），但在Python中只是将对象的引用拷贝过去而已。
# 以下为区别：
'''
a = {1:'one', 2:'two', 3:'three'}
b = a.copy()
c = a
c[4] = 'four'
c
{1: 'one', 2: 'two', 3: 'three', 4: 'four'}
a
{1: 'one', 2: 'two', 3: 'three', 4: 'four'}
b
{1: 'one', 2: 'two', 3: 'three'}
'''