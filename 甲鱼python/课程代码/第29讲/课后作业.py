# 0.编写一个程序，接受用户的输入并保存为新的文件
# def file_write(file_name):
#     f = open(file_name, 'w')
#     print("请输入内容【单独输入“:w”保存退出】：")
#
#     while True:
#         write_some = input()
#         if write_some != ":w":
#             f.write('%s\n' % write_some)   # %s 字符串格式化   \n 起到了换行的作用
#             # f.write(write_some)     # 因为没有\n ，到文件中不会换行
#         else:
#             break
#     f.close()
# file_name = input("请输入文件名（包括后缀）：")
# file_write(file_name)


# 1.编写一个程序，比较用户输入的两个文件，如果不同，显示出所有不同处的行号与第一个不同字符的位置
# def file_compare(file1, file2):
#     f1 = open(file1)    # 这里不需要对 file1 和 file2 进行写入操作，所以用默认即可
#     f2 = open(file2)
#     count = 0 # 统计行数
#     differ = [] # 统计不一样的数量
#
#     for line1 in f1:
#         line2 = f2.readline()   # 读取并返回一行
#         count += 1
#         if line1 != line2:
#             differ.append(count)
#
#     f1.close()
#     f2.close()
#     return differ
#
# file1 = input("请输入要比较的第一个文件名：")
# file2 = input("请输入要比较的第二个文件名：")
#
# differ = file_compare(file1, file2)
#
# if len(differ) == 0:
#     print("两个文件完全一样！")
# else:
#     print("两个文件共有[%d]处不同" % len(differ))
#     for each in differ:
#         print("第 %d 行不一样" % each)


# 2.编写一个程序，当用户输入文件名和行数（N）后，将该文件的前N行打印到屏幕上
# def five_view(file_name, line_num):
#     print("\n文件%s的前%s的内容如下：" % (file_name, line_num))
#     f = open(file_name)
#     for i in range(int(line_num)):
#         print(f.readline(),end=" ")
#     f.close()
#
# file_name = input(r"请输入要打开的文件（C:\\test.txt）：") # r 是防止字符串转义
# line_num = input("请输入需要显示该文件前几行：")
# five_view(file_name, line_num)


# 3.在上一题的基础上扩展，用户可以随意输入需要显示的行数
# 如输入13：21，显示从 13 行开始到 21 行结束的内容
# def file_view(file_name, line_num):
#     if line_num.strip() == ":":     # strip() 方法用于移除字符串头尾指定的字符（默认为空格）
#         begin = '1'
#         end = '-1'
#
#     (begin, end) = line_num.split(":")
#
#     if begin == "":
#         begin = "1"
#     if end == "":
#         end ="-1"
#
#     if begin =="1" and end =="-1":
#         prompt = "的全文"
#     elif begin == "1":
#         prompt = '从开始到%s' % end
#     elif end =="-1":
#         prompt = '从%s到结束' % begin
#     else:
#         prompt = '从第%s行到第%s行' % (begin, end)
#
#     print("\n文件%s%s的内容如下：\n" % (file_name, prompt))
#
#     begin = int(begin) -1   # -1 是因为程序读数据是从 0 开始
#     end = int(end)
#     lines = end - begin
#
#     f = open(file_name)
#     for i in range(begin):  # 用于消耗掉begin之前的内容，因为前面的不需要打印出来
#         f.readline()        # 读完之后指针会在上一段的末尾，下面开始就是需要打印的内容
#
#     if lines < 0:
#         print(f.read())
#     else:
#         for j in range(lines):
#             print(f.readline(),end="")
#
#     f.close()
#
# file_name = input(r"请输入要打开的文件（C:\\test.txt）：")
# line_num = input("请输入需要显示的行数【格式如 13：21 或 ：21 或 21： 或 ： 】：")
# file_view(file_name, line_num)


# 4.编写一个程序，实现“全部替换”功能
def file_replace(file_name, rep_word, new_word):
    f_read = open(file_name)

    content = []
    count = 0

    for eachline in f_read:
        if rep_word in eachline:
            count = eachline.count(rep_word) + count   # count感觉应该用这个      # count 统计个数    # 为什么还要再 + count ，貌似如果换行的话，就会把之前存储的个数给覆盖掉
            # replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
            # str.replace(old, new[, max])
            eachline = eachline.replace(rep_word,new_word)
        content.append(eachline)

    decide = input("\n文件 %s 中共有%s个【%s】\n您确定要把所有的【%s】替换为【%s】吗？\n[YES/NO]："
                   % (file_name, count, rep_word, rep_word, new_word))

    if decide in ["YES",'Yes','yes']:
        f_write = open(file_name,'w')
        f_write.writelines(content)     #Awritelines
        f_write.close()

    f_read.close()
file_name = input("请输入文件名：")
rep_word = input("请输入需要替换的单词或字符：")
new_word = input("请输入新的单词或字符：")
file_replace(file_name, rep_word, new_word)

