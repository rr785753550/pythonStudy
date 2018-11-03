# coding: utf-8

"""列表：增加清除功能"""
lists = [1, 2, 3]
lists.append(4)
print(lists)
# 结果： [1, 2, 3, 4]
lists.clear()
print(lists)
# 结果： []

"""复制列表"""
a = [1, 2, 3]
b = a
b[0] = 5
print("a=", a)
print("b=", b)      # 结果：a= [5, 2, 3] b= [5, 2, 3]
c = a.copy()
print("c=", c)      # 结果：c= [5, 2, 3]
c[0] = 1
print("a=", a)
print("c=", c)      # 结果：a= [5, 2, 3] c= [1, 2, 3]

"""count功能"""
