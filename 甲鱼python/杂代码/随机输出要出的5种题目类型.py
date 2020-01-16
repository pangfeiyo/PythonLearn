import random
n = random.randint(0,4)
list1 = ['数学','理化','生物','天文','地理']
list2 = [0,0,0,0,0]
list3 = [40,40,40,40,40]
number = 200-13

for i in range(0, 300):
    rc = random.choice(list1)
    if rc == list1[0]:
        if list2[0] < list3[0]:
            list2[0] += 1
            print(rc)
        else:
            continue
    if rc == list1[1]:
        if list2[1] < list3[1]:
            list2[1] += 1
            print(rc)
        else:
            continue
    if rc == list1[2]:
        if list2[2] < list3[2]:
            list2[2] += 1
            print(rc)
        else:
            continue
    if rc == list1[3]:
        if list2[3] < list3[3]:
            list2[3] += 1
            print(rc)
        else:
            continue
    if rc == list1[4]:
        if list2[4] < list3[4]:
            list2[4] += 1
            print(rc)
        else:
            continue
    




#while True:
#    if n == 0 and list2[n] < list3[n]:
#        print("数学")
#        list2[0] += 1

#    if n == 1 and list2[n] < list3[n]:
#        print("理化")
#        list2[1] += 1

#    if n == 2 and list2[n] < list3[n]:
#        print("生物")
#        list2[2] += 1

#    if n == 3 and list2[n] < list3[n]:
#        print("天文")
#        list2[3] += 1

#    if n == 4 and list2[n] < list3[n]:
#        print("地理")
#        list2[4] += 1


#print(list2)
