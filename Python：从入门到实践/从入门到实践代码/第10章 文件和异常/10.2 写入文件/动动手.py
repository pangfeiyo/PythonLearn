# 10-3  访客 ：编写一个程序，提示用户输入其名字；用户作出响应后，将其名字写入到文件 guest.txt 中。
name = input("what's your name?")
filename = 'guest.txt'
with open(filename,'w') as f:
    f.write(name)    


# 10-4  访客名单 ：编写一个 while 循环，提示用户输入其名字。
# 用户输入其名字后，在屏幕上打印一句问候语，并将一条访问记录添加到文件 guest_book.txt 中。
# 确保这个文件中的每条记录都独占一行。
filename = 'guest_book.txt'
print("Enter 'quit' when you are finished.")
while True:
    name = input("\nWhat's your name?")
    if name =='quit':
        break
    else:
        with open(filename,'a') as f :
            f.write(name + "\n")
        print("Hi " + name + ",you've been added to the guest book.")

        
# 10-5  关于编程的调查 ：编写一个 while 循环，询问用户为何喜欢编程。
# 每当用户输入一个原因后，都将其添加到一个存储所有原因的文件中。
filename = 'programming_poll.txt'
responses = []
while True:
    response = input("\nWhy do you like programming?")
    responses.append(response)

    continue_poll = input("Would you like to let someone else respond?(y/n)")
    if continue_poll != "y":
        break
with open(filename,'a') as f:
    for response in responses:
        f.write(response +"\n")