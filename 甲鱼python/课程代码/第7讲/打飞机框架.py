'''
加载背景音乐
播放背景音乐（单曲循环）
我方飞机诞生
interval = 0     # 小飞机间隔


while True:
    if 用户是否点击了关闭按钮：
        退出程序

    interval += 1           #这边要加50次，才能满足下面 == 50
    if interval == 50:      #相当于间隔50像素才刷新一个小飞机
        interval = 0
        小飞机诞生

    小飞机移动一个位置
    屏幕刷新

    if 用户鼠标产生移动：
        我方飞机中心位置 = 用户鼠标位置
        屏幕刷新

    if 我方飞机与小飞机产生肢体冲突：
        我方挂，播放撞机音乐
        修改我方飞机图案
        打印“game over”
        停止背景音乐，最好淡出


'''