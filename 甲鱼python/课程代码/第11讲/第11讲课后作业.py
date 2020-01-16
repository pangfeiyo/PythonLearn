# 从列表末尾取出一个元素，并将这个元素插入列表最前边
member = ['一','甲鱼','玩笑']
member.insert(0,member.pop())
print(member)


#python支持负数下标，列表最后一个元素为-1
list2 = [1,3,2,9,7,8]
print(list2[-3:-1])


#切片和赋值的区别
#切片相当于复制
sy1 = [1,3,2,9,7,8]
sy2 = sy1[:]    #切片复制sy1的内容给sy2
sy3 = sy1       #sy1赋值给sy3
sy1.sort()      #对sy1进行大小排序
print('sy1：',sy1)
print('sy2：',sy2)
print('sy3：',sy3)


