#使用方法 sort() 对列表进行永久性排序
cars = ['bmw','audi','toyota','subaru']
cars.sort()    #排序，按照字母顺序，应该是按照ascii码（猜测
print(cars)
#按字母顺序反序排序
cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)   #reverse  相反               reverse()只是反转列表元素顺序，reverse()改变后若想恢复到原来的排序只需再次reverse() 即可
print(cars)

#直接列表元素反序排序  .reverse()
print(),print("直接反序打印")
cars = ['bmw','audi','toyota','subaru']
cars.reverse()
print(cars)

print()
#临时排序
#使用 sorted()
cars = ['bmw','audi','toyota','subaru']
print('Here is the original list:')
print(cars)
print('Here is the sorted list:')
print(sorted(cars))                 #临时排序
print('Here is the sorted reverse list again:')
print(sorted(cars,reverse=True))    #临时反向排序
print('Here is the original list again:')
print(cars)

#确定列表长度，使用len
#python 计算列表长度时从1 开始
print(),print('确定列表长度，使用len')
cars = ['bmw','audi','toyota','subaru']
print(len(cars))
