# 7.3 　使用 while 循环来处理列表和字典
# 到目前为止，我们每次都只处理了一项用户信息：获取用户的输入，再将输入打印出来或作出应答；循环再次运行时，我们获悉另一个输入值并作出响应。
# 然而，要记录大量的用户和信息，需要在 while 循环中使用列表和字典。
# for 循环是一种遍历列表的有效方式，但在 for 循环中不应修改列表，否则将导致 Python 难以跟踪其中的元素。
# 要在遍历列表的同时对其进行修改，可使用 while 循环。通过将 while 循环同列表和字典结合起来使用，可收集、存储并组织大量输入，供以后查看和显示。

# 7.3.1 　在列表之间移动元素
# 假设有一个列表，其中包含新注册但还未验证的网站用户；验证这些用户后，如何将他们移到另一个已验证用户列表中呢？
# 一种办法是使用一个 while 循环，在验证用户的同时将其从未验证用户列表中提取出来，再将其加入到另一个已验证用户列表中。
# 代码可能类似于下面这样：

# 首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfinmed_users = ['alice','brian','candace']
confindmed_users = []
# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的列表都移到已验证用户列表中
while unconfinmed_users:
    current_user = unconfinmed_users.pop()

    print("Verifying user:", current_user.title())
    confindmed_users.append(current_user)
# 显示所有已验证的用户
print("\nThe following users have been confinmed:")
for confinmed_user in confindmed_users:
    print(confinmed_user.title())
print("……")

# 7.3.2 　删除包含特定值的所有列表元素
# 在第 3 章中，我们使用函数 remove() 来删除列表中的特定值，这之所以可行，是因为要删除的值在列表中只出现了一次。
# 如果要删除列表中所有包含特定值的元素，该怎么办呢？
# 假设你有一个宠物列表，其中包含多个值为 'cat' 的元素。
# 要删除所有这些元素，可不断运行一个 while 循环，直到列表中不再包含值 'cat' ，如下所示：
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(set(pets))    # set 去除重复
print("……")

# 7.3.3 　使用用户输入来填充字典
# 可使用 while 循环提示用户输入任意数量的信息。
# 下面来创建一个调查程序，其中的循环每次执行时都提示输入被调查者的名字和回答。
# 我们将收集的数据存储在一个字典中，以便将回答同被调查者关联起来：
responses = {}
# 设置一个标志，指出调查是否继续
polling_active = True
while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("what's your name?")
    response = input("Which mountain would you like to climb someday?")
    # 将答案存储在字典中
    responses[name] = response
    # 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond?(Yes / No)")
    if repeat.lower() == 'no':
        polling_active = False

# 调查结束，显示结果
print("\n--- Poll Results ---")
for name,response in responses.items():
    print(name,"would like to climb", response,".")

