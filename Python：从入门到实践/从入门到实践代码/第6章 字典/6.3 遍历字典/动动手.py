# 动手试一试
# 6-4  词汇表 2  ：
# 既然你知道了如何遍历字典，现在请整理你为完成练习 6-3 而编写的代码，将其中的一系列 print 语句替换为一个遍历字典中的键和值的循环。
# 确定该循环正确无误后，再在词汇表中添加 5 个 Python 术语。当你再次运行这个程序时，这些新术语及其含义将自动包含在输出中。
glossary = {
    'int':'整型',
    'float':'浮点',
    'bool':'布尔',
    'del':'删除',
    'print':'打印'
}
glossary['for'] = 'for循环'
glossary['if']= '条件判定'
for name,value in glossary.items():
    print(name,":",value)
# 6-5  河流 ：创建一个字典，在其中存储三条大河流及其流经的国家。其中一个键 — 值对可能是 'nile': 'egypt' 。
# 使用循环为每条河流打印一条消息，如 “The Nile runs through Egypt.” 。
# 使用循环将该字典中每条河流的名字都打印出来。
# 使用循环将该字典包含的每个国家的名字都打印出来。
print()
rivers = {
    'changjiang':'china',
    'nile':'egypt',
    'mixixi':'usa'
}
for name,river in rivers.items():
    print('The',name.title(),'runs through',river.title())
print("打印每条河流的名字：") #打印 键
for river in rivers.keys():
    print(river.title())
print("打印每个国家名字：")  #打印 值
for name in rivers.values():
    print(name)
# 6-6  调查 ：在 6.3.1 节编写的程序 favorite_languages.py 中执行以下操作。
# 创建一个应该会接受调查的人员名单，其中有些人已包含在字典中，而其他人未包含在字典中。
# 遍历这个人员名单，对于已参与调查的人，打印一条消息表示感谢。对于还未参与调查的人，打印一条消息邀请他参与调查。
print()
favorite_languages = {
    'jen':'python',
    'sarch':'c',
    'edward':'ruby',
    'phil':'python'
    }
names = ['jen','c','phil','lgd','IG']
for name in names:
    if name in favorite_languages:
        print('Thinks',name.title(),'participate in the investigation')
    else:
        print("We are very hopeful",name.title(),'come he')