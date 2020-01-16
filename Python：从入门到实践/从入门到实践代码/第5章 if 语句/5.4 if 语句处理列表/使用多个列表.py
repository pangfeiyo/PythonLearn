# 5.4.3 　使用多个列表
# 顾客的要求往往五花八门，在比萨配料方面尤其如此。如果顾客要在比萨中添加炸薯条，该怎么办呢？
# 可使用列表和 if 语句来确定能否满足顾客的要求。来看看在制作比萨前如何拒绝怪异的配料要求。
# 下面的示例定义了两个列表，其中第一个列表包含比萨店供应的配料，而第二个列表包含顾客点的配料。
# 这次对于 requested_toppings 中的每个元素，都检查它是否是比萨店供应的配料，再决定是否在比萨中添加它：
available_toppings = ('mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese')  # 店家有的，固定，所以用了元组
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']  # 顾客点的
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding",requested_topping)
    else:
        print("Sorry,we don't have",requested_topping)
print('\nFinished making your pizza!')