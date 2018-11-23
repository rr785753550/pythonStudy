"""继承"""

"""最简单的子类直接继承父类"""
class Person(object):
    def talk(self):
        print("person is talking")

class Chinese(Person):
    def walk(self):
        print("person is walking")

# issubclass判断两个类的继承关系
print(issubclass(Chinese, Person))     # 结果：True
print(issubclass(Person, Chinese))     # 结果：False
# __bases__获取类的基类
print(Person.__bases__)        # 结果：(<class 'object'>,)
print(Chinese.__bases__)        # 结果：(<class '__main__.Person'>,)
# isinstance判断对象是否是特定类的实例
print(isinstance(Chinese(), Chinese))           # 结果：True
print(isinstance(Chinese(), Person))           # 结果：True
print(isinstance(Person(), Chinese))           # 结果：False

# 父类调用父类的方法
Chinese().talk()        # 结果： person is talking
Chinese().walk()        # 结果： person is walking
Person().talk()         # 结果： person is talking

"""构造函数的继承"""
class Person1(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = 'weight'

    def talk(self):
        print("person is talking")

class Chinese1(Person1):
    def __init__(self, name, age, language):  # 先继承，再重构
        Person1.__init__(self, name, age)   # 继承父类的构造方法
        # super(Chinese1, self).__init__(name, age)     # 另一种继承父类的构造方法
        self.language = language            # 定义类本身的属性

    def walk(self):
        print("person is walking")

c = Chinese1(name='zhang', age=20, language='Chinese')
# 实现方法：对象c调用子类的__init__()，子类的__init__()继承父类的__init__()，再调用父类的__init__()
c.talk()                            # 结果：person is talking
c.walk()                            # 结果：person is walking

"""子类对父类方法的重写"""
class Person2(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = 'weight'

    def talk(self):
        print("person is talking")

class Chinese2(Person2):
    def __init__(self, name, age, language):  # 先继承，再重构
        Person2.__init__(self, name, age)   # 继承父类的构造方法
        # super(Chinese1, self).__init__(name, age)     # 另一种继承父类的构造方法
        self.language = language            # 定义类本身的属性

    def talk(self):
        print(self.name, " is speaking chinese")

    def walk(self):
        print("person is walking")

Chinese2(name='zhang', age=20, language='Chinese').talk()   # 结果：zhang  is speaking chinese
Person2(name='zhang', age=20).talk()            # 结果：person is talking
