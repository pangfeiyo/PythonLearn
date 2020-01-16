import random
# 包括两类函数，常用共8个
# - 基本随机函数：seed(), random()
# - 扩展随机函数：randint(), getrandbits(), uniform()
#                 randrange(), choice(), shuffle()

# random.seed(10) 给一个随机数种子，用于可复现随机数操作
# seed(10)之后，random.random()  0.571    下次再遇到seed(10)，random()还是0.571
'''random.seed(10)
print(random.random())
print(random.random())
random.seed(10)
print(random.random())'''

'''但是这里用了random.seed(10)之后，后面的随机数据都成固定的了'''

# randint(a, b)  生成一个[a,b]之间的整数
print("randint:",random.randint(10,100))

# randrange(m, n[, k])  生成一个[m, n)之间以k为步长的随机整数
print("randrange:",random.randrange(10, 100, 10))

# getrandbits(k)  生成一个k比特长的随机整数
print("getrandbits:",random.getrandbits(16))

# uniform(a, b)  生成一个[a,b]之间的随机小数
print("uniform:", random.uniform(10, 100))

# choice(seq)  从序列seq中随机选择一个元素
print("choice:", random.choice([1,2,3,4,5,6,7,8]))

# shuffle(seq)  将序列seq中元素随机排列，返回打乱后的序列
s = [1,2,3,4,5,6,7,8,9]
random.shuffle(s)
print("shuffle:", s)
