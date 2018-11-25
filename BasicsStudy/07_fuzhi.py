# coding: utf-8
"""赋值"""

# 序列解包的方式赋值
"""同时给多个变量赋值"""
x, y, z = 1, 2, 3
print(x, y, z)  # 结果：1 2 3
"""通过赋值的方式，交互两个变量的值"""
x, y = y, x
print(x, y)     # 结果：2 1

"""将元组的值依次传给多个变量"""
tupleValues = 1, 2, 3
print(tupleValues)  # 结果：(1, 2, 3)
x, y, z = tupleValues
print(x, y, z)      # 结果：1 2 3

"""从字典中使用popitem随机删除一个键-值对并将其传给多个变量"""
dictValues = {'key1': 'value1', 'key2': 'value2'}
key, value = dictValues.popitem()
print(key, value, dictValues)   # 结果：key2 value2 {'key1': 'value1'}

"""变量名前含有*"""
x, y, *z = 1, 2, 3, 4
print("x:%s, y:%s, z:%s" % (x, y, z))   # 结果：x:1, y:2, z:[3, 4]
x, y, *z = [5, 6, 7, 8]
print("x:%s, y:%s, z:%s" % (x, y, z))   # 结果：x:5, y:6, z:[7, 8]
s = 'abc'
x, *y, z = s
print("x:%s, y:%s, z:%s" % (x, y, z))   # 结果：x:a, y:['b'], z:c
s = "appium is used by python."
x, *y, z = s.split()
print("x:%s, y:%s, z:%s" % (x, y, z))   # 结果：x:appium, y:['is', 'used', 'by'], z:python.

# 链式赋值
x = y = 1
print(x, y)     # 结果： 1 1

# 增加赋值 += 、*=
x = 1
x += 1
print(x)    # 结果：2
x *= 2
print(x)     # 结果：4
x = 'abc'
x += 'de'
print(x)    # 结果：abcde
x *= 2
print(x)    # 结果：abcdeabcde
