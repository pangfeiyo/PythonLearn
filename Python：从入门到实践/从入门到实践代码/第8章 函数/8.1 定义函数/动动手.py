# 8-1  消息 ：编写一个名为 display_message() 的函数，它打印一个句子，指出你在本章学的是什么。调用这个函数，确认显示的消息正确无误。
def display_message(course):
    print("本章学的是：",course)
display_message('函数')

# 8-2  喜欢的图书 ：编写一个名为 favorite_book() 的函数，其中包含一个名为 title 的形参。
# 这个函数打印一条消息，如 One of my favorite books isAlice in Wonderland 。
# 调用这个函数，并将一本图书的名称作为实参传递给它。
def favorite_book(title):
    print(" One of my favorite books isAlice in Wonderland ",title)
favorite_book('简爱')