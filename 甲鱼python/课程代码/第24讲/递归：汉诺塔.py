'''
对于游戏玩法，可以简单分解为三个步骤
——将前 63 个盘子从 X 移动到 Y 上。
——将最底下的第 64 个盘子从 X 移动到 Z 上。
——将 Y 上的 63 个盘子移动到 Z 上。
'''

'''
问题一：将 X 上的 63 个盘子借助 Z 移动到 Y 上；
    - 将前62个盘子从X移动到Z上。                   这里又能将第一和第三问题再次拆解成像问题一与问题二的问题
    - 将最底下的第63个盘子移动到Y上。
    - 将Z上的62个盘子移动到X上。
    
问题二：将 Y 上的 63 个盘子借助 X 移动到 Z 上；
    - 将前62个盘子从Y移动到X上。
    - 将最底下的第63个盘子移动到Z上。
    - 将X上的62个盘子移动到Y上。
'''

# n 代表一共多少盘子，  X Y Z 代表三根针
def hanoi(n,x,y,z):
    if n == 1:
        print(x, "-->", z)
    else:
        hanoi(n-1, x, z, y) # 将前 n-1 个盘子从 X 移动到 Y 上
        print(x, "-->", z) # 将最底下的最后一个盘子从 X 移动到 Z 上
        hanoi(n-1,y, x, z) # 将 Y 上的 n-1 个盘子移动到 Z 上
n = int(input("请输入汉诺塔层数："))
print(hanoi(n, 'X','Y','Z')) 