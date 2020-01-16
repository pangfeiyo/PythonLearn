# 0.编写一个程序，统计当前目录下每个文件类型的文件数
import os
# os.listdir(path=".") 列举指定目录中的文件名（"."表示当前目录，".."表示上一级目录）
# os.curdir 指代当前目录（"."）
'''写法一 '''
all_files = os.listdir(os.curdir)   # 使用 os.curdir 表示当前目录更标准
# '''写法二 '''all_files = os.listdir('C:\\Users\\PangFei\\Desktop\\Python学习\\甲鱼python\\课程代码\\第29讲')
# '''写法三 '''all_files = os.listdir(input("请输入目录："))
print(all_files)
type_dict = dict()  # 相当于建个空字典

for each_file in all_files:
    # isdir(path) 判断指定路径是否存在且是一个目录
    if os.path.isdir(each_file):
        # .setdefault(key[, default]) 如果key 在字典中，则返回其值。如果没有，则插入值为 default 的 key，并返回default。 default默认为 None
        # 相关内容：.setdefault() 与 get(key[, default])类似，如果 Key 在字典中，返回 key 的值，否则返回 default 的值
        type_dict.setdefault('文件夹',0)
        type_dict['文件夹'] += 1
    else:
        # .splitext(path) 分离文件名与扩展名，返回（f_name, f_extension）元组
        ext = os.path.splitext(each_file)[1]
        type_dict.setdefault(ext,0)
        type_dict[ext] += 1
for each_type in type_dict.keys():
    print("该文件夹下共有类型为【%s】的文件 %d 个" % (each_type, type_dict[each_type]))


# 1.编写一个程序，计算当前文件夹下所有文件的大小
print()
all_files = os.listdir(os.curdir)
file_dict = dict()

for each_file in all_files:
    # .isfile(path) 判断指定路径是否存在且是一个文件
    if os.path.isfile(each_file):
        # os.path.getsize(file) 返回指定文件尺寸，单位是字节
        file_size = os.path.getsize(each_file)
        file_dict[each_file] = file_size
for each in file_dict.items():
    print("%s【%dBytes】" % (each[0], each[1]))



# 2.用户输入文件名以及开始搜索的路径，搜索该文件是否存在。
# 如遇到文件夹，则进入文件夹继续搜索
# def search_file(start_dir, target):
#     # os.chdir(path) 改变工作目录
#     os.chdir(start_dir)
#
#     # os.listdir(path='.') 列举指定目录中的文件名。     os.curdir 指当前目录
#     for each_file in os.listdir(os.curdir):
#         if each_file == target:
#             # .getcwd() 返回当前工作目录。 os.sep 输出操作系统特定的路径分隔符（win下是'\\',linux下为'/'）
#             print(os.getcwd() + os.sep + each_file) # 使用os.sep 使程序更标准（试验后不加的话最后each_file前没有\\，这样路径是错的）
#         # os.path.isdir 判断指定路径是否存在且是一个目录
#         if os.path.isdir(each_file):
#             search_file(each_file, target) # 递归调用
#             # os.pardir 指代上一级目录（'..'）
#             os.chdir(os.pardir) # 递归调用后切记返回上一层目录
# start_dir = input("\n请输入待查找的初始目录：")
# target = input("请输入需要查找的目标文件：")
# search_file(start_dir, target)


