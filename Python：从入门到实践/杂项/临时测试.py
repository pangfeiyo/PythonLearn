from random import randint


b =[]
for i in range(10):
    a1 = randint(1,6)
    a2 = randint(1,6)
    print("a1:", a1)
    print("a2:", a2)
    s = a1 + a2
    b.append(s)

print(b)


cc = [1,2,3,5]
print(len(cc))

for v in range(len(cc)):
    print(v)