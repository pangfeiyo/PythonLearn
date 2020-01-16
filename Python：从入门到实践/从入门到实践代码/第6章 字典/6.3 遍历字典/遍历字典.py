# 6.3.1 　遍历所有的键 — 值对
# 探索各种遍历方法前，先来看一个新字典，它用于存储有关网站用户的信息。下面的字典存储一名用户的用户名、名和姓：
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
# for 语句的第二部分包含字典名和方法 items() ，它返回一个键 — 值对列表
# Python 字典 items() 方法以列表返回可遍历的(键, 值) 元组数组。
# 返回值   返回可遍历的(键, 值) 元组数组。
for key, value in user_0.items():
    print('\nKey:',key)
    print('value:',value)


# 注意，即便遍历字典时，键 — 值对的返回顺序也与存储顺序不同。 Python 不关心键 — 值对的存储顺序，而只跟踪键和值之间的关联关系。
# 在 6.2.6 节的示例 favorite_languages.py 中，字典存储的是不同人的同一种信息；对于类似这样的字典，遍历所有的键 — 值对很合适。
# 如果遍历字典 favorite_languages ，将得到其中每个人的姓名和喜欢的编程语言。
# 由于其中的键都是人名，而值都是语言，因此我们在循环中使用变量 name 和 language ，而不是 key 和 value ，这让人更容易明白循环的作用：
print('\n人名和语言')
favorite_languages = {
    'jen':'python',
    'sarch':'c',
    'edward':'ruby',
    'phil':'python'
    }
for name,language in favorite_languages.items():
    print(name.title()+"'s favorite language is",language.title())


# 6.3.2 　遍历字典中的所有键
# 在不需要使用字典中的值时，方法 keys() 很有用。
# 下面来遍历字典 favorite_languages ，并将每个被调查者的名字都打印出来：
print('\n遍历字典中的所有键')
favorite_languages = {
    'jen':'python',
    'sarch':'c',
    'edward':'ruby',
    'phil':'python'
    }
# 遍历字典时，会默认遍历所有的键，因此，如果将上述代码中的 for name in favorite_languages.keys(): 替换为 for name in favorite_languages: ，输出将不变。
# 如果显式地使用方法 keys() 可让代码更容易理解，你可以选择这样做，但如果你愿意，也可省略它
for name in favorite_languages.keys():
    print(name.title())

# 在这种循环中，可使用当前键来访问与之相关联的值。下面来打印两条消息，指出两位朋友喜欢的语言。
# 我们像前面一样遍历字典中的名字，但在名字为指定朋友的名字时，打印一条消息，指出其喜欢的语言：
print()
favorite_languages = {
    'jen':'python',
    'sarch':'c',
    'edward':'ruby',
    'phil':'python'
    }
friends = ['phil','sarch']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("  Hi",name.title(),",i see your favorite language is",favorite_languages[name].title(),"!")
# 你还可以使用 keys() 确定某个人是否接受了调查。下面的代码确定 Erin 是否接受了调查：
if 'erin' not in favorite_languages.keys():
    print('Erin,please take our poll!')
# 方法 keys() 并非只能用于遍历；实际上，它返回一个列表，其中包含字典中的所有键，因此上面的代码行只是核实 'erin' 是否包含在这个列表中。
# 由于她并不包含在这个列表中，因此打印一条消息，邀请她参加调查



# 6.3.3 　按顺序遍历字典中的所有键
# 字典总是明确地记录键和值之间的关联关系，但获取字典的元素时，获取顺序是不可预测的。这不是问题，因为通常你想要的只是获取与键相关联的正确的值。
# 要以特定的顺序返回元素，一种办法是在 for 循环中对返回的键进行排序。为此，可使用函数 sorted() 来获得按特定顺序排列的键列表的副本：
print('\n6.3.3 　按顺序遍历字典中的所有键')
favorite_languages = {
    'jen':'python',
    'sarch':'c',
    'edward':'ruby',
    'phil':'python'
    }
# 这条 for 语句类似于其他 for 语句，但对方法 dictionary.keys() 的结果调用了函数 sorted() 。
# 这让 Python 列出字典中的所有键，并在遍历前对这个列表进行排序。输出表明，按顺序显示了所有被调查者的名字：
for name in sorted(favorite_languages.keys()):
    print(name.title()+", thank you for taking the poll.")


# 6.3.4 　遍历字典中的所有值
# 如果你感兴趣的主要是字典包含的值，可使用方法 values() ，它返回一个值列表，而不包含任何键。
# 例如，如果我们想获得一个这样的列表，即其中只包含被调查者选择的各种语言，而不包含被调查者的名字，可以这样做：
print("\n6.3.4 遍历字典中的所有值")
favorite_languages = {
    'jen':'python',
    'sarch':'c',
    'edward':'ruby',
    'phil':'python'
    }
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# 这种做法提取字典中所有的值，而没有考虑是否重复。涉及的值很少时，这也许不是问题，但如果被调查者很多，最终的列表可能包含大量的重复项。
# 为剔除重复项，可使用集合（ set ）。 集合 类似于列表，但每个元素都必须是独一无二的
print('\n提出重复的值')
favorite_languages = {
    'jen':'python',
    'sarch':'c',
    'edward':'ruby',
    'phil':'python'
    }
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())