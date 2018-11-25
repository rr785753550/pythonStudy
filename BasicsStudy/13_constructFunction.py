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


"""定义函数中调用初始化函数中参数"""
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