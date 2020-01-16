# 8.4 　传递列表
# 你经常会发现，向函数传递列表很有用，这种列表包含的可能是名字、数字或更复杂的对象（如字典）。
# 将列表传递给函数后，函数就能直接访问其内容。下面使用函数来提高处理列表的效率。
# 假设有一个用户列表，我们要问候其中的每位用户。
# 下面的示例将一个名字列表传递给一个名为 greet_users() 的函数，这个函数问候列表中的每个人：
def greet_users(names):
    '''向列表中每位用户都发出简单的问候'''
    for name in names:
        msg = "hello" , name.title()
        print(msg)
username = ['Haha','nono','yesyes']
greet_users(username)

# 8.4.1 　在函数中修改列表
# 将列表传递给函数后，函数就可对其进行修改。
# 在函数中对这个列表所做的任何修改都是永久性的，这让你能够高效地处理大量的数据。
# 来看一家为用户提交的设计制作 3D 打印模型的公司。
# 需要打印的设计存储在一个列表中，打印后移到另一个列表中。下面是在不使用函数的情况下模拟这个过程的代码：
# 首先创建一个列表，其中包含一些打印的设计
print("\n8.4.1")
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
comleted_models = []
# 模拟打印每个设计，直到没有未打印的设计为止
# 打印每个设计后，都将其移动到 comleted_models 中
while unprinted_designs:
    current_designs = unprinted_designs.pop()
    # 模拟根据设计制作3D打印模型的过程
    print("Printing model:",current_designs)
    comleted_models.append(current_designs)
# 显示打印好的所有模型
print("The following models have been printed:")
for completed_model in comleted_models:
    print(completed_model)

# 为重新组织这些代码，我们可编写两个函数，每个都做一件具体的工作。
# 大部分代码都与原来相同，只是效率更高。第一个函数将负责处理打印设计的工作，而第二个将概述打印了哪些设计：
print("重组后代码：")
def print_models(unprinted_designs, completed_models):
    '''
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表 completed_models 中
    '''
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # 模拟根据设计制作3D打印模型的过程
        print("Printing model:", current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    '''显示打印好的所有模型'''
    print("The following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['LGD','IG','LFY']
completed_models = []
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)


# 8.4.2 　禁止函数修改列表
# 有时候，需要禁止函数修改列表。例如，假设像前一个示例那样，你有一个未打印的设计列表，并编写了一个将这些设计移到打印好的模型列表中的函数。
# 你可能会做出这样的决定：即便打印所有设计后，也要保留原来的未打印的设计列表，以供备案。
# 但由于你将所有的设计都移出了 unprinted_designs ，这个列表变成了空的，原来的列表没有了。
# 为解决这个问题，可向函数传递列表的副本而不是原件；这样函数所做的任何修改都只影响副本，而丝毫不影响原件。
# 要将列表的副本传递给函数，可以像下面这样做：
# function_name(list_name[:])
# 切片表示法 [:] 创建列表的副本。在 print_models.py 中，如果不想清空未打印的设计列表，可像下面这样调用 print_models() ：
# print_models(unprinted_designs[:], completed_models)
