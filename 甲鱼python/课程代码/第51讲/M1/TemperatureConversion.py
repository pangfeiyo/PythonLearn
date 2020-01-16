# 摄转华
def c2f(cel):
    fah = cel * 1.8 +32 
    return fah

# 华转摄
def f2c(fah):
    cel = (fah - 32) / 1.8
    return cel

# 每一个模块写完之后都应该有一个测试
def test():
    print("测试，0摄氏度 = %.2f华氏度" % c2f(0))
    print("测试，0华氏度 = %.2f摄氏度" % f2c(0))

if __name__ == "__main__":
    test()
