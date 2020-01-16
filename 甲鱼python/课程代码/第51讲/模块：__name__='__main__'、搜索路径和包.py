# if __name__ == '__main__'


import M1.TemperatureConversion as tc
print("\n32摄氏度 = %.2f华氏度" % tc.c2f(32))
print("99华氏度 = %.2f摄氏度" % tc.f2c(99))


# 这里会把模块TemperatureConversion中的测试代码也打出来
# 这里就可以使用__name__
# 如果在主程序中使用，就会打印'__main__'
# 所以要用在模块中
# 看这一讲的课后有解释
print(tc.__name__)



# 搜索路径
# 写好的模块应该放在哪里
# 以前是模块与主程序放在同一文件夹
# 现在通过文件夹的方式更好的组织代码
import sys  # sys　和系统相关
# python会从以下路径中寻找模块，找到便导入，找不到导入失败
# 最佳模块存放位置 site-packages   最后一个
print(sys.path)
# 将某一个文件夹加入搜索路径
sys.path.append("D:\\")
print(sys.path)



# package 包   针对大型项目中的模块
# 该模块分门别类存放在文件夹中，然后将文件夹位置告诉python
'''
1.创建一个文件夹，用于存放相关的模块，文件夹的名字即包的名字
2.在文件夹中创建一个__init__.py的模块文件，内容可以为空
3.将相关的模块放入文件夹中
4.导入包的模块  
    包名.模块名
'''
import M1.TemperatureConversion as tc
print("\n32摄氏度 = %.2f华氏度" % tc.c2f(32))
print("99华氏度 = %.2f摄氏度" % tc.f2c(99))