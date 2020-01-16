import random



list = ['局长','doom','阿次','皮皮','左手','大壮','胖神','抖s',
        '噜噜','方丈','乐色宗','山主','徐','太一','hero','鸡神',
        '伤口撒盐','whisper','辅助','王如雪']


max = []
maxnum = 0

def rand():
    global maxnum
    n = random.randint(1,100)
    print(i,n)
        
    if n > maxnum:
       maxnum = n
       max.clear()
       max.append(i)
    elif n == maxnum:
        max.append(i)


for i in list:
    rand()
    
print(max)

if len(max) > 1:
    for i in max:
        rand()
            
    
            

print("此次获得至宝的是：",max[0])


    

    
