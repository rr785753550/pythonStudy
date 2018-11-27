# coding: utf-8\
"""字典的基本操作"""

"""直接创建字典"""
dict1 = {'name': 'A', 'age': '25', 'sex': 'male'}
"""使用函数dict从其他映射或键-值对序列创建字典"""
item1 = [('name', 'A'), ('age', '25'), ('sex', 'male')]
dict2 = dict(item1)
print(dict2)        # 结果： {'name': 'A', 'age': '25', 'sex': 'male'}
dict3 = dict(name='A', age='25', sex='male')
print(dict3)        # 结果： {'name': 'A', 'age': '25', 'sex': 'male'}

"""字典基本操作：len、添加新项、删除某项、判断键是否存在于字典"""
length = len(dict1)
print(length)           # 结果： 3
print(dict1['name'])    # 结果： A
dict1['score'] = '90'
print(dict1)            # 结果： {'name': 'A', 'age': '25', 'sex': 'male', 'score': '90'}
del dict1['sex']
print(dict1)            # 结果：{'name': 'A', 'age': '25', 'score': '90'}
print('name' in dict1)  # 结果： True

"""将字符串格式设置功能用于字典"""
s1 = "A's age is {age}".format_map(dict1)
print(s1)           # 结果：A's age is 25

"""清除字典方法：clear"""
d1 = {'a': 1, 'b': 2}
d2 = d1
d3 = d1
d2 = {}
print(d2)       # 结果：{}
print(d1)       # 结果：{'a': 1, 'b': 2}
d3.clear()
print(d3)        # 结果：{}
print(d1)        # 结果：{}

"""复制字典：浅复制copy，深复制deepcopy"""
d4 = {'a': 1, 'b': [2, 3, 4]}
d5 = d4.copy()
print(d5)           # 结果：{'a': 1, 'b': [2, 3, 4]}
d5['a'] = 3
d5['b'].remove(2)
print(d4)           # 结果：{'a': 1, 'b': [3, 4]}
print(d5)           # 结果：{'a': 3, 'b': [3, 4]}
from copy import deepcopy
d6 = deepcopy(d4)
print(d6)           # 结果：{'a': 1, 'b': [3, 4]}
d6['a'] = 3
d6['b'].remove(4)
print(d4)           # 结果：{'a': 1, 'b': [3, 4]}
print(d6)           # 结果：{'a': 3, 'b': [3]}

"""fromkeys创建一个新字典，类似于dict"""
dict4 = {}.fromkeys(['name', 'age'])
print(dict4)                            # 结果： {'name': None, 'age': None}
print(dict.fromkeys(['name', 'age']))   # 结果： {'name': None, 'age': None}

"""get：获得字典中某个键的value值"""
dict1 = {'name': 'A', 'age': '25'}
print(dict1.get('name'))        # 结果： A
"""items、keys和values：获得字典的所有项、所有键值、所有value值"""
print(dict1.items())    # 结果：dict_items([('name', 'A'), ('age', '25')])
print(dict1.keys())     # 结果：dict_keys(['name', 'age'])
print(dict1.values())   # 结果：dict_values(['A', '25'])

"""pop:删除字典的指定健-值对，并返回"""
m = dict1.pop('age')
print(m)        # 结果：25
print(dict1)    # 结果：{'name': 'A'}
"""popitem：随机删除字典的值"""
dict1['age'] = '25'
dict1['sex'] = 'male'
print(dict1.popitem())    # 结果： ('sex', 'male')
print(dict1)       # 结果： {'name': 'A', 'age': '25'}

"""setdefault方法"""
print(dict1.setdefault('name', 'None'))      # 结果：A
print(dict1.setdefault('name1', 'my'))       # 结果：my
print(dict1)          # 结果：  {'name': 'A', 'age': '25', 'name1': 'my'}

"""update方法"""
dict2 = {'name1': 'B'}
dict1.update(dict2)
print(dict1)    # 结果： {'name': 'A', 'age': '25', 'name1': 'B'}
dict3 = {'name2': 'C'}
dict1.update(dict3)
print(dict1)    # 结果：{'name': 'A', 'age': '25', 'name1': 'B', 'name2': 'C'}

