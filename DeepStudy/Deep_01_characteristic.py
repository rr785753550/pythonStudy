# coding: utf-8
"""特性"""


"""函数property"""
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self, size):
        self.width, self.height = size

    def get_size(self):
        return self.width, self.height

    size = property(get_size, set_size)

r = Rectangle()
r.width = 10
r.height = 5
print(r.size)       # 结果：(10, 5)
r.size = 150, 100
print(r.width)      # 结果：150



"""静态方法和类方法"""
class MyClass:
    @staticmethod                       # 第二种@装饰器的方式
    def smeth():
        print("This is a static method.")
    # smeth = staticmethod(smeth)       # 第一种调用的方式

    @classmethod
    def cmeth(cls):
        print("This is a class method of ", cls)
    # cmeth = classmethod(cmeth)

MyClass.smeth()         # This is a static method.
MyClass.cmeth()         # This is a class method of  <class '__main__.MyClass'>



"""__getattr__和__setattr__方法"""
class Rectangle1:
    def __init__(self):
        self.width = 0
        self.height = 0

    def __setattr__(self, key, value):
        if key == 'size':
            self.width, self.height = value
        else:
            self.__dict__[key] = value

    def __getattr__(self, item):
        if item == 'size':
            return self.width, self.height
        else:
            raise AttributeError()
