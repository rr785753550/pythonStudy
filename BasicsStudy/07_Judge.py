# coding: utf-8
"""判断语句"""

# bool布尔值
"""bool值输出"""
print(True)         # 结果： True
print(True + 42)    # 结果： 43
print(False + 42)   # 结果： 42
"""将不同类型的值转化为bool值"""
print(type(True))   # 结果：<class 'bool'>
print(bool("my name"))   # 结果：True
print(bool(42))     # 结果：True
print(bool(''))     # 结果：False
print(bool([]))     # 结果：False

"""if语句用法"""
import random
i = random.randint(-100, 100)  # i为从1到100的随机整数
if i < 0:
    print("数字%s为负数" % i)
elif i == 0:
    print("数字%s为零" % i)
else:
    print("数字%s为正数" % i)


"""if语句嵌套"""
import random
i = random.randint(-100, 100)  # i为从1到100的随机整数
if i < 0:
    if i % 2 == 0:
        print("数字%s为负偶数" % i)
    else:
        print("数字%s为负奇数" % i)
elif i == 0:
    print("数字%s为零" % i)
else:
    if i % 2 == 0:
        print("数字%s为正偶数" % i)
    else:
        print("数字%s为正奇数" % i)


"""比较运算符： is和=="""
x = "python"
y = "python"
print(x == y)       # 结果：True
print(x is y)       # 结果：True
x = y = [1, 2, 3]
z = [1, 2, 3]
print(x == z)       # 结果：True
print(x is z)       # 结果：False，x和z值虽然相等但它们指向的对象不同
print(x == y)       # 结果：True
print(x is y)       # 结果：True

"""比较运算符： in"""
if 'on' in 'python':
    print("元素on在python中")
else:
    print("元素on不在python中")  # 结果：元素on在python中

"""字符串和序列的比较"""
print("abc" < "aa")             # 结果：False
print([1, 2, 3] < [1, 3, 2])    # 结果：True

"""逻辑运算符and、or、not"""
a = 0
b = 10
if a and b:
    print("a和b全为真")
else:
    print("a和b至少有一个为假")     # 输出
if a or b:
    print("a和b至少有一个为真")     # 输出
else:
    print("a和b全为假")
if not a:
    print("a为假")            # 输出
else:
    print("a为真")

"""while循环"""
x = 1
s = 0
while x <= 5:
    s += x
    x += 1
print(s)    # 结果：15

"""for循环：列表"""
list1 = ['hello', 'world']
for s in list1:
    print(s)     # 结果hello   world

"""for循环：字典"""
dict1 = {'x': 1, 'y': 2}
for key in dict1:
    print(key, "=", dict1[key])
# 结果： x = 1 y = 2

"""迭代字典"""
for key, value in dict1.items():
    print(key, '=', value)      # 结果： x = 1 y = 2
"""并行迭代"""
names = ['cheng', 'zhang']
ages = [12, 20]
for i in range(len(names)):
    print(names[i], 'is', ages[i])  # 结果：cheng is 12    zhang is 20
for name, age in zip(names, ages):
    print(name, 'is', age)          # 结果：cheng is 12    zhang is 20
print(zip(names, ages))             # 结果：<zip object at 0x00000000025A0748>
print(list(zip(names, ages)))       # 结果：[('cheng', 12), ('zhang', 20)]
print(list(zip(range(2), range(10))))   # 结果：[(0, 0), (1, 1)]
"""迭代时获取索引"""
list1 = ['hello world!', 'python 3', 'good time']
for s in list1:
    if 'py' in s:
        index = list1.index(s)
        list1[index] = 'python3.6'
print(list1)            # 结果：['hello world!', 'python3.6', 'good time']
for index, s in enumerate(list1):
    if 'world!' in s:
        list1[index] = 'study'
print(list1)            # 结果：['study', 'python3.6', 'good time']
"""反射迭代和排序后再迭代"""
list1 = [2, 6, 1, 7]
print(sorted(list1))    # 结果：[1, 2, 6, 7]
s = "good"
print(sorted(s))        # 结果：['d', 'g', 'o', 'o']
print(list(reversed(('hello'))))    # 结果：['o', 'l', 'l', 'e', 'h']
print(''.join(reversed('hello')))   # 结果：olleh
print(sorted("AbC", key=str.lower))   # 结果：['A', 'b', 'C']
print(sorted("AbC"))                # 结果：['A', 'C', 'b']

"""跳出循环break、continue"""
i = -1
while True:
    i += 1
    if i == 5:
        break               # 结束循环
    elif i == 0:
        print("数字为：", i)
        continue                # 跳过本次循环，下方的代码不再执行，开始新的循环
    print("数字0< %d < 5" % i)
"""# 结果：
数字为： 0
数字0< 1 < 5
数字0< 2 < 5
数字0< 3 < 5x
数字0< 4 < 5
"""

"""列表推导"""
x = [i * i for i in range(5)]
print(x)        # 结果：[0, 1, 4, 9, 16]

y = [i * i for i in range(5) if i % 2 == 0]
print(y)        # 结果：[0, 4, 16]
y = []
for i in range(5):
    if i % 2 == 0:
      y.append(i*i)
print(y)        # 结果：[0, 4, 16]

y = [(i, j) for i in range(2) for j in range(2)]
print(y)        # 结果：[(0, 0), (0, 1), (1, 0), (1, 1)]
y = []
for i in range(2):
    for j in range(2):
        y.append((i, j))
print(y)        # 结果：[(0, 0), (0, 1), (1, 0), (1, 1)]

"""字典推导"""
y = {i: "{} squared is {}".format(i, i**2) for i in range(2)}
print(y)        # 结果：{0: '0 squared is 0', 1: '1 squared is 1'}

"""pass语句"""
i = 0
if i == 0:
    pass        # 无任何输出
else:
    print(i, "不等于0")

"""exec"""
exec("print('hello, world!')")  # 结果： hello, world!
