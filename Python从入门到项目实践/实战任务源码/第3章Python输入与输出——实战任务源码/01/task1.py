# *_* coding： UTF-8 *_*
# 开发团队：明日科技
# 明日学院网站：www.mingrisoft.com
# 开发工具：PyCharm
# 任务1：输出字母、数字或符号的ASCII状态值

while True:
    # 用户输入字符
    c = input("请输入单个字符: ")
    # 判断字符长度
    if len(c) >= 2:
        # 打印提示信息
        print("字符长度超出范围，请输入单个字符！")
    else:
        # 打印ASCII 码
        print(c + " 的ASCII 码为", ord(c))
