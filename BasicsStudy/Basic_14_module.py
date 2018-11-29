# coding: utf-8

"""模块"""

"""当前目录下所有模块的路径"""
import sys
# 搜索当前目录、所有已安装的内置模块和第三方模块，并将路径以列表形式存放sys模块的path变量中
print(sys.path)

import pprint
pprint.pprint(sys.path)
# print是将文件一行打印出来，不会自动换行
# pprint.pprint 输出格式的对象字符串到指定的stream，以换行符结束


# """导入包中某个.py模块"""
# # 如：Python Package名为：BasicsStudy，导入此包下的函数Basic_02_tuple.py
# from BasicsStudy import Basic_02_tuple


"""探索模块"""

# 使用dir列出copy模块中除去以下划线开头的可供外部调用的所有属性
import copy
dir_out = [n for n in dir(copy) if not n.startswith('_')]
print(dir_out)      # 结果：['Error', 'copy', 'deepcopy', 'dispatch_table', 'error']

# 变量__all__
all_out = copy.__all__
print(all_out)      # 结果：['Error', 'copy', 'deepcopy']


# sys模块
print(sys.argv)
# 结果：['F:/PythonWorkSpace/PythonStudy/BasicsStudy/Basic_14_module.py']
try:
    sys.exit(0)
except:
    print('Program is dead.')
# 结果：Program is dead.
print(sys.modules)
print(sys.platform)
# 结果：win32


# """os模块"""
# import os
# print(os.environ)               # 显示所有的环境变量
# print(os.environ['ANDROID_HOME'])   # 访问ANDROID_HOME的环境变量
# # 结果：C:\Users\admin\AppData\Local\Android\Sdk\platform-tools
# os.system("adb devices")        # 显示当前adb连接的设备信息
#
# # 三种启动web浏览器的方法
# os.system(r'D:\\"Program Files"\"Mozilla Firefox"\firefox.exe')     # Windows下启动浏览器
# # os.system('/usr/bin/firefox')     # Linux下启动浏览器
# os.startfile(r"D:\Program Files\Mozilla Firefox\firefox.exe")       # 启动浏览器
# import webbrowser
# webbrowser.open('http://www.baidu.com')     # 默认使用IE浏览器打开网址
#
#
# """fileinput模块"""
# import fileinput
# # 查看文件所有行
# for line in fileinput.input('test.txt'):
#     print(line)
# # 修改文件并备份原文件
# for line in fileinput.input('test.txt', backup='.bak', inplace=1):
#     line = line.replace('test2', 'test-B')
#     print(line)
# # 输出当前行号和行内容
# for line in fileinput.input('test.txt'):
#     lineno = fileinput.lineno()
#     print(lineno, line)
# # 判断是否为第一行
# for line in fileinput.input('test.txt'):
#     if fileinput.isfirstline():
#         print(line)
#         break


"""集合"""
# 创建集合
setTogether = set(range(10))
print(setTogether)              # 结果：{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
string1 = 'test'
print(set(string1))             # 结果：{'s', 'e', 't'}
list1 = ['a', 'b', 'c']
print(set(list1))               # 结果：{'b', 'a', 'c'}
# 空{}并不是集合类型
print(type(setTogether))        # 结果：<class 'set'>
print(type({}))                 # 结果：<class 'dict'>
# 集合中无重复元素
print({0, 1, 2, 3, 0, 3, 5})    # 结果：{0, 1, 2, 3, 5}
# 集合是无序的
print({'fee', 'file', 'fae'})   # 结果：{'fee', 'fae', 'file'}

# 集合运算
a = {1, 2, 3}
b = {2, 3, 4}
# 并集
print(a.union(b))           # 结果：{1, 2, 3, 4}
print(a | b)                # 结果：{1, 2, 3, 4}
# 交集
print(a.intersection(b))    # 结果：{2, 3}
print(a & b)                # 结果：{2, 3}
# 差集
print(a - b)                # 结果：{1}
print(a.difference(b))      # 结果：{1}
print(b - a)                # 结果：{4}
print(b.difference(a))      # 结果：{4}
# 对称差集
print(a.symmetric_difference(b))    # 结果：{1, 4}
print(a ^ b)                        # 结果：{1, 4}
# 判断a是否为b的子集
print(a.issubset(b))    # 结果：False
# 判断a是否为b的父集
print(a.issuperset(b))  # 结果：False

# 集合：增删改查
# 增加一个元素
a.add(8)
print(a)    # 结果：{8, 1, 2, 3}
# 增加一个列表
a.update(['x', 'y'])
print(a)    # 结果：{1, 2, 3, 8, 'x', 'y'}
# 随机删除一个元素
a.pop()
print(a)      # 结果：{2, 3, 8, 'y', 'x'}
# 删除一个指定元素
a.remove('x')
print(a)        # 结果：{2, 3, 'y', 8}
# 删除一个指定元素，并返回该元素
a.discard('y')
print(a)        # 结果：{2, 3, 8}
# 从集合a中删除另一集合b中所有元素
a.difference_update(b)
print(a)        # 结果：{8}
# 将a和b的对称差更新到集合a中
a.symmetric_difference_update(b)
print(a)        # 结果：{2, 3, 4, 8}

# 清空集合中所有元素
a.clear()
print(a)       # 结果： set()



"""堆"""
from heapq import *
from random import shuffle
data = list(range(10))
print(data)         # 结果：[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle(data)
print(data)         # 结果：[9, 8, 4, 3, 6, 0, 5, 7, 1, 2]
heap = []
for i in data:
    heappush(heap, i)
print(heap)             # 结果：[0, 1, 3, 4, 2, 8, 5, 9, 7, 6]
print(heappop(heap))    # 结果：0
print(heappop(heap))    # 结果：1
print(heap)             # 结果：[2, 4, 3, 5, 6, 9, 8, 7]

heap1 = [5, 6, 1, 4, 9, 2]
heapify(heap1)
print(heap1)             # 结果：[1, 4, 2, 6, 9, 5]
heapreplace(heap1, 0.5)
print(heap1)            # 结果：[0.5, 4, 2, 6, 9, 5]



"""双端队列"""
from collections import deque
x = deque(range(5))
print(x)              # 结果：deque([0, 1, 2, 3, 4])
x.append(5)
print(x)              # 结果：deque([0, 1, 2, 3, 4, 5])
print(x.pop())        # 结果： 5
print(x.popleft())    # 结果： 0
print(x)              # 结果：deque([1, 2, 3, 4])
x.rotate(3)
print(x)              # 结果：deque([2, 3, 4, 1])
x.rotate(-1)
print(x)              # 结果：deque([3, 4, 1, 2])
