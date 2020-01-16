# 8.1 　定义函数
# 下面是一个打印问候语的简单函数，名为 greet_user() ：
def greet_user():
    '''显示简单的问候语'''
    print("hello!")
greet_user()


# 8.1.1 　向函数传递信息
# 只需稍作修改，就可以让函数 greet_user() 不仅向用户显示 Hello! ，还将用户的名字用作抬头。为此，可在函数定义 def greet_user() 的括号内添加 username 。
# 通过在这里添加 username ，就可让函数接受你给 username 指定的任何值。现在，这个函数要求你调用它时给 username 指定一个值。
# 调用 greet_user() 时，可将一个名字传递给它，如下所示：
def greet_user(username):
    '''显示简单的问候语'''
    print("Hello",username.title(),"!")
greet_user('Lili')


# 8.1.2 　实参和形参
# 前面定义函数 greet_user() 时，要求给变量 username 指定一个值。调用这个函数并提供这种信息（人名）时，它将打印相应的问候语。
# 在函数 greet_user() 的定义中，变量 username 是一个 形参 —— 函数完成其工作所需的一项信息。在代码 greet_user('jesse') 中，值 'jesse' 是一个 实参 。实参是
# 调用函数时传递给函数的信息。我们调用函数时，将要让函数使用的信息放在括号内。在 greet_user('jesse') 中，将实参 'jesse' 传递给了函数 greet_user() ，这个
# 值被存储在形参 username 中。
# 注意 　大家有时候会形参、实参不分，因此如果你看到有人将函数定义中的变量称为实参或将函数调用中的变量称为形参，不要大惊小怪。

