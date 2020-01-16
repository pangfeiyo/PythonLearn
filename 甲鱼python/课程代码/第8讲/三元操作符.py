# 三元操作符
'''
x,y = 4,5
if x<y:
    small=x
else:
    small=y
'''
#可改进为
x,y = 4,5
small = x if x<y else y
print(small)



#请将以下代码修改为三元操作符实现：
x,y,z = 6,5,4
'''
if x < y:
    small = x
    if z < small:
        small = z
elif y < z :
    small = y
else:
    small = z
'''
small = x if (x < y and x < z ) else (y if y < z  else z)
