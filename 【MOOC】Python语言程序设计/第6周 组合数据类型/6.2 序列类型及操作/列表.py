'''
列表是序列类型的一种扩展
  - 列表是一种序列类型，创建后可以随便被修改
  - 使用方括号[] 或 list()创建，元素间用逗号,分隔
  - 可以使用或不使用小括号
'''
ls = ["cat",'dog','tiger',1024]
print(ls)
'''
ls
   \    使用等号= 并没有真正生成另一个列表，只是把同一个列表分给了两个不同的名字
     ["cat",'dog','tiger',1024]
   /    方括号[] 真正创建一个列表，赋值仅传递引用     
lt
'''
lt = ls
print(lt)


'''
ls[i] = x           替换列表ls第i元素为x
ls[i:j:k] = lt      用列表lt替换ls切片后所对应元素子列表
del ls[i]           删除列表ls中第i元素
del ls[i:j:k]       删除列表ls中第i到j以k为步长的元素
ls += lt            更新列表ls，将列表lt元素增加到ls中
ls *= n             更新列表ls，其元素重复n次
'''
ls = ["cat",'dog','tiger',1024]
ls[1:2] = [1,2,3,4]
print("\n"+str(ls))
del ls[::3]
print(ls)
print(ls*2)


'''
ls.append(x)        在列表ls最后增加一个元素x
ls.clear()          删除列表ls中所有元素
ls.copy()           生成一个新列表，赋值ls中所有元素
ls.insert(i, x)     在列表ls的第i位置增加元素x
ls.pop(i)           将列表ls中第i位置元素取出并删除该元素
ls.remove(x)        将列表ls中出现的第一个元素x删除
ls.reverse()        将列表ls中的元素反转
'''
ls = ["cat",'dog','tiger',1024]
ls.append(1234)
print("\n"+str(ls))
ls.insert(3, "human")
print(ls)
ls.reverse()
print(ls)