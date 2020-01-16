# 6.4.3 　在字典中存储字典
# 可在字典中嵌套字典，但这样做时，代码可能很快复杂起来。
# 例如，如果有多个网站用户，每个都有独特的用户名，可在字典中将用户名作为键，
# 然后将每位用户的信息存储在一个字典中，并将该字典作为与用户名相关联的值。
# 在下面的程序中，对于每位用户，我们都存储了其三项信息：名、姓和居住地；
# 为访问这些信息，我们遍历所有的用户名，并访问与每个用户名相关联的信息字典
users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },

    'mcurie':{
        'first':'marice',
        'last':'curie',
        'location':'paris',
    }

}

for username,user_info in users.items():
    print("\nUsername:",username.title())
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name:", full_name.title())
    print('\tLocation:', location.title())