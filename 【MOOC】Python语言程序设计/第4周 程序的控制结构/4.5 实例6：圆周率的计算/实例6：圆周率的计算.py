import random
import time

pi = 0
N = 100 # 循环数量/累加数量
for k in range(N):
    # \ 这个是换行符
    pi += 1 / pow(16,k) * (\
        4/(8*k+1) -  2/(8*k+4) - \
        1/(8*k+5) - 1/(8*k+6))
print("圆周率是：{}".format(pi))



DARTS = 1000*1000 # 面积
hits = 0.0  # 在圆内部点的数量
start = time.perf_counter()  # 当前系统时间
for i in range(1, DARTS+1):
    x, y = random.random(), random.random()
    # 计算是否在圆内
    dist = pow(x**2 + y**2, 0.5)
    # 如果小于1.0，在内部
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits/DARTS)
print("圆周率值是：{}".format(pi))
print("运算时间是：{:.5f}s".format(time.perf_counter() - start))
