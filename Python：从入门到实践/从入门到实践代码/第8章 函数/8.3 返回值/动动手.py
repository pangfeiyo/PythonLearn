# 8-6  城市名 ：编写一个名为 city_country() 的函数，它接受城市的名称及其所属的国家。
# 这个函数应返回一个格式类似于下面这样的字符串："Santiago, Chile"
print("8-6：")
def city_country(city, country):
    c_c = city + ", " + country
    return c_c
# city_name =input("请输入城市名：")
# country_name = input("请输入国家：")
# ci_co = city_country(city_name,country_name)
ci_co = city_country('北京','中国')
print(ci_co)
ci_co = city_country('San Francisco','USA')
print(ci_co)
ci_co = city_country('Paris','France')
print(ci_co)

# 8-7  专辑 ：编写一个名为 make_album() 的函数，它创建一个描述音乐专辑的字典。
# 这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。
# 使用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。
print("\n8-7：")
def make_album(name, album, number = 0):
    music_album = {
        'make':name.title(),
        'album':album.title(),
        }
    # 给函数 make_album() 添加一个可选形参，以便能够存储专辑包含的歌曲数。如果调用这个函数时指定了歌曲数，就将这个值添加到表示专辑的字典中。
    # 调用这个函数，并至少在一次调用中指定专辑包含的歌曲数。
    if number:
        music_album['numbers'] = number
    return music_album
music = make_album('metallica', 'ride the lightning')
print(music)
music = make_album('beethoven', 'ninth symphony',number = 3)
print(music)
music = make_album('willie nelson', 'red-headed stranger')
print(music)


# 8-8  用户的专辑 ：在为完成练习 8-7 编写的程序中，编写一个 while 循环，让用户输入一个专辑的歌手和名称。
# 获取这些信息后，使用它们来调用函数 make_album() ，并将创建的字典打印出来。在这个 while 循环中，务必要提供退出途径。
print("\n8-8：")
def make_album(name, album, number = 0):
    music_album = {
        'make':name.title(),
        'album':album.title(),
        }
    if number:
        music_album['numbers'] = number
    return music_album
while True:
    music_name = input("请输入歌手名：")
    music_album = input("请输入专辑名：")
    music_number = input("请输入数量：")
    if music_name == "quit":
        break
    elif music_album == "quit":
        break
    elif music_number == "quit":
        break

    if music_number.isdigit():
        musicalbum = make_album(music_name, music_album, music_number)
    else:
        musicalbum = make_album(music_name, music_album)
    print(musicalbum)
