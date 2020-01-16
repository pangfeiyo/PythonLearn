#  , 和 + 的区别
names = [1,2]         #这里  names = [1,2,3,4]  和  names = ['1','2','3','4']  是有区别的
for name in names:
    print("hello" , name)   #  names 是 int 型列表   而 print("hello") 这里是 str() 类型，如果使用   ,  不需要改 name 的类型，会直接输出，并会出现一个空格
for name in names:
    print("hello" + name)   #  如果使用 +  则必须左右两边属于同一类型  这里就需要把 name  转为   str(name)
                             #  如果前面定义的 names  是  name = ['1','2']  则不需要把 name  换 str()

