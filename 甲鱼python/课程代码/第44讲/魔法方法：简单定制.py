# 实现一个类的定制
# 基本要求：
# - 定制一个计时器的类
# - start 和 stop 方法代表启动计时和停止计时
# - 假设计时器对象t1，print(t1)和直接调用t1的显示结果
# - 当计时器未启动或已经停止计时，调用stop方法会给予温馨的提示
# - 两个计时器对象可以进行相加： t1 + t2
# - 只能使用提供的有限资源完成
#   - 使用 time 模块的 localtime 方法获取时间
#       扩展阅读： time 模块详解（时间获取和转换）
#   - time.localtime 返回 struct_time　的时间格式
#   - 表现你的类：__str__和__repr__

# __str__
# 被打印的时候，需要字符串的形式输出的时候，就会找到__str__，把其返回值打印出来
class A:
    def __str__(self):
        return "小甲鱼"
a = A()
print(a)

# __repr__
# 和重写__str__类似
class B:
    def __repr__(self):
        return '小甲鱼2'
b = B()
print(b)



# 代码
import time as t
class Mytimer():
    def __init__(self):
        self.unilt = ['年','月','天','小时','分钟','秒']
        self.prompt = "未开始计时！"
        self.lasted = []
        self.begin = 0  # 这里要避免属性和方法名重名
        self.end = 0
    
    def __str__(self):
        return self.prompt

    __repr__ = __str__

    # 两个计时器相加
    def __add__(self, other):
        prompt = "总共运行了"
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unilt[index])
        return prompt
        
    # 开始计时
    def start(self):
        self.begin = t.localtime()
        self.prompt = '提示：请先调用 stop() 停止计时！'
        print("计时开始...") 

    # 停止计时
    def stop(self):
        if not self.begin:
            print("提示：请先调用 start() 进行计时！")
        else:
            self.end = t.localtime()
            self.__calc()
            print("计时结束！")

    # 内部方法，计算运行时间
    def __calc(self):
        self.lasted = []
        self.prompt = "总共运行了"
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:   # 不为0
                self.prompt += (str(self.lasted[index]) + self.unilt[index])
        #为下一轮计时初始化变量
        self.begin = 0
        self.end = 0
        print(self.prompt)

t1 = Mytimer()
t2 = Mytimer()

while True:
    abc = input()
    if abc == 't1.start()':
        t1.start()
    if abc == 't2.start()':
        t2.start()
    if abc == 't1.stop()':
        t1.stop()
    if abc == 't2.stop()':
        t2.stop()
    if abc == 't1+t2':
        print(t1 + t2)
    if abc == 'quit':
        break