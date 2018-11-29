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
print(a.union(b))           # 结果：{1, 2, 3, 4}
print(a | b)                # 结果：{1, 2, 3, 4}
print(a.intersection(b))    # 结果：{2, 3}
print(a & b)                # 结果：{2, 3}
print(a - b)                # 结果：{1}
print(a.difference(b))      # 结果：{1}
print(b - a)                # 结果：{4}
print(b.difference(a))      # 结果：{4}

