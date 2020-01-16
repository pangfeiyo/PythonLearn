for i in range(10):
    if i % 2 != 0:
        print(i)
        continue        # continue  跳出此次循环，进入下一次循环

    i += 2
    print(i)