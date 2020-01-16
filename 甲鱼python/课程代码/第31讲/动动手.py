# 0.编写一个程序，要求使用pickle将文件（record.txt）里的对话按照以下要求腌制成不同文件
#   -- 小甲鱼的对话单独保存为boy_*.txt的文件（去掉"小甲鱼："）
#   -- 小客服的对话单独保存为girl_*.txt的文件（去掉'小客服：'）
#   -- 文件中总共有三段对话，分别保存为boy_1.txt, girl_1.txt, boy_2.txt, girl_2.txt, boy_3.txt, girl_3.txt共6个文件
#   （提示：文件中不同的对话间已经使用'==============='分割）
import pickle

def save_file(boy, girl, count):
    file_name_boy = 'boy_' + str(count) + '.txt'
    file_name_girl = 'girl_' + str(count) + '.txt'

    boy_file = open(file_name_boy, 'wb') # 记得一定要加 b 吖
    girl_file = open(file_name_girl, 'wb') # 记得一定要加 b 吖

    pickle.dump(boy, boy_file)
    pickle.dump(girl, girl_file)

    boy_file.close()
    girl_file.close()

def split_file(file_name):
    count = 1
    boy = []
    girl = []

    f = open(file_name)

    for each_line in f:
        if each_line[:6] != '======':
            # split("：",1)  以"："为分割，分割次数1
            (role, line_spoken) = each_line.split('：', 1)
            if role == '小甲鱼':
                boy.append(line_spoken)
            if role == '小客服':
                girl.append(line_spoken)
        else:
            save_file(boy, girl, count)

            boy = []
            girl = []
            count += 1

    save_file(boy, girl, count)
    f.close()

split_file('record.txt')

# 读取
pickle_file = open('boy_1.txt','rb')
file = pickle.load(pickle_file)
print(file)

