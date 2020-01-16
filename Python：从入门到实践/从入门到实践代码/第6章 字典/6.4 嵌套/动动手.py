# 6-7  人 ：在为完成练习 6-1 而编写的程序中，再创建两个表示人的字典，然后将这三个字典都存储在一个名为 people 的列表中。
# 遍历这个列表，将其中每个人的所有信息都打印出来。
friends1 = {
    'first_name':'张',
    'last_name':'同',
    'age':'111',
    'city':'liquid',
    }
friends2 = {
    'first_name':'王',
    'last_name':'明',
    'age':'222',
    'city':'nb',
    }
friends3 = {
    'first_name':'钱',
    'last_name':'经',
    'age':'333',
    'city':'lfy',
    }
people = [friends1,friends2,friends3]
number = 0
for friend in people:
    # for name,value in friend.items():
    number += 1
    print("\n第", number ,"个用户的信息：")
    print("姓名：", friend['first_name'] + friend['last_name'])
    print("年龄",friend['age'])
    print('城市',friend['city'])
    # print(friend)
print("……")
# 6-8  宠物 ：创建多个字典，对于每个字典，都使用一个宠物的名称来给它命名；在每个字典中，包含宠物的类型及其主人的名字。
# 将这些字典存储在一个名为 pets的列表中，再遍历该列表，并将宠物的所有信息都打印出来。
dog = {
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
}
car = {
'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
}
flsh = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes',
}
pets = [dog, car, flsh]
for pet in pets:
    print("\nHere's what i know about", pet['name'].title())
    for key,value in pet.items():
        print("\t",key , ":", str(value))
print('……')

# 6-9  喜欢的地方 ：创建一个名为 favorite_places 的字典。
# 在这个字典中，将三个人的名字用作键；对于其中的每个人，都存储他喜欢的 1~3 个地方。
# 为让这个练习更有趣些，可让一些朋友指出他们喜欢的几个地方。
# 遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。
favorite_place = {
    'wang': ['bear mountain', 'death valley', 'tierra del fuego'],
    'qian': ['hawaii', 'iceland'],
    'liu': ['mt. verstovia', 'the playground', 'south carolina']
    }
for name,places in favorite_place.items():
    print("\n", name.title(), "likes the following places:")
    for place in places:
        print("-", place.title())
print("……")
# 6-10  喜欢的数字 ：
# 修改为完成练习 6-2 而编写的程序，让每个人都可以有多个喜欢的数字，然后将每个人的名字及其喜欢的数字打印出来。
friends = {
    'mandy': [42, 17],
    'micah': [42, 39, 56],
    'gus': [7, 12],
    }
for name,numbers in friends.items():
    print("\n", name.title(), "likes the following numbers;")
    for number in numbers:
        print(" ",number)
print("……")

# 6-11  城市 ：创建一个名为 cities 的字典，其中将三个城市名用作键；
# 对于每座城市，都创建一个字典，并在其中包含该城市所属的国家、人口约数以及一个有关该城市的事实。
# 在表示每座城市的字典中，应包含 country 、 population 和 fact 等键。
# 将每座城市的名字以及有关它们的信息都打印出来。
cities = {
    'santiago': {
        'country': 'chile',
        'population': 6158080,
        'nearby mountains': 'andes',
        },
    'talkeetna': {
        'country': 'alaska',
        'population': 876,
        'nearby mountains': 'alaska range',
        },
    'kathmandu': {
        'country': 'nepal',
        'population': 1003285,
        'nearby mountains': 'himilaya',
        }
    }
for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    mountains = city_info['nearby mountains'].title()

    print('\n', city.title(), 'is in', country)
    print("  It has a population of about " + str(population) + ".")
    print("  The " + mountains + " mountains are nearby.")
print('……')
# 6-12  扩展 ：本章的示例足够复杂，可以以很多方式进行扩展了。
# 请对本章的一个示例进行扩展：添加键和值、调整程序要解决的问题或改进输出的格式。