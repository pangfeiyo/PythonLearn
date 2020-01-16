# and or no 
# and 逻辑与
# and 逻辑或
# not 逻辑非

""" and 逻辑与 Start """
# 逻辑运算符的运算结果是返回True False
'''
True and True 	----> True
True and False 	----> False
False and True 	----> False
False and False	----> False 

8 > 10 and 6 < 8

Flaes and True  ----> Fales

'admin' == 'admin123' and '123456' == '123456'	----> False
	Fales 						True
'''

n1 = 8
n2 = 5
n3 = 3

result = n1 >= (n2 + n3) and n1 > n2
print(result)
'''
步骤：
1. n1 >= (n2+n3) 	8 >= 8	True
2. n1 > n2			8 >  5	True
3. True and True
4. 结果：True
'''


n2 = n2 + n3
result = n1 >= n2 and n1 == n3
print(result)
'''
步骤：
1. n2 = n2+n3   n2=5+3   n2=8
2. n1 >= n2		8 >= 8		True
3. n1 == n3		8 == 3		False
4. 结果：False
'''


# 此时，n1 = 8, n2 = 8, n3 = 3
n4 = (n1+n3)-n2  # n4 = 3
result = n4<n1 and (n4+n3)>n2
print(result)

""" and 逻辑与 End """


""" or 逻辑或 Start """
# 12:43

