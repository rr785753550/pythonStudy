# coding: utf-8
"""元组介绍"""
i = (42)
print(type(i))      # 结果：<class 'int'>
j = (42,)
print(type(j))      # 结果：<class 'tuple'>
m = (1, 2, 3)
print(type(m))      # 结果：<class 'tuple'>

"""列表转化为元组"""
x1 = [1, 2, 3]
y1 = tuple(x1)
print(y1)           # 结果：(1, 2, 3)

"""字符串转化为元组"""
x2 = 'abc'
y2 = tuple(x2)
print(y2)           # 结果：('a', 'b', 'c')
