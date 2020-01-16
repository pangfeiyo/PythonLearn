# 第一个元素的每个值都做为键， 第二个元素做为值
dic6 = dict.fromkeys(['host1','host2','host3'], 'test')
print(dic6)

# 这里有一个问题，涉及到深浅拷贝
# 改了test3后，所有的都变成了test3
dic6 = dict.fromkeys(['host1','host2','host3'], ['test1','test2'])
dic6['host2'][1] = 'test3'
print(dic6)



# 字典嵌套
print("\n字典嵌套")
av_catalog = {
    '欧美':{
        'www.youporn.com':['很多免费的，世界最大的', '质量一般'],
        'www.pornhub.com':['很多免费的，也很大', '质量比youporn高点'],
        'letmedothistoyou.com':['多是自拍，高质量图片很多', '资源不多，更新慢']
    },
    '日韩':{
        "tokyo-hot":["质量怎么样不清楚，个人已经不喜欢日韩风了","听说是收费的"]
    },
    '大陆':{
        "1024":['全部免费，真好，好人一生平安', '服务器在国外，慢']
    }
}

av_catalog['欧美']['www.youporn.com'][1] = '高清无码1080P'
print(av_catalog)



# 字典排序
print("\n字典排序")
dic5 = {5:'555', 2:'666', 4:'444'}
'''sort 与 sorted 区别：
sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。'''
print(sorted(dic5))
print(sorted(dic5.values()))
print(sorted(dic5.items()))



# 字典的遍历
print("\n字典遍历")
dic5 = {'name':'alex', 'age':18}

# 这个for 默认打印出键
for i in dic5:
    print(i)

# 方法一：打印出键值
# 推荐方法一，因为方法二实际是把字典转成列表，数量少还可以，多了就会慢
print("\n方法一：")
for i in dic5:
    print(i, dic5[i])

# 方法二：
print("\n方法二：")
for i in dic5.items():
    print(i)

print()
for i,j in dic5.items():
    print(i,j)