person = "大圣哥"
address = "北京市"
phone = "1588"
num = 5

# 使用“+”必须左右两边都是str
print("订单接收人：" +  person + "，" + 
"收件地址是：" + address + "，" + 
"手机号是：" + phone)

# 一行太长，用“\”换行
print("订单接收人：%s，收件地址是：%s，\
手机号是：%s，数量是：%d" \
        % (person, address, phone, num))