# 8-3 T 恤 ：编写一个名为 make_shirt() 的函数，它接受一个尺码以及要印到 T 恤上的字样。
# 这个函数应打印一个句子，概要地说明 T 恤的尺码和字样。
# 使用位置实参调用这个函数来制作一件 T 恤；再使用关键字实参来调用这个函数。
def make_shirt(size, foot):
    print("这是一件",size,"尺码并印有",foot,"字样的衣服")
make_shirt('39','Haha')
make_shirt(foot='Nave',size='9')

# 8-4  大号 T 恤 ：修改函数 make_shirt() ，使其在默认情况下制作一件印有字样 “I love Python” 的大号 T 恤。
# 调用这个函数来制作如下 T 恤：
# 一件印有默认字样的大号 T恤、一件印有默认字样的中号 T 恤和一件印有其他字样的 T 恤（尺码无关紧要）。
print("\n8-4")
def make_shirt(size='big', foot='I love Python'):
    print("这是一件",size,"尺码并印有",foot,"字样的衣服")
make_shirt()
make_shirt(size='中')
make_shirt(foot='液体')

# 8-5  城市 ：编写一个名为 describe_city() 的函数，它接受一座城市的名字以及该城市所属的国家。
# 这个函数应打印一个简单的句子，如 Reykjavik is in Iceland 。给用于存储国家的形参指定默认值。
# 为三座不同的城市调用这个函数，且其中至少有一座城市不属于默认国家。
print("\n8-5")
def describe_city(name='Reykjavik',country='Iceland'):
    print(name,"属于",country)
describe_city()
describe_city(name='北京',country='中国')
describe_city(country='ICC')
