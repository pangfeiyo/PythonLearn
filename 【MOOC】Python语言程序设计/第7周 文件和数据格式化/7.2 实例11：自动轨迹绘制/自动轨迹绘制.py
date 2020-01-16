'''
自动轨迹绘制
  - 需求：根据脚本来绘制图形
  - 不是写代码而是写数据绘制轨迹
  - 数据脚本是自动化最重要的第一步

基本思路
  - 步骤1：定义数据文件格式（接口）
  - 步骤2：编写程序，根据文件接口解析参数绘制图形
  - 步骤3：编制数据文件


一行表示一次操作
    300, 0, 144, 1, 0, 0
    行进距离
    转向判断，0左，1右
    转向角度
    后三参数：RGB三个通道颜色，0-1之间浮点数
'''
import turtle as t

t.title('自动轨迹绘制')   # 窗口标题
t.setup(800, 600, 0, 0)
t.pencolor("red")
t.pensize(5)

# 打开数据文件，解析数据文件每一行信息，并做相关处理
datals = []
f = open('data.txt')
for line in f:  # 按行读取
    line = line.replace("\n", "")   # 去掉换行符
    # split(",")以逗号分隔
    # map(a,b) 将第一个参数的功能作用于第二个参数的每个元素
    # 将这一行数据转为列表
    datals.append(list(map(eval, line.split(","))))
f.close()

# 自动绘制
for i in range(len(datals)):
    # 颜色
    t.pencolor(datals[i][3], datals[i][4], datals[i][5])
    # 距离
    t.fd(datals[i][0])
    # 转向方向及角度
    if datals[i][1]:    # != 0   为1是True，默认
         t.right(datals[i][2])
    else:
         t.left(datals[i][2])
t.done()
            
'''
理解方法思维 
  - 自动化思维：数据和功能分离，数据驱动的自动运行
  - 接口化设计：格式化设计接口，清晰明了
  - 二维数据应用：应用维度组织数据，二维数据最常用

应用问题扩展
  - 扩展接口设计，增加更多控制接口
  - 扩展功能设计，增加弧形等功能
  - 扩展应用需求，发展自动轨迹绘制到动画绘制
'''