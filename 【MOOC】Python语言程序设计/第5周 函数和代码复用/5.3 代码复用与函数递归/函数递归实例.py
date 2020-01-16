# 将字符串反转
# 普通方法
s = "python"
print(s[::-1])


# 递归方法：
# - 函数+分支结构
# - 区分哪些是递归链条，哪些是递归基例
def rvs(s):
   if s == "":
       return s
   else:
       return rvs(s[1:]) + s[0]
print(rvs('abc'))


'''
斐波那契数列

        1                 n = 1
F(n) =   1                 n = 2
      F(n-1) + F(n-2)     otherwise

'''
def f(n):
   if n == 1 or n == 2:
       return 1
   else:
       return f(n-1) + f(n-2)


# 汉诺塔
count = 0
def hanoi(n, src, dst, mid):    # 圆盘数量， 第一个柱子， 目的柱子， 中间柱子
    global count
    if n == 1:
        print("{}:{}->{}".format(1, src, dst))
        count += 1
    else:
        hanoi(n-1, src, mid, dst)
        print("{}:{}->{}".format(n, src, dst))
        count += 1
        hanoi(n-1, mid, dst, src)

hanoi(5,"起","目","中")