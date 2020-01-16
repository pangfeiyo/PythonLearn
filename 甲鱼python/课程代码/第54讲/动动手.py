import urllib.request
url  = "http://python.usyiyi.cn/translate/python_352/library/urllib.request.html"
response = urllib.request.urlopen(url)
code = response.getcode()
print(code)


# 配合EasyGui，给“下载一只猫”的代码增加互动
import easygui as g

def main():
    msg = "请填写喵的尺寸"
    title = "下载一只猫"
    fieldName = ["宽：","高："]
    fieldValues = []
    size = width, height = 200 , 300
    # easygui.multenterbox 显示具有多个数据输入字段的屏幕
    # 如果值比名称更少，则值的列表将填充空字符串，直到值的数量与名称的数量相同。
    # 如果有比名称更多的值，值的列表将被截断，以便有与名称一样多的值。
    # 返回字段值的列表，如果用户取消操作，则返回None。
    fieldValues = g.multenterbox(msg, title, fieldName, size)

    while 1:
        if fieldValues == None:
            break
        errmsg = ""

        try:
            # strip() 方法用于移除字符串头尾指定的字符（默认为空格）
            width = int(fieldValues[0].strip())
        except:
            errmsg = "宽度必须为整数！"

        try:
            height = int(fieldValues[1].strip())
        except:
            errmsg = "高度必须为整数！"

        if errmsg == "":
            break

        fieldValues = g.multenterbox(errmsg, title, fieldName, fieldValues)

    url = "http://placekitten.com/g/%d/%d" % (width, height)

    response = urllib.request.urlopen(url)
    cat_img = response.read()

    # easygui.diropenbox 用于获取目录名的对话框
    filepath = g.diropenbox("请选择存放喵的文件夹")

    if filepath:
        filename = "%s/cat_%d_%d.jpg" % (filepath, width, height)
    else:
        filename = "cat_%d_%d.jpg" % (width, height)

    # w 只写入  wb 以二进制打开只写入
    with open(filename, "wb") as f:
        f.write(cat_img)

if __name__ == "__main__":
    main()
