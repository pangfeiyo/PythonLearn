#写出五个你想去的地方
destination = ['xian','beijing','dali','yili','heilongjiang']
print(destination)
print("临时排序：",sorted(destination))

print("临时按字母顺序相反排序",sorted(destination,reverse=True))

destination.reverse()
print("直接反序列表元素顺序",destination)
destination.reverse()
print("再反序一次，列表还原",destination)

destination.sort()
print("按字母顺序",destination)

destination.sort(reverse=True)
print("按字母反序",destination)
#destination.sort()
#print(destination)
