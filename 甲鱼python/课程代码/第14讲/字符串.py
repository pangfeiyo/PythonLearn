# py2.x与py3部分字符串有区别
str1 = 'I love fishc.com'
print(str1[:6])

print(str1[5])


print(str1[:6] + '你我' + str1[6:]) #该插入并不会改变st1，相当于再建一个
print(str1)

#字符串方法看扩展阅读
#这里只有部分

#开头转大写
abc = 'aADefg'
print(abc.capitalize())    #必须在要外面加层pyrint()才显示大写
print(abc)  #输出的还是小写
#整个字符串转小写
print(abc.casefold())
#字符串居中，使用空格填充剩下的字符
print(abc.center(40))
#返回sub在字符串出现的次数，start和end参数表示范围，可选
#count(sub,[start[,end]])
print(abc.count('A'))
#检查结尾是不是以sub结束
print(abc.endswith('g'))
#把字符串中tab符号（\t）转换成空格，如不指定参数，默认是8
abc2 = 'i\tlovefish\tc.com'
print(abc2.expandtabs())
#检测sub是否包含在字符串中，如果有返回索引值，否则返回-1，start和end参数表示范围，可选
#find(sub[,start[,end]])
print(abc2.find('\t'))
#index  跟find()方法一样，不过如果sub不在string中会产生一个异常
abc2.index('i')
print(abc2)
#把old子字符串替换成new子字符串，如果count指定，则替换不超过count次
#replace(old,new[,count])
abc3 = 'IlovefishC.com'
print(abc3.replace('love','ai'))