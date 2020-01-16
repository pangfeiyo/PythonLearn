product_list = [
    ('Mac',9000),
    ('kindle',800),
    ('tesla',900000),
    ('python book',105),
    ('bike',2000)
]

saving = input("please input your money:")
shopping_car = []   # 购物车

if saving.isdigit():    # 如果 saving 是数字的话
    saving = int(saving)    # 也可以直接 saving = eval(input))，就不用在这里if了

    '''
    for i in product_list:
        #加个序号
        print(product_list.index(i),i)'''

    while True:
        # 用于将一个可遍历的数据对象组合为一个索引序列，同时列出数据和数据下标
        # start=1 下标起始位置
        # 打印商品内容
        for i,j in enumerate(product_list, start=1):
            print(i," >>>> ",j)

        # 引导用户选择商品
        choice = input("选择购买商品编号[退出：q]：")

        # 验证输入是否合法
        if choice.isdigit():    # 如果是数字
            choice = int(choice)

            if choice > 0 and choice <= len(product_list):  # 是否越界
                # 将用户选择商品通过choice取出来
                p_item = product_list[choice - 1]

                # 如果钱够，用本金saving减去该商品价格，并将该商品加入购物车
                if p_item[1] < saving:
                    saving -= p_item[1] # 存的钱减商品钱
                    shopping_car.append(p_item) # 加入购物车

                else:
                    print("余额不足，还剩%s" % saving)
                print(p_item)
            else:
                print('编码不存在，越界')
        elif choice == 'q':
            print('-------- 您已购买以下商品 --------')
            # 循环遍历购物车里面的商品，购物车存放的是已买商品
            # 并显示数量
            shopset = set(shopping_car)   # set() 去除重复
            for i in shopset:
                print(i, "数量：", shopping_car.count(i))
            print("您还剩%s元钱" % saving)
            break
        else:
            print("invalid input")  # 非法输入



