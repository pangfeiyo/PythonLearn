name = "赵飞"
print("姓名是：" + name) # str + str

age = 18
# print("年龄是：" + age)   会报错，str + int
print("年龄是：" + str(age))
print("年龄是：%s" % age) # %s --> str 简写，底层：str(age)

isMarry = False
print("结婚否？回答：%s" % isMarry)



print("年龄：%d" % age)




salary = 12000.3
print("我的薪水是：%.1f" % salary)  # 小数点后1位，四舍五入