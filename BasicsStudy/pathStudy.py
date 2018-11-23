import os
import sys

# 获取当前py的绝对路径,包括文件名
py_path = os.path.abspath(__file__)
print(py_path)      # 结果：F:\PythonWorkSpace\others\PythonStudy\BasicsStudy\pathStudy.py

# 获取当前py所在的文件夹的绝对路径，不包括文件名
py_file_path = os.path.dirname(os.path.abspath(__file__))
print(py_file_path)     # 结果：F:\PythonWorkSpace\others\PythonStudy\BasicsStudy

# 获取py所在文件夹的上一级文件夹的绝对路径
py_pre_file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(py_pre_file_path)     # 结果：F:\PythonWorkSpace\others\PythonStudy

# 将路径动态的添加到环境变量中
sys.path.append(py_pre_file_path)