# 6-1  人 ：使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居住的城市。
# 该字典应包含键 first_name 、 last_name 、 age 和 city 。将存储在该字典中的每项信息都打印出来。
friends = {
    'first_name':'name',
    'last_name':'name2',
    'age':'111',
    'city':'LGD',
    }
print(friends['first_name'].title())
print(friends['last_name'])
print(friends['age'])
print(friends['city'])

print("……")
# 6-2  喜欢的数字 ：使用一个字典来存储一些人喜欢的数字。请想出 5 个人的名字，并将这些名字用作字典中的键；
# 想出每个人喜欢的一个数字，并将这些数字作为值存储在字典中。打印每个人的名字和喜欢的数字。为让这个程序更有趣，通过询问朋友确保数据是真实的。
friends = {
    'lgd':1,
    'lfy':2,
    'nb':3,
    'liuqiu':4,
    }
num = friends['lgd']
print("lgd's favorite number is " + str(num) + ".")

num = friends['lfy']
print("lfy's favorite number is " + str(num) + ".")

num = friends['nb']
print("nb's favorite number is " + str(num) + ".")

num = friends['liuqiu']
print("liuqiu's favorite number is " + str(num) + ".")

print("……")
# 6-3  词汇表 ： Python 字典可用于模拟现实生活中的字典，但为避免混淆，我们将后者称为词汇表。
# 想出你在前面学过的 5 个编程词汇，将它们用作词汇表中的键，并将它们的含义作为值存储在词汇表中。
# 以整洁的方式打印每个词汇及其含义。
# 为此，你可以先打印词汇，在它后面加上一个冒号，再打印词汇的含义；
# 也可在一行打印词汇，再使用换行符（ \n ）插入一个空行，然后在下一行以缩进的方式打印词汇的含义。
glossary = {
    'int':'整型',
    'float':'浮点',
    'bool':'布尔',
    'del':'删除',
    'print':'打印'
}
# 方法一：
# for name,value in glossary.items():
#     print(name+"的含义是：")
#     print("\t",value)

# 方法二：.
word = 'int'
print(word.title() + ": " + glossary[word])

word = 'float'
print(word.title() + ": " + glossary[word])

word = 'bool'
print(word.title() + ": " + glossary[word])

word = 'del'
print(word.title() + ": " + glossary[word])

word = 'print'
print(word.title() + ": " + glossary[word])