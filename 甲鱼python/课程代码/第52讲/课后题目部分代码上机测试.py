
country_counter = {}

def addone(country):
    if country in country_counter:
        country_counter[country] += 1
    else:
        country_counter[country] = 1

addone('china')
addone('china')
addone('japan')
addone('american')

print(country_counter)
print(len(country_counter))



dict1 = {}
dict1[1] = 1
print(dict1)

dict1 = {}
dict1["1"] = 2
print(dict1)

dict1 = {}
dict1[1.0] = 3
print(dict1)


dict2 = {}
dict2[1] = 1
dict2["5"] = 2
dict2[1.0] = 3
print(dict2)

print()
result = 0
for each in dict2:
    print("\neach:" ,each)
    print("dict2[each]",dict2[each])
    result += dict2[each]

print("\nresult:",result)
print()

for each in dict2:
    print("each",each)

print()
for each in dict2:
    print("dict2[each]",dict2[each])



print("\n")
class A:
    def __init__(self, a, b, c):
        self.x = a + b + c 

a = A(1,2,3)
b = getattr(a, 'x')
print(b)
setattr(a, 'x', b+1)
b = getattr(a, 'x')
print(b)



print("\n")

list1 = [1,2]
list2 = [3,4]

dict1 = {"1":list1, "2":list2}
dict2 = dict1.copy()
dict3 = dict1

print(dict1)
print(dict2)


dict1["1"][0] = 5
print("\n" + str(dict1))
print(dict2)
print(dict3)

#class CCC:
#    def a(self):
#        self.a = 1
#        self.b = 2
#        self.c = 3

#    def b(self,x):
#        self.x = x+ self.a

#c = CCC()
#c.b(10)
#print(c.x)