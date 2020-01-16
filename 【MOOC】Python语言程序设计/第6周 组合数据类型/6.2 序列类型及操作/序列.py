'''
序列类型定义：
序列具有先后关系的一组元素
  - 序列是一维元素向量，元素类型可以不同
  - 类似数学元素序列：S0,S1,....,Sn-1
  - 元素间由序号引导，通过下标访问序列的特定元素

操作符：
x in s      如果 x 是序列s的元素，返回True，否则返回False
x not in s  如果 x 是序列s的元素，返回False，否则返回True
s + t       连接两个序列s和t
s * n 或n * s    将序列 s 复制n次
s[i]        索引，返回s中的第i个元素，i是序列的序号
s[i:j] 或 s[i:j:k]   切片，返回序列s中第i到j以k为步长的元素子序列
'''
ls = ["python", 123, ".io"]
print(ls[::-1])
s = "python123.io"
print(s[::-1])


'''
len(s)      返回序列s的长度
min(s)      返回序列s的最小元素，s中元素需要可比较
max(s)      返回序列s的最大元素，s中元素需要可比较
s.index(x) 或 s.index(x,i,j)     返回序列s从i开始到位置j中第一次出现元素x的位置
s.count(x)  返回序列s中出现x的总次数
'''
ls = ["python", 123, ".io"]
print(len(ls))
s = "python123.io"
print(max(s))


'''
元组类型定义：
元组是序列类型的一种扩展
  - 元组是一种序列类型，一旦创建就不能被修改
  - 使用小括号() 或 tuple() 创建，元素间用逗号,分隔
  - 可以使用或不使用小括号
'''
def func():
    return 1,2
print(func())

creature = 'cat','dog','tiger','human'
print(creature)
color = (0x001100,'blue', creature)
print(color)

'''
元组类型操作：
  - 元组继续序列类型的全部通用操作
  - 元组因为创建后不能被修改，因此没有特殊操作
  - 使用或不使用括号
'''
creature = 'cat','dog','tiger','human'
print(creature[::-1])
color = (0x001100,'blue', creature)
print(color[-1][2])


'''
序列类型应用场景：
  - 元组用于元素不改变的应用场景，更多用于固定搭配场景
  - 列表更加灵活，它是最常用的序列类型
  - 最主要作用：表示一组有序数据，进而操作它们
  
元素遍历
for item in ls:
    <语句块>
'''