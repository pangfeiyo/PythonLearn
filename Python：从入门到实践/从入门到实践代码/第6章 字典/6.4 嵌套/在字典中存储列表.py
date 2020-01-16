# 6.4.2 　在字典中存储列表
# 有时候，需要将列表存储在字典中，而不是将字典存储在列表中。
# 例如，你如何描述顾客点的比萨呢？如果使用列表，只能存储要添加的比萨配料；
# 但如果使用字典，就不仅可在其中包含配料列表，还可包含其他有关比萨的描述。
# 在下面的示例中，存储了比萨的两方面信息：外皮类型和配料列表。其中的配料列表是一个与键 'toppings' 相关联的值。
# 要访问该列表，我们使用字典名和键 'toppings'，就像访问字典中的其他值一样。这将返回一个配料列表，而不是单个值：

# 存储所点比萨的信息
pizza = {
    'crust':'thick',
    'topings':['mushrooms','extra cheese'],
    }
# 描述所点的比萨
print("You ordered a", pizza['crust'], "-crust pizza",
      "with the following toppings:")

for topping in pizza['topings']:
    print("\t" + topping)


# 每当需要在字典中将一个键关联到多个值时，都可以在字典中嵌套一个列表。
# 在本章前面有关喜欢的编程语言的示例中，如果将每个人的回答都存储在一个列表中，被调查者就可选择多种喜欢的语言。在
# 这种情况下，当我们遍历字典时，与每个被调查者相关联的都是一个语言列表，而不是一种语言；
# 因此，在遍历该字典的 for 循环中，我们需要再使用一个 for 循环来遍历与被调查者相关联的语言列表：
print()
favorite_languages = {                  # ❶
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name ,languages in favorite_languages.items():
    # 为进一步改进这个程序，可在遍历字典的for 循环开头添加一条 if 语句，通过查看 len(languages) 的值来确定当前的被调查者喜欢的语言是否有多种。
    # 如果他喜欢的语言有多种，就像以前一样显示输出；如果只有一种，就相应修改输出的措辞，如显示Sarah's favorite language is C 。
    if len(languages) > 1:
        print("\n"+name.title()+"'s favorite languages are:")
        for language in languages:
            print("\t",language.title())
    else:
        print("\n"+ name.title() +"'s favorite language is",language.title())
# 正如你看到的，现在与每个名字相关联的值都是一个列表（见 1 ）。请注意，有些人喜欢的语言只有一种，而有些人有多种。遍历字典时（见❷），我们使用了变量 languages
# 来依次存储字典中的每个值，因为我们知道这些值都是列表。在遍历字典的主循环中，我们又使用了一个 for 循环来遍历每个人喜欢的语言列表（见❸）。现在，每个人想列出
# 多少种喜欢的语言都可以：