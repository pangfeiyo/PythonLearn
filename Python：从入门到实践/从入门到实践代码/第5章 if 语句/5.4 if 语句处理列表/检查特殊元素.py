# 5.4.1 　检查特殊元素
# 本章开头通过一个简单示例演示了如何处理特殊值 'bmw' —— 它需要采用不同的格式进行打印。
# 既然你对条件测试和 if 语句有了大致的认识，下面来进一步研究如何检查列表中的特殊值，并对其做合适的处理。
# 继续使用前面的比萨店示例。这家比萨店在制作比萨时，每添加一种配料都打印一条消息。
# 通过创建一个列表，在其中包含顾客点的配料，并使用一个循环来指出添加到比萨中的配料，可以以极高的效率编写这样的代码：
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
print("Finished making your pizza!")

print()
# 然而，如果比萨店的青椒用完了，该如何处理呢？为妥善地处理这种情况，可在 for 循环中包含一条 if 语句
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry,we are not of green peppers right now.')
    else:
        print("Adding " + requested_topping + ".")
print("Finished making your pizza!")