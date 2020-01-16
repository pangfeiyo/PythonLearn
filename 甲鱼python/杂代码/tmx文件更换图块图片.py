import os

# os.chdir 改变工作目录
#f = os.chdir(r"C:\Users\PangFei\Desktop\Debug.win32\res\maps")
#print(f)

#list = []       
#for i in range(len(os.listdir())):  # os.listdir  当前目录下的文件
#    list.append(os.listdir()[i])


#for n in range(len(list)):
#    print(list[n])


#for i in range(1,21):
#    mapX = "map" + str(i) + ".tmx"
#    with open(mapX,'r') as f:
#        f.read()

    #print(f.readline)



os.chdir(r"C:\Users\PangFei\Desktop\Debug.win32\res\maps")

for i in range(1,21):
    mapX = "map" + str(i) + ".tmx"
    file_date = ""

    if i < 11:
        with open(mapX,'r') as f:
            for line in f:
                if "grassland" in line:
                    line = line.replace("grassland", "iceland")
                file_date += line
            #print(file_date)

        with open(mapX,'w') as f:
            f.write(file_date)
        print(mapX + "完成")

    else:
        with open(mapX,'r') as f:
            for line in f:
                if "iceland" in line:
                    line = line.replace("iceland","grassland")
                file_date += line
            #print(file_date)

        with open(mapX,'w') as f:
            f.write(file_date)
        print(mapX + "完成")
        
