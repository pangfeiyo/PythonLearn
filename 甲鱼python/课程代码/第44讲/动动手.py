# 代码改进
# 如果开始计时时间为2022年2月22日16：30：30 ，停止时间是2025年1月23日15：30：30
# 按照用停止时间减开始时间的计算方式就会出现负数
# 一个月的天数不固定
# 是否考虑闰年

# 解决方案（Pthon官方推荐）
# 用time模块的 perf_counter() 和 process_time() 来计算，
# 其中 perf_counter()返回计时器的精准时间（系统的运行时间）
# process_time()返回当前进程执行CPU的时间总和

# 改进：这次使用 perf_counter() 和 process_time() 作为计时器
# 另外增加一个 set_timer()方法，用于设置默认计时器
# （默认是 perf_counter()，可以通过此方法修改为 process_time()）

# 再次改进，能够统计一个函数运行若干次的时间
# 要求一：函数调用的次数可以设置（默认是1000000次）
# 要求二：新增一个timing()方法，用于启动计时器
import time as t
class MyTimer:
    def __init__(self):
        self.unit = ['年','月','天','小时','分钟','秒']
        self.borrow = [0,12,31,24,60,60]
        self.prompt = "未开始计时！"
        self.lasted = []
        self.begin = 0
        self.end = 0

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def __add__(self,other):
        prompt = '总共运行了'
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index] + self.unit[index])
        return prompt

    # 开始计时
    def start(self):
        self.begin = t.localtime()
        self.prompt = '提示：请先调用 stop()停止计时！'
        print("计时开始...")

    # 停止计时
    def stop(self):
        if not self.begin:
            print("提示：请先调用 start()进行计时！")
        else:
            self.end = t.localtime()
            self.__calc()
            print("计时结束！")

    # 内部方法，计算运行时间
    def __calc(self):
        self.lasted = []
        self.prompt = '总共运行了'
        for index in range(6):
            temp = self.end[index] - self.begin[index]

            # 低位不够减，需向高位借位
            if temp < 0:
                # 测试高位是否有得“借”，没得借的话向再高位借
                i = 1 
                while self.lasted[index-i] < 1:
                    self.lasted[index-i] += self.borrow[index-i] -1
                    self.lasted[index-i-1] -= 1
                    i += 1
                
                self.lasted.append(self.borrow[index] + temp )
                self.lasted[index-1] -= 1
            else:
                self.lasted.append(temp)

        # 由于高位随时会被借位，所以打印要放在最后 
        for index in range(6):
            if self.lasted[index]:
                self.prompt += str(self.lasted[index]) + self.unit[index]

        # 为下一轮计时初始化变量
        self.begin = 0
        self.end = 0



        