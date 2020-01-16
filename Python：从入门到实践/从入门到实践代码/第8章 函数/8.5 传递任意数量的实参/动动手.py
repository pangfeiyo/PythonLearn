# 8-12  三明治 ：编写一个函数，它接受顾客要在三明治中添加的一系列食材。
# 这个函数只有一个形参（它收集函数调用中提供的所有食材），并打印一条消息，对顾客点的三明治进行概述。
# 调用这个函数三次，每次都提供不同数量的实参。
def make_sandwich(*items):
    '''制作具有特定物品的三明治'''
    print("\nI'll make you a great sandwich:")
    for item in items:
        print(" ...adding " + item + " to your sandwich.")
    print("Your sandwich is ready!")
make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')


# 8-13  用户简介 ：复制前面的程序 user_profile.py ，在其中调用 build_profile() 来创建有关你的简介；
# 调用这个函数时，指定你的名和姓，以及三个描述你的键 - 值对。
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('飞','胖',
                             SteamID = 'pangfeiyo',
                             OriginID = 'thisyes',
                             GOGID = '等我喝完这杯酒')
print(user_profile)


# 8-14  汽车 ：编写一个函数，将一辆汽车的信息存储在一个字典中。
# 这个函数总是接受制造商和型号，还接受任意数量的关键字实参。
# 这样调用这个函数：提供必不可少的信息，以及两个名称 — 值对，如颜色和选装配件。
def make_car(manufacturer, model, **options):
    '''创建一个代表汽车的字典'''
    car_dict = {
        'manufacturer':manufacturer.title(),
        'model':model.title()
    }
    for option, value in options.items():
        car_dict[option] = value
    return car_dict

my_outback = make_car('subaru','outback',color = 'bule', tow_package = True)
print(my_outback)
my_accord = make_car('honda', 'accord', year=1991, color='white',
        headlights='popup')
print(my_accord)