# 3.用户输入开始搜索的路径，查找该路径下（包含子文件夹内）所有视频格式文件（要求查找mp4,rmvb,avi的格式即可）
# 并把创建一个文件（vedioList.txt)存放所有找到的文件的路径
def search_file(start_file, target):
    # os.chdir(path) 改变工作目录
    os.chdir(start_file)

    # os.listdir(path='.') 列举指定目录中的文件名。     os.curdir 指当前目录
    for each_file in os.listdir(os.curdir):
        # .splitext(path) 分离文件名与扩展名，返回（f_name, f_extension）元组
        ext = os.path.splitext(each_file)[1]
        if ext in target:
            # os.getcwd() 返回当前工作目录
            # 通过试验，如果下面的语句在最后不用"\n"，而采用os.linesep，那么在编号为4的程序中代码读文件vedioList.txt时会读完第一行后每行行数+1
            vedio_list.append(os.getcwd() + os.sep + each_file + "\n") # 使用os.sep使程序更标准    os.linesep 当前平台终止符（win为'\r\n'）
        # os.path.isdir 判断指定路径是否存在且是一个目录
        if os.path.isdir(each_file):
            search_file(each_file, target)  # 递归调用
            # os.pardir 指代上一级目录（'..'）
            os.chdir(os.pardir) # 递归调用后切记返回上一层目录
start_dir = input("\n请输入待查找的初始目录：")
program_dir = os.getcwd()   # os.getcwd() 返回当前目录

target = ['.mp4','.avi','.rmvb','.mp3']
vedio_list = []

search_file(start_dir, target)

f = open(program_dir + os.sep + 'vedioList.txt','w')
f.writelines(vedio_list)
f.close()



# 4.用户输入关键字，查找当前文件夹内（如果当前文件夹内包含文件夹，则进入文件夹继续搜索）所有含有该关键字的文本文件
# 要求显示该文件所在的位置及关键字在文件中的具体位置（第几行第几个字符）
# 从search_files转到这里
def search_in_file(file_name, key):
    # 传入进来的file_name是.txt文件的路径， key是关键字
    f = open(file_name)
    count = 0  # 记录行数
    key_dict = dict()  # 字典，用户存放key所在具体行数对应具体位置

    for each_line in f:
        count += 1
        if key in each_line:
            pos = pos_in_line(each_line, key)  # key在每行对应的位置
            key_dict[count] = pos
    f.close()
    return key_dict

# 从search_in_file转到这里
def pos_in_line(line, key):
    # line，当前行的内容。   key，关键字
    pos = []
    # str.find(str, beg=0, end=len(string))
    # find()方法检测字符串中是否包含子字符串str，如果指定beg（开始）和end（结束）范围，则检查是否包含在指定范围内，
    # 如果指定范围内如果包含指定索引值，返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1。
    begin = line.find(key)
    while begin != -1:
        pos.append(begin + 1)  # 用户的角度是从1开始数
        begin = line.find(key, begin + 1)  # 从下一个位置继续查找
    return pos

def print_pos(key_dict):    # 从search_files转来
    keys = key_dict.keys()
    keys = sorted(keys)  # 由于字典是无序的，我们这里对行数进行排序
    for each_key in keys:
        print('关键字出现在第 %s 行，第 %s 个位置。' % (each_key, str(key_dict[each_key])))

def search_files(key, detail):
    # 从这里开始
    # os.walk(top) 遍历top路径下所有子目录，返回一个三元组：（路径, [包含目录], [包含文件]）
    all_files = os.walk(os.getcwd())
    txt_files = []

    for i in all_files:
        # i[2] 文件名
        for each_file in i[2]:
            # 分离文件名与扩展名，返回一个元组
            if os.path.splitext(each_file)[1] == '.txt':  # 根据后缀判断是否文本文件
                # os.path.join 讲path1,和path2组合成一个路径名
                each_file = os.path.join(i[0], each_file)
                txt_files.append(each_file) # 这个列表内是带.txt文件的路径

    for each_txt_file in txt_files:
        key_dict = search_in_file(each_txt_file, key)
        if key_dict:
            print('================================================================')
            print('在文件【%s】中找到关键字【%s】' % (each_txt_file, key))
            if detail in ['YES', 'Yes', 'yes']:
                print_pos(key_dict)

key = input('\n请将该脚本放于待查找的文件夹内，请输入关键字：')
detail = input('请问是否需要打印关键字【%s】在文件中的具体位置（YES/NO）：' % key)
search_files(key, detail)
