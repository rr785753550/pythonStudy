# coding: utf-8
"""构造函数（初始化__init__）"""


"""构造函数中参数"""
# 构造函数中不传入参数
class FooBar1:
    def __init__(self):
        self.somevar = 42

print(FooBar1().somevar)     # 结果：42

# 构造函数中传入参数并初始化赋值
class FooBar2:
    def __init__(self, somevar = 42):
        self.somevar = somevar

print(FooBar2().somevar)                # 结果：42
print(FooBar2(somevar=45).somevar)      # 结果：45

# 构造函数中传入参数且未初始化
class FooBar3:
    def __init__(self, somevar):
        self.somevar = somevar

print(FooBar3(somevar=42).somevar)      # 结果：42



"""类中定义函数调用构造函数参数"""
class Bird1:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("Aaaah...")
            self.hungry = False
        else:
            print("No, thanks!")
bird = Bird1()
print(bird)
bird.eat()      # 结果：Aaaah...
bird.eat()      # 结果：No, thanks!

class Bird2:
    def __init__(self, hungry):
        self.hungry = hungry

    def eat(self):
        if self.hungry:
            print("Aaaah...")
        else:
            print("No, thanks!")
Bird2(hungry=True).eat()        # 结果：Aaaah...
Bird2(hungry=False).eat()       # 结果：No, thanks!



"""重写构造函数"""
class Bird3:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("Aaaah...")
            self.hungry = False
        else:
            print("No, thanks!")
# 调用未关联的超类构造函数
class SongBird1(Bird3):
    def __init__(self):
        Bird3.__init__(self)
        self.sound = 'Singer'

    def sing(self):
        print(self.sound)
songBird1 = SongBird1()
songBird1.sing()         # 结果：Singer
songBird1.eat()          # 结果：Aaaah...
# 使用函数super
class SongBird2(Bird3):
    def __init__(self):
        super().__init__()
        self.sound = 'Singer'

    def sing(self):
        print(self.sound)
songBird2 = SongBird2()
songBird2.sing()         # 结果：Singer
songBird2.eat()          # 结果：Aaaah...
