# 0.按照要求定义一个游乐园门票的类，并尝试计算2个成人+1个小孩平日票价
# -- 平时票价100元
# -- 周末票价为平时的120%
# -- 儿童半票
# 面向对象编程的难点在于思维的转换
class Ticket():
    # weekend 平时或周末   child 是否为儿童
    def __init__(self, weekend = False, child = False):
        self.exp = 100
        if weekend:
            self.inc = 1.2
        else:
            self.inc = 1
        if child:
            self.discount = 0.5
        else:
            self.discount = 1
    def calcPrice(self, num):
        return self.exp * self.inc * self.discount * num
adult = Ticket()
child = Ticket(child = True)
print("2个成人 + 1个小孩平日票价为：%.2f" % (adult.calcPrice(2) + child.calcPrice(1)))


# 0.1 进阶，可以让用户手动输入是否为周末，有几个成人和儿童，求票价
'''有问题，无法解决在外部改变__init__的形参默认值'''
#class Ticket():
#    def __init__(self, weekend = False, child = False):
#        self.exp = 100
#        if weekend:
#            self.inc = 1.2
#        else:
#            self.inc = 1
#        if child:
#            self.discount = 0.5
#        else:
#            self.discount = 1
#    def calcPrice(self, adult_num, child_num):
#        return self.inc * self.exp * adult_num +  self.inc * self.exp * self.discount * child_num


#weekend = input("是否为周末（是或否）？\n")
#adult_num = int(input("请输入成人人数："))
#child_num = int(input("请输入儿童人数："))

#if weekend == 'j':
#    weekend = '周末'
#    Ticket(weekend = True)
#else:
#    weekend = '平日'

#if child_num > 0:
#    Ticket(child = True)

##t = Ticket()

#print("%d个成人和%d个小孩的%s票价为%.2f" % (adult_num, child_num, weekend, Ticket().calcPrice(adult_num, child_num)))




# 1.游戏编程：按以下要求定义一个乌龟类和鱼类并尝试编写游戏
'''
假设游戏场景为范围（x,y）为0 <= x <= 10, 0 <= y <= 10
游戏生成1只乌龟和10条鱼
它们的移动方向均随机
乌龟的最大移动能力是2（可以随机选择1还是2移动），鱼儿最大移动能力是1
当移动到场景边缘，自动向反方向移动 
乌龟初始化体力为100（上限）
乌龟每移动一次，体力消耗1
当乌龟和鱼的坐标重叠，乌龟吃掉鱼，乌龟体力增加20
鱼暂不计算体力
当乌龟体力值为0（挂掉）或鱼儿的数量为0时游戏结束'''
import random as r

legal_x = [0, 10]
legal_y = [0, 10]

class Turtle:
    def __init__(self):
        # 初始体力
        self.power = 100
        # 初始位置随机
        self.x = r.randint(legal_x[0], legal_x[1])
        self.y = r.randint(legal_y[0], legal_y[1])

    def move(self):
        # 随机计算方向并移动到新的位置（x, y）
        new_x = self.x + r.choice([1, 2, -1, -2])
        new_y = self.y + r.choice([1, 2, -1, -2])
        # 检查移动后是否超出场景x轴边界
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x
        # 检查移动后是否超出场景y轴边界
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y        
        # 体力消耗
        self.power -= 1
        # 返回移动后的新位置
        return (self.x, self.y)

    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100

class Fish:
    def __init__(self):
        self.x = r.randint(legal_x[0], legal_x[1])
        self.y = r.randint(legal_y[0], legal_y[1])
        
    def move(self):
        # 随机计算方向并移动到新的位置（x, y）
        new_x = self.x + r.choice([1, -1])
        new_y = self.y + r.choice([1, -1])
        # 检查移动后是否超出场景x轴边界
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x
        # 检查移动后是否超出场景y轴边界
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y
        # 返回移动后的新位置
        return (self.x, self.y)

turtle = Turtle()
fish = []
for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)

while True:
    if not len(fish):
        print("鱼儿都吃完了，游戏结束！")
        break
    if not turtle.power:
        print("乌龟体力耗尽，挂掉了！")
        break

    pos = turtle.move()
    # 在迭代器中删除列表元素是非常危险的，经常会出现意想不到的问题，因为迭代器是直接引用列表的数据进行引用
    # 这里我们把列表拷贝给迭代器，然后对原列表进行删除操作就不会有问题了^_^
    for each_fish in fish[:]:
        if each_fish.move() == pos:
            # 鱼儿被吃掉了
            turtle.eat()
            fish.remove(each_fish)
            print("有一条鱼儿被吃掉了...")
