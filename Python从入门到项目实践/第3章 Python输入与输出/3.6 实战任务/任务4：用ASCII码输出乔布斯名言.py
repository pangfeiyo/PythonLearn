# Stay hungry, Stay foolish
stra =""     # 定义连接后的字符串
while True:
    # 用户输入内容，转换成ASCII码输出
    a = input("请输入一个字符: ")
    stra = stra + str(ord(a)) + " "  # 连接字符串
    print(stra)         # 打印连接后的字符串

'''
输出结果：
83 116 97 121 32 104 117 110 103 114 121 44 
83 116 97 121 32 102 111 111 108 105 115 104 46 
'''