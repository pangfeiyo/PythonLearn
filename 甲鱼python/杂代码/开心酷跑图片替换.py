import os
import shutil

# 返回当前工作目录
print(os.getcwd())
# 改变工作目录
os.chdir("d:\\")
print(os.getcwd())
#列举指定目录中的文件名   .表示当前目录   ..上级目录
print(os.listdir(path="."))
os.chdir("d:\\项目\\OTT17_HappyTooRush\\0_Design\\地图文件\\prcture2")
print(os.listdir(path="."))

# 把文件复制到另一个文件夹内
# fixed文件替换
mapX = "map"
for i in range(1,6):
    mapX = mapX + str(i)
    shutil.copyfile("d:\\项目\\OTT17_HappyTooRush\\0_Design\\地图文件\\prcture2\\fixed.png",
                    "d:\\项目\\OTT17_HappyTooRush\\0_Design\\地图文件\\" + mapX + "\\prcture2\\fixed.png")
    mapX = "map"




# 地图map文件替换
mapX = "map"
mapY = "map"
for j in range(2,6):
    mapY = mapY + str(j)
    for i in range(1,31):
        mapX = mapX + str(i)
        shutil.copyfile("d:\\项目\\OTT17_HappyTooRush\\0_Design\\地图文件\\map1\\" + mapX + ".tmx",
                        "d:\\项目\\OTT17_HappyTooRush\\0_Design\\地图文件\\" + mapY + "\\" + mapX + ".tmx")
        mapX = "map"
    mapY = "map"