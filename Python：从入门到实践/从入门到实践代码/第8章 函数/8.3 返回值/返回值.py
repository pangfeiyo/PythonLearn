# 8.3 　返回值
# 函数并非总是直接显示输出，相反，它可以处理一些数据，并返回一个或一组值。函数返回的值被称为 返回值 。
# 在函数中，可使用 return 语句将值返回到调用函数的代码行。
# 返回值让你能够将程序的大部分繁重工作移到函数中去完成，从而简化主程序。
# 8.3.1 　返回简单值
# 下面来看一个函数，它接受名和姓并返回整洁的姓名：
def get_formatted_name(first_name, last_name):
    '''返回整洁的姓名'''
    full_name = first_name + last_name
    return full_name.title()
musician = get_formatted_name('王','阳明')
print(musician)

# 8.3.2 　让实参变成可选的
# 有时候，需要让实参变成可选的，这样使用函数的人就只需在必要时才提供额外的信息。可使用默认值来让实参变成可选的。
# 例如，假设我们要扩展函数 get_formatted_name() ，使其还处理中间名。为此，可将其修改成类似于下面这样：
print("8.3.2")
def get_formatted_name(first_name, middle_name, last_name):
    '''返回整洁的姓名'''
    full_name = first_name + " " + middle_name + " " + last_name
    return full_name.title()
musician = get_formatted_name('john','lee','hooker')
print(musician)
# 然而，并非所有的人都有中间名，但如果你调用这个函数时只提供了名和姓，它将不能正确地运行。
# 为让中间名变成可选的，可给实参 middle_name 指定一个默认值 —— 空字符串，并在用户没有提供中间名时不使用这个实参。
# 为让 get_formatted_name() 在没有提供中间名时依然可行，可给实参 middle_name 指定一个默认值 —— 空字符串，并将其移到形参列表的末尾：
def get_formatted_name(first_name, last_name, middle_name=""):
    '''返回整洁的姓名'''
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name
musician = get_formatted_name('jimi','hendrix')
print(musician)

musician = get_formatted_name('john','hooker','lee')
print(musician)


# 8.3.3 　返回字典
# 函数可返回任何类型的值，包括列表和字典等较复杂的数据结构。例如，下面的函数接受姓名的组成部分，并返回一个表示人的字典：
print("8.3.3")
def build_person(first_name, last_name):
    '''返回一个字典，其中包含有关一个人的信息'''
    person = {'first_name':first_name, 'last_name':last_name}
    return person
musician = build_person('jimi','hendrix')
print(musician)
# 这个函数接受简单的文本信息，将其放在一个更合适的数据结构中，让你不仅能打印这些信息，还能以其他方式处理它们。
# 当前，字符串 'jimi' 和 'hendrix' 被标记为名和姓。
# 你可以轻松地扩展这个函数，使其接受可选值，如中间名、年龄、职业或你要存储的其他任何信息。例如，下面的修改让你还能存储年龄：
def build_person(first_name, last_name, age=""):
    '''返回一个字典，其中包含有关一个人的信息'''
    person = {'first_name':first_name, 'last_name':last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi','hendrix',age='27')
print(musician)


# 8.3.4 　结合使用函数和 while  循环
# 可将函数同本书前面介绍的任何 Python 结构结合起来使用。
# 例如，下面将结合使用函数 get_formatted_name() 和 while 循环，以更正规的方式问候用户。
# 下面尝试使用名和姓跟用户打招呼：
def get_formatted_name(first_name, last_name):
    '''返回整洁的姓名'''
    full_name = first_name + last_name
    return full_name.title()
# 这是一个无限循环
while True:
    print("\nPlease tell me your name:")
    f_name = input("First_name:")
    # 但这个while 循环存在一个问题：没有定义退出条件。请用户提供一系列输入时，该在什么地方提供退出条件呢？我们要让用户能够尽可能容易地退出，因此每次提示用户输入
    # 时，都应提供退出途径。每次提示用户输入时，都使用break语句提供了退出循环的简单途径：
    if f_name == 'q':
        break

    l_name = input("Last_name:")
    if l_name == "q":
        break

    formatted_name = get_formatted_name(f_name,l_name)
    print("Hello",formatted_name)
