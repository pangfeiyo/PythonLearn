import math
members = {'毛毛':[179,41,21],
           '小砾':[218,40,26],
           '阿奇':[203,44,38],
           '灰灰':[193,60,41],
           '路马':[230,48,37],
           '天天':[205,36,40]
           }
# 当前血量不太够，放大点
for value in members.values():
    value[0] = value[0] * 1

enemy = {'杰瑞':[141,52,34],
         '小丑鱼':[217,35,19],
         '乌龟':[223,50,35]}

# for value in enemy.values():
#     value[0] = math.ceil(value[0] /3)
#     value[1] = math.ceil(value[1] /3)
#     value[2] = math.ceil(value[2] /3)
# print(enemy)
for value in enemy.values():
    count = 0
    while count < len(value) :
        value[count] = math.ceil(value[count] / 1)
        count += 1
print(enemy)


mem_name = '灰灰'
mem_hp = 0
mem_attack = 0  #攻击
mem_defense = 0 # 防御

en_name = '乌龟'
en_hp = 0
en_attack = 0
en_defense = 0

for mem_value in members.values():
    mem_hp = members[mem_name][0]
    mem_attack = members[mem_name][1]
    mem_defense = members[mem_name][2]
    break

for en_value in enemy.values():
    en_hp = enemy[en_name][0]
    en_attack = enemy[en_name][1]
    en_defense = enemy[en_name][2]
    break

mem_hurt = (mem_attack * 100 / (100 + en_defense))//1
en_hurt = (en_attack * 100 / (100 + mem_defense))//1

# 敌人的血量能抵挡几次伤害
# math模块中的math.ceil 向上取整，只要小数部位>0，整数+1
en_hp_resist = math.ceil(en_hp / mem_hurt)
# if en_hp_resist > int(en_hp_resist):
#     en_hp_resist = en_hp_resist // 1 + 1

# 角色的血量能抵挡几次伤害
mem_hp_resist = math.ceil(mem_hp/ en_hurt)
# if mem_hp_resist > int(mem_hp_resist):
#     mem_hp_resist = mem_hp_resist // 1 + 1

print("角色[%s]对敌人[%s]造成的伤害是：%s" % (mem_name, en_name, mem_hurt))
print("    [%s]的总血量是%s，一共可以抵挡%s下伤害" % (en_name, en_hp, en_hp_resist))

print("\n敌人[%s]对角色[%s]造成的伤害是：%s" % (en_name, mem_name, en_hurt))
print("    [%s]的总血量是%s，一共可以抵挡%s下伤害" % (mem_name, mem_hp, mem_hp_resist))
# mem_hp = members[mem_name]
# print(mem_hp)


