# 5.4.2 　确定列表不是空的
# 到目前为止，对于处理的每个列表都做了一个简单的假设，即假设它们都至少包含一个元素。
# 我们马上就要让用户来提供存储在列表中的信息，因此不能再假设循环运行时列表不是空的。
# 有鉴于此，在运行 for 循环前确定列表是否为空很重要。
# 下面在制作比萨前检查顾客点的配料列表是否为空。
# 如果列表是空的，就向顾客确认他是否要点普通比萨；如果列表不为空，就像前面的示例那样制作比萨：
requested_toppings = []
# 在 if 语句中将列表名用在条件表达式中时， Python 将在列表至少包含一个元素时返回 True ，并在列表为空时返回 False 。
if requested_toppings:      # 这里列表为空，所以为 False
    for requested_topping in requested_toppings:
        print('Adding',requested_topping)
    print('Finished making your pizza!')
else:
    print("Are you sure you want a plain pizza?")