import openpyxl 

# 文件路径，python中路径要用\\
d = r'D:\CompanyProject\002_Others\CloudGame\0_Design\1_页面设计\3_手机3.0版\手机3.0版_设计文档.xlsx'

# 要添加的工作表名
SheetList = ["a004_首页","a047_搜索页面","a036_消息","a007_专题内容","a006_游戏分类",
             "a008_游戏详情","a018_商店","a006_游戏_专题","a005_游戏","a012_游戏圈",
             "a012_资讯","a012_版块","a018_商店","a020_商城钻石充值","a053_淘宝店",
             "a021_输入兑换码","a014_个人中心","a015_编辑资料","a038_连续登录奖励","a037_每日任务",
             "a022_我的收藏","a044_游玩历史","a045_我的会员","a046_我的钻石","a024_虚拟手柄",
             "a027_查看登陆设备","a026_投屏","a023_官方交流群","a034_设置","a059_退出确认"]

# 列表长度
sllen = int(len(SheetList))
print("sllen:",sllen)

# 打开并写入
wb = openpyxl.load_workbook(d)

# 循环新建工作表
for i in range(sllen): 
    wb.create_sheet(title = SheetList[i],index = -1)
    i+=1

# 保存
wb.save(d)

print("操作完成")
