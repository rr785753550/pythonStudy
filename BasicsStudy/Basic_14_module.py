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


"""os模块"""
import os
print(os.environ)
os.system()