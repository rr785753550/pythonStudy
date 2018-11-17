# coding: utf-8
"""字符串的相关操作"""

"""字符串最简单的格式"""
format = "Hello, %s! Today is so %s."
values = ("Jenny", "Hot")
s1 = format % values
print(s1)   # 结果： Hello, Jenny! Today is so Hot.

"""字符串方法：center"""
s = "Hello, World!"
print(s.center(20))         # 结果：   Hello, World!
print(s.center(20, "*"))    # 结果：***Hello, World!****

"""字符串方法：find"""
s = "The package name is com.android.settings. please tell me the package and activity!"
print(s.find("package"))    # 结果： 4

"""字符串方法：join"""
list1 = ['1', '2', '3', '4', '5']
s = '+'
print(s.join(list1))    # 结果： 1+2+3+4+5
d = 'data', 'local', 'tmp'
print('\\'.join(d))     # 结果： data\local\tmp

"""字符串方法： split"""
s = "A B C D E"
print(s.split(" "))         # 结果：['A', 'B', 'C', 'D', 'E']
print(s.split())            # 结果：['A', 'B', 'C', 'D', 'E']
print(s.split("C"))         # 结果：['A B ', ' D E']

"""字符串方法：lower， title， upper"""
s = "Hello, WORLD!"
print(s.lower())        # 结果： hello, world!
print(s.title())        # 结果： Hello, World!
print(s.upper())        # 结果： HELLO, WORLD!

"""字符串方法：replace"""
s = "Hello, Jimmy!"
print(s.replace('Jimmy', 'Tom'))    # 结果： Hello, Tom!

"""字符串方法：strip"""
s = "    hello   world!   "
print(s.strip())        # 结果：hello   world!
print(s.strip(" !d"))   # 结果：hello   worl

"""字符串方法： translate（将字符串中c和s分别替换成k和z）"""
s = "This is an cup."
table = str.maketrans('cs', 'kz')
print(s.translate(table))               # 结果：Thiz iz an kup.
table1 = str.maketrans('cs', 'kz', ' ')
print(s.translate(table1))              # 结果：Thizizankup.

"""字符串方法：判断字符串是否满足特定的条件"""
s = "Hello"
print(s.islower(), s.isalnum(), s.isalpha(), s.isdecimal())
# 结果： False True True False
