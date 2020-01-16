people = ['zhang','li','wang']
#print('I invited it ',end = " "),print(people)
print('今晚有 ' + people[0] + ' , ' + people[1] + " , " + people[2])
print('但 ' + people.pop() + ' 来不了')
print('所以今晚只有 ',end=" "),print(people)
people.append('liu')
print('来了位新朋友 ',people[2])
print('今天有 ',end=" "),print(people)

#添加3位新的嘉宾
#分别加入开头，中间，末尾
#前两个用insert()，加入末尾用 append()即可
people.insert(0,'ti')
people.insert(2,'major')
people.append('Jifu')
print(people)
#确定列表的长度，使用 len
#number = str(len(people))   #这里转为str型，如果不转下面会报错，不能为int型    如果下面print()里面用的是 +    如果用的是, 就不用转
number = len(people)
print('今晚共有', number , '位嘉宾')

#缩减名单，只留两位
name = people.pop()
print('对不起今晚不能邀请 ' + name +' 来')
name = people.pop()
print('对不起今晚不能邀请 ' + name +' 来')
name = people.pop()
print('对不起今晚不能邀请 ' + name +' 来')
name = people.pop()
print('对不起今晚不能邀请 ' + name +' 来')
print('你依然被邀请 '+ people[0] + ", " + people[1])
#清空列表
del people[0]
del people[0]
print("列表值：",end=" ")
print(people)
