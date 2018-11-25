"""面向对象"""

"""多态"""
print(1 + 2)
print('hello ' + 'world!')
def add(x, y):
    return x+y
print(add('heool', 'world!'))
print("hello".count('e'))
# 运算符+ 、 add函数、count方法等这些均属于多态

"""封装"""

"""类"""
# 不含继承的类
class Student:
    def name(self, name):
        return name

    def score(self, score):
        return score


name = Student().name('zhang')
score = Student().score("90")
print(name, ':', score)         # 结果：zhang : 90

# 含继承的类
class Student1(object):
    def name(self, name):
        return name

    def score(self, score):
        return score


name = Student1().name('zhang')
score = Student1().score("90")
print(name, ':', score)         # 结果：zhang : 90

# 类中存在初始化变量，初始变函数中存在变量
class Student11(object):
    def __init__(self, name):
        self.name = name

    def score(self, score):
        return [self.name, score]

result11 = Student11(name='zhange').score('90')
print(result11)         # 结果：['zhange', '90']

# 类中存在初始化变量，初始变函数中不存在变量
class Student12(object):
    def __init__(self):
        self.name = 'zhang'

    def score(self, score):
        return [self.name, score]

result11 = Student12().score('90')
print(result11)         # 结果：['zhange', '90']

# 没有在类中定义的函数
def student(name):
    return name
name = student('zhang')
print(name)                 # 结果：zhang


# 类中一个函数调用另一函数，以及外部调用类中函数的写法
class Student2:
    def name(self):
        print('zhang')

    def score(self):
        self.name()
        print("90")
Student2().name()           # 结果：zhang
Student2().score()          # 结果：zhang      90

# 类中函数私有化
class Student3:
    def __name(self):
        print("zhang")

    def score(self):
        self.__name()
        print("90")
# Student3().__name()        # 报错，外部无法访问__name，但在内部可以访问
Student3().score()                  # 结果：zhang      90

# 类中定义变量
class MyClass:
    number = 0

    def init(self):
        MyClass.number += 1

print(MyClass.number)       # 结果：0
MyClass().init()
print(MyClass.number)       # 结果：1
MyClass().init()
print(MyClass.number)       # 结果：2




