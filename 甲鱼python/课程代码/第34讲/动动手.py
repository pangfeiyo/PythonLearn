# 0.使用with改以下代码，让python去关心文件的打开与关闭
def file_compare(file1, file2):
    # f1 = open(file1)
    # f2 = open(file2)
    with open(file1) as f1, open(file2) as f2:
        count = 0 # 统计行数
        differ = [] # 统计不一样的数量

        for line1 in f1:
            line2 = f2.readline()
            count += 1
            if line1 != line2:
                differ.append(count)

    # f1.close()
    # f2.close()
    return differ

file1 = input('请输入需要比较的头一个文件名：')
file2 = input('请输入需要比较的另一个文件名：')

differ = file_compare(file1, file2)

if len(differ) == 0:
    print('两个文件完全一样！')
else:
    print('两个文件共有【%d】处不同：' % len(differ))
    for each in differ:
        print('第 %d 行不一样' % each)


# 利用异常的原理,修改以下代码
print('|--- 欢迎进入通讯录程序 ---|')
print('|--- 1：查询联系人资料  ---|')
print('|--- 2：插入新的联系人  ---|')
print('|--- 3：删除已有联系人  ---|')
print('|--- 4：退出通讯录程序  ---|')

contacts = dict()

while 1:
    instr = int(input('\n请输入相关的指令代码：'))

    if instr == 1:
        name = input('请输入联系人姓名：')
        # if name in contacts:
        try:
            print(name + ' : ' + contacts[name])
        # else:
        except KeyError:
            print('您输入的姓名不再通讯录中！')

    if instr == 2:
        name = input('请输入联系人姓名：')
        # if name in contacts:
        try:
            contacts[name]  # 有点"为赋新词强说愁"的感觉
            print('您输入的姓名在通讯录中已存在 -->> ', end='')
            print(name + ' : ' + contacts[name])
            if input('是否修改用户资料（YES/NO）：') == 'YES':
                contacts[name] = input('请输入用户联系电话：')
        # else:
        except KeyError:
            contacts[name] = input('请输入用户联系电话：')

    if instr == 3:
        name = input('请输入联系人姓名：')
        # if name in contacts:
        try:
            del (contacts[name])  # 也可以使用dict.pop()
        # else:
        except KeyError:
            print('您输入的联系人不存在。')

    if instr == 4:
        break

print('|--- 感谢使用通讯录程序 ---|')
