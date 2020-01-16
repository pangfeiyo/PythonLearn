# 将文件（recird.txt）中的数据进行分割并按照以下规律保存起来：
# - 小甲鱼的对话单独保存为boy_*.txt的文件（去掉“小甲鱼：”）
# - 小客服的对话单独保存为gril_*.txt的文件（去掉“小客服：”）
# - 文件中总共有三段对话，分别保存为boy_1.txt， gril_1.txt， boy_2.txt, gril_2.txt,
#   boy_3.txt, gril_3.txt 共6个文件（提示：文件中不同的对话间已经使用“=========”分割）
def save_file(boy, girl ,count):
    file_name_boy = 'boy_' + str(count) + ".txt"
    file_name_girl = 'girl_' + str(count) + ".txt"

    boy_file = open(file_name_boy, 'w')
    girl_file = open(file_name_girl, 'w')

    # writelines 可将序列写入文件
    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()


def split_file(file_name):
    # 同一目录下可以这么简写
    f = open(file_name)     # f = open("record.txt")
    #f = open('C:\\Users\\PangFei\\Desktop\\Python学习\\甲鱼python\\课程代码\\第29讲\\record.txt')

    boy = []
    girl = []
    count = 1

    for each_line in f:
        # 如果这一行前6个字符不是 =
        if each_line[:6] != "======":
            # 进行字符串分割操作
            # role 角色  line_spoken　话
            # split()通过指定分隔符对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个“：”
            (role, line_spoken) = each_line.split("：",1)
            if role == "小甲鱼":
                boy.append(line_spoken)
            if role == "小客服":
                girl.append(line_spoken)
        else:
            # 文件的分别保存操作
            save_file(boy, girl, count)

            boy = []
            girl = []
            count += 1

    # 这里再次调用该函数是因为，按上面的 if 所写，遇到 [:6] == "=======" 时才会把“======”以上的对话保存在新建文件中
    # 而第三段对话开始就不会再出现“=======”，如果不再次调用该函数就不会把第三段对话保存在新建文件中
    # 为什么这里调用函数会只保存第三段对话，因为上次读数据时指针读到了第二段======的末尾
    save_file(boy, girl ,count)

    f.close()

split_file("record.txt")