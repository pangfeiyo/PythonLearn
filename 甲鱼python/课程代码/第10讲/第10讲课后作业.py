member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
for i in member:
    print(i)

print()
print("方法一")
#修改上面的打印结果使得更好看
#方法一
count = 0
length = len(member)
while count < length:
    print(member[count],member[count+1])
    count += 2


print()
print("方法二")
#方法二
for each in range(len(member)):
    if each % 2 == 0:
        print(member[each],member[each+1])