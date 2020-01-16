import random

# 敌人ID
enemy = [1,2,3,4,5,6,7,8,9,10,11,12]

enemys = []
enemylist = []

# 波数
waves = 6

# in range(5) 解释 有多少关，就range()多少，比如6共有8关，就写range(8)
# 全选粘贴到单元格，自动换后一格换下一行
# 功能不齐全，只能写有6波的关卡数总和
for nn in range(8):
    for w in range(waves):
        # 每波数量
        wavesnum = random.randint(4,8)

        for i in range(wavesnum):
            # random.choice 从列表中随机
            r = random.choice(enemy)
            enemys.append(r)
            
        enemylist.append(enemys)
        enemys = []

print("enemylist",enemylist)

s = ""

# m = 0 ，记数，因为每6波就是一个关卡，
# 当m=6时，就要给 s 加上一个 \n，这样来区分每个关卡
m = 0
for x in enemylist:
    m += 1
    n = 0
    for y in x:
        n += 1
        if n == len(x):
            s += str(y)
        else:
            s += str(y) + "|"
    # \t 的原因，加了\t之后，粘贴到excel中可以往后一个单元格自动粘贴
    # \n 的话，只能自动往下
    s += "\t"
    # 看上面m=0的注释
    if m % 6 == 0:
        s += "\n"
    
print("s:\n"+s)




# 代码简化
'''
enemy = [1,2]
waves = 3
waverng = (4,8)

wavenums = [random.randint(*waverng) for _ in range(waves)]
enemylist = [[random.choice(enemy) for i in range(w)]
              for w in wavenums]

print("enemylist:", enemylist)
print("s:\n", '\n'.join([str(e)[1:-1].replace(',', '|')
                         for e in enemylist]), sep = "")
'''
