# 根本课堂上的例子，定制一个列表，同时要求记录列表中每个元素被访问的次数。
# 功能更加全面些，比如支持append()、pop()、extend()原生列表所拥有的方法
# 要求1：实现获取、设置和删除一个元素的行为（删除一个元素的时候对应的计数器也会被删除）
# 要求2：增加counter(index)方法，返回index参数所指定的元素记录的访问次数
# 要求3：实现append()、remove()、inset()、clear()和revers()方法（重写这些方法的时候注意考虑计数器的对应改变）
# 为了实现这么多功能，不能再用字典来存放元素的计数了。因为对于列表来说，如果你删除其中一个元素
# 那么其他元素的下标都会发生相应的变化（利用下标作为键的字典肯定就不能应对自如）
# 因此，改用一个列表来存放对应的元素的计数
# 下边的CountList类继承并严重依赖其父类（List）的行为，并按要求重写了一些方法
class CountList(list):
    def __init__(self, *args):
        super().__init__(args)
        self.count = []
        for i in args:
            self.count.append(0)

    def __len__(self):
        return len(self.count)

    def __getitem__(self, key):
        self.count[key] += 1
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        self.count[key] += 1
        super().__setitem__(key, value)

    def __delitem__(self, key):
        del self.count[key]
        super().__delitem__(key)

    def counter(self, key):
        return self.count[key]

    def append(self, value):
        self.count.append[0]
        super().append(value)

    def pop(self, key = -1):
        del self.count[key]
        return super().pop(key)

    def remove(self, value):
        key = super().index(value)
        del self.count[key]
        super().remove(value)

    def insert(self, key, value):
        self.count.insert(key, 0)
        super().insert(key, value)

    def clear(self):
        self.count.clear()
        super().clear()

    def reverse(self):
        self.count.reverse()
        super().reverse()

