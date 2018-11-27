# coding: utf-8

"""打印print"""

"""print打印一个字符串或数字"""
print("number: 20")     # 结果：number: 20
print(20)                # 结果：20

"""print打印多个表达式，用逗号分隔"""
print("number:", 20)    # 结果：number: 20
a, b, c = 1, 2, 3
print(a, b, c)              # 结果：1 2 3
print(a, ',', b, ',', c)    # 结果：1 , 2 , 3
a = 'Hello'
b = 'World'
print(a + ',', b + '!')        # 结果：Hello, World!

"""print中添加自定义分隔符"""
print('I', 'want', 'go', 'home')    # 结果：I want go home
print('I', 'want', 'go', 'home', sep='_')   # 结果：I_want_go_home
print('Hello,', end='')
print('world')                  # 结果：Hello,world
