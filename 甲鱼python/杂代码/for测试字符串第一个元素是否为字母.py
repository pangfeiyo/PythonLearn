chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
passwd1 = '1fishc.com'
for each in passwd1[0]:
    if each in chars:
        print(each,end=" ")
        break
    else:
        print("ddd")
        break