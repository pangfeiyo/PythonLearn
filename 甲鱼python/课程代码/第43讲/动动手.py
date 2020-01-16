# 定义一个类，当实例化该类的时候，自动判断传入了多少个参数，并显示出来 
class C:
    # *  传入多余数据保存为元组和列表
    # ** 保存为字典
    def __init__(self, *args):
        if not args:
            print("并没有参数")
        else:
            print("传入了%d个参数，分别是：" % len(args), end="")
            for each in args:
                print(each,end=" ")
c = C(1,2,3,4,5)



# 定义一个单词（Word）类继承自字符串，重写比较操作符（参考：Python魔法方法详解）
# 当两个Word类对象进行比较时，根据单词的长度来进行比较大小
# 加分需求：实例化时如果传入的是带空格的字符串，则取第一个空格前的单词作为参数
# 答：加分需求可以通过重载__new__方法来实现（因为字符串是不可变类型），
# 通过重写__gt__, __lt__, __ge__, __le__方法来定义Word类在比较操作中的表现
# 注意：我们没有定义__eq__和__ne__方法。这是因为将会产生一些怪异不符合逻辑的结果
# （比如Word('FishC')会等于Word('Apple')
class Word(str):
    '''存储单词的类，定义比较单词的几种方法'''
    def __new__(cls, word):
        # 注意我们必须要用到__new__方法，因为str是不可变类型
        # 所以我们必须在创建时将它初始化
        if " " in word:
            print("Value contains spaces. Truncating to first space.")
            # index() 检查字符串中是否包含子字符串，如果指定开始和结束范围，则检查是否包含在指定范围内，如果不在抛出一个异常
            # str.index(str, beg=0, end=len(string))    开始beg  结束end
            # 如果包含子字符串返回开始的（我的理解是这个字符的）索引值，否则抛出异常。
            word = word[:word.index(' ')]   # 单词是第一个空格之前的所有字符
        return str.__new__(cls, word)

    # 定义大于号的行为： x > y 调用 x.__gt__(y)
    def __gt__(self, other):
        return len(self) > len(other)

    # 定义小于号的行为： x < y 调用 x.__lt__(y)
    def __lt__(self, other):
        return len(self) < len(other)
    
    # 定义大于等于号的行为： x >= y 调用 x.__ge__(y)
    def __ge__(self, other):
        return len(self) >= len(other)

    # 定义小于等于号的行为： x <= y 调用 x.__le__(y)
    def __le__(self, other):
        return len(self) <= len(other)

a = Word('FishCas')
b = Word("compu cop")
print(a>b)