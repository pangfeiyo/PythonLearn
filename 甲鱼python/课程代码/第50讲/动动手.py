# python支持一小部分常量，如True False None等
# 创建一个const模块，让python支持常量
import const

const.NAME = "FishC"
print(const.NAME)

try:
    # 尝试修改常量
    const.NAME = "FishC.com"
except TypeError as Err:
    print(Err)

try:
    # 变量名需要大写
    const.name = "FishC"
except TypeError as Err:
    print(Err)
