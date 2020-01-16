# 用while语句实现以下for语句相同的功能
'''
for each in range(5):
    print(each)
'''
alist = range(5)
it = iter(alist)
while True:
    try:
        print(next(it))
    except StopIteration:
        break


# 写一个迭代器，要求输出至今到2000年为止的所有闰年，如：
'''
>>> leapYears = leapYears()
>>> for i in leapYears:
        if i >= 2000:
            print(i)
        else:
            break

2012
2008
2004
2000

提示：闰年判定法  
    year % 4 == 0 and year % 100 != 0 
or  
    year % 400 == 0
'''
import datetime as dt

class LeapYear:
    def __init__(self):
        self.now = dt.date.today().year

    def isLeapYear(self, year):
        if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
            return True
        else:
            return False
        
    def __iter__(self):
        return self

    def __next__(self):
        while not self.isLeapYear(self.now):
            self.now -= 1 

        temp = self.now
        self.now -= 1
        
        return temp

leapyear = LeapYear()
for each in leapyear:
    if each < 2000:
        break
    else:
        print(each)



# 要求自己写一个MyRev类，功能与reversed()相同
# （内置函数reversed(seq)是返回一个迭代器，是序列seq的逆序显示）
# 例如：
'''
>>> myRev = MyRev("FishC")
>>> for i in myRev:
        print(i, end ="")

ChsiF
'''
class MyRev:
    def __init__(self, date):
        self.date = date 
        self.index = len(date)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration

        self.index = self.index - 1
        return self.date[self.index]

myRev = MyRev("FishC")
for each in myRev:
    print(each)




