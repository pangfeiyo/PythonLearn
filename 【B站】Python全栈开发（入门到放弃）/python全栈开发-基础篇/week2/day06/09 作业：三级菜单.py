'''
要求：
1 打印省、市、县三级菜单
2 可返回上一级
3 可随时退出程序 
'''

menu = {
	"北京":{
		'朝阳':{
			'国贸':{
				'CICC':{},
				'HP':{},
				'渣打银行':{},
				'CCTV':{},
			},
			'望京':{
				'陌陌':{},
				'奔驰':{},
				'360':{},
			},
			'三里屯':{
				'优衣库':{},
				'apple':{},
			}
		},
		'昌平':{
			'沙河':{
				'老男孩':{},
				'阿泰包子':{},
			},
			'天通苑':{
				'链家':{},
				'我爱我家':{},
			},
			'回龙观':{},
		},
		'海淀':{
			'五道口':{
				'谷歌':{},
				'网易':{},
				'Sohu':{},
				'Sogo':{},
				'快手':{},
			},
			'中关村':{
				'youku':{},
				'Iqiyi':{},
				'汽车之家':{},
				'新东方':{},
				'QQ':{},
			},
		},
	},
	"上海":{
		'浦东':{
			'陆家嘴':{
				'CICC':{},
				'高盛银行':{},
				'摩根':{},
			},
			'外滩':{},
		},
		'闵行':{},
		'静安':{},
	},
	"山东":{
		'济南':{},
		'德州':{
			'乐陵':{
				'丁务镇':{},
				'城区':{},
			},
			'平原':{},
		},
		'青岛':{},
	},}


''' 简易流程
while True:
	# 打印字典第1层的三个key：北京上海山东
	for key in menu:
		print(key)
	
	
	choice = input(">>:").strip()	# .strip() 去空格和换行
	if choice in menu:	# 如果用户输入的内容在第1层的key上
		while True:	# 让程序停在第二层
			for key2 in menu[choice]:	# 循环打印出北京的值
				print(key2)
	
			choice2 = input("2>>:").strip()
			# 如果用户输入的内容在北京的3个值昌平朝阳海淀里
			if choice2 in menu[choice]:	
				while True:
					for key3 in menu[choice][choice2]:	# 打印出昌平的值
						print(key3)
	
					choice3 = input("3>>:").strip()
					# 如果用户输入的内容在昌平的值里
					if choice3 in menu[choice][choice2]:
						# 打印沙河里的值
						for key4 in menu[choice][choice2][choice3]:
							print(key4)
'''


'''只能返回一次父层
current_layer = menu
#parent_layer = menu # 记录父层，只能记住单个父层。使用列表记录后把这条语句注释

parent_list = []	# 列表，存放多个父层。用字典也可以

while True:
	for key in current_layer:
		print(key)
	
	choice = input(">>>:").strip()
	if len(choice) == 0:continue	# 如果输入的长度为0，跳出本次循环

	if choice in current_layer:	# 判断用户输入的内容是否在字典第1层
		# parent_layer = current_layer  # 把当前层赋值给父层
		
		
		# 如果存在，把第2层字典的key赋给current_layer
		# 本次while循环结束，回到开头，打印第2层字典key值
		current_layer = current_layer[choice]	# 当前层进入子层
	
	elif choice == 'b':	# 如果用户输入'b'
		current_layer = parent_layer # 把子层改成父层
			
	else:
		print("无此项")

'''

current_layer = menu
parent_list = []	# 保存所有父层，最后一个元素永远都是父级。用字典也可以

while True:
	for key in current_layer:
		print(key)
	
	choice = input(">>>:").strip()
	if len(choice) == 0:continue	# 如果输入的长度为0，跳出本次循环

	if choice in current_layer:	# 判断用户输入的内容是否在字典第1层
		parent_list.append(current_layer)	# 在进入下一层前，把当前层加入到父层列表中
		# 下一次loop，当用户选择b的时候，就可以直接取列表的最后一个值出来
		current_layer = current_layer[choice]	# 当前层进入子层
	
	elif choice == 'b':	# 如果用户输入'b'
		if parent_list: # 如果为真，即不为空
			current_layer = parent_list.pop()	# 取最后一个且删除
			
	else:
		print("无此项")
		