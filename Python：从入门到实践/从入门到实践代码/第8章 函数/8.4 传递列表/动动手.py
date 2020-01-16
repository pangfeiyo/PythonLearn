# 8-9  魔术师 ：创建一个包含魔术师名字的列表，并将其传递给一个名为 show_magicians() 的函数，这个函数打印列表中每个魔术师的名字。
def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())
magicians = ['harry houdini', 'david blaine', 'teller']
show_magicians(magicians)


# 8-10  了不起的魔术师 ：在你为完成练习 8-9 而编写的程序中，编写一个名为 make_great() 的函数，
# 对魔术师列表进行修改，在每个魔术师的名字中都加入字样 “theGreat” 。调用函数 show_magicians() ，确认魔术师列表确实变了。
print("\n8-10")
def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    """给每个魔术师名字中加上 theGreat """
    # Build a new list to hold the great musicians.  建立一个新列表
    great_magicians = []
    # Make each magician great, and add it to great_magicians. 给每个魔术师名字后加上 thrGreat 并加到 great_magicians中
    while magicians:
        magician = magicians.pop()
        great_magician = magician + " theGreat"
        great_magicians.append(great_magician)
    # Add the great magicians back into magicians.  把加上 theGreat的魔术师名字 加到 magicians 中（之前使用 .pop() 导致 magicians 列表已经为空了。
    for great_magician in great_magicians:
        magicians.append(great_magician)

magicians = ['Harry Houdini', 'David Blaine', 'Teller']
show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)


# 8-11  不变的魔术师 ：修改你为完成练习 8-10 而编写的程序，在调用函数 make_great() 时，向它传递魔术师列表的副本。
# 由于不想修改原始列表，请返回修改后的列表，并将其存储到另一个列表中。
# 分别使用这两个列表来调用 show_magicians() ，确认一个列表包含的是原来的魔术师名字，而另一个列表包含的是添加了字样 “the Great” 的魔术师名字。
print("\n8-11")
def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    great_magicians = []
    while magicians:
        magician = magicians.pop()
        great_magician = magician + " thegreat"
        great_magicians.append(great_magician)
    for great_magician in great_magicians:
        magicians.append(great_magician)
    return magicians

magicians = ['Harry Houdini', 'David Blaine', 'Teller']
show_magicians(magicians)

print("\nGreat magicians:")
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

print("\nOriginal magicians:")
show_magicians(magicians)