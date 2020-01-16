# 设每根射出去的箭的从圆心到箭尾的相隔角度是11.5或12

# 初始箭数
initial = 9

# 每根箭间隔
interval = 360/initial

if initial >30:
    print("箭数太多了")
    
if interval < 11.5:
    print("间隔太小")

    
nlist = []
n = int(0)
for i in range(initial):
    nlist.append(int(n))
    n += interval
print("nlist:\n",nlist)


# 将列表转换成 | 相连的列表
m = ("|".join(str(x) for x in nlist))      
print(m)

# 上方推导式转换普通写法
# 无法改变列表的逗号，除非改底层代码（或魔法方法？）
m2 = ""
for i in nlist:
    # 如果是最后一个元素，就不加"|"
    # -1 的原因是 len 是从1开始，index是从0开始
    if nlist.index(i) == len(nlist)-1:
        m2 += str(i)
    else:
        m2 += str(i) + "|"
print("m2:\n"+ m2)


