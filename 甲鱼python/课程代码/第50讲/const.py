# 该模块让python支持常量操作
class Const:
    def __setattr__(self, name, value):
        # __dict__是用来存储对象属性的一个字典，其键为属性名，值为属性的值。
        if name in self.__dict__:
            # 我们可以使用raise语句自己触发异常
            raise TypeError("常量无法改变！")

        if not name.isupper():
            raise TypeError("常量名必须由大写字母组成！")

        self.__dict__[name] = value

import sys
sys.modules[__name__] = Const()
