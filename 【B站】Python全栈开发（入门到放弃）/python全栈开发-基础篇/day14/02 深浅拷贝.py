# s = [1,'alex','alvin']

# s1 = [1,'alex','alvin']
# s1[0] = 2

# print(s)
# print(s1)


'''    拷贝   '''
# s = [1,'alex','alvin']

# s2 = s.copy()
# print(s2)

# s2[0] = 3
# print("s:",s)
# print("s2:",s2)


''' 浅拷贝 ，只拷贝第一层
'''
# s = [[1,2], "alex", "alvin"]
# s3 = s.copy()
# print(s3)

# # s3[1] = 'linux'
# # print("s3:",s3)
# # print("s:",s)

# s3[0][1] = 3
# print("s3:",s3)
# print("s:",s)

husand = ["xiaohu",123,[15000,9000]]

wife = husand.copy()
wife[0] = "xiaopang"
wife[1] = 345

husand[2][1] -= 3000

print(husand)
print(wife)


'''深拷贝，单独一份'''
import copy
xiaosan = copy.deepcopy(husand)
xiaosan[0] = "jinxing"
xiaosan[1] = 666
xiaosan[2][1] -= 1999

print(wife)
print(xiaosan)