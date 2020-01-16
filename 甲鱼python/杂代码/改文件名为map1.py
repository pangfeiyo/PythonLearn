import os
import shutil

# 返回当前工作目录
print(os.getcwd())

# 列举指定目录中的文件名
print(os.listdir())
listdir = os.listdir()


n = range(1,31)
# 判定map1是否存在，如果存在，删除
if os.path.exists("map1.tmx"):
    os.remove("map1.tmx")
for i in n:
    mapX = "map" + str(i) + ".tmx"
    # os.path.exists 判定指定路径（目录和文件）是否存在
    if os.path.exists(mapX):
        print("存在")
        print(mapX)
        # 重命名，前面是旧名，后面是新名
        os.rename(mapX,"map1.tmx")
        
            

        
