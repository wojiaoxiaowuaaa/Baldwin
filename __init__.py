"""
---介绍下sys.path.append(os.path.abspath('.'))

sys.path 是一个包含模块搜索路径的列表。当 Python 解释器寻找要导入的模块时，它会搜索这些路径。
sys.path.append(path) 是将指定的路径 path 添加到 sys.path 列表中。
因此，sys.path.append(os.path.abspath('.')) 的作用是将当前工作目录的绝对路径添加到 sys.path 列表中。
这通常用于确保 Python 解释器能够找到项目中的模块，特别是当项目的某个模块需要被其他模块导入时。

sys.path 是一个列表，它指定了 Python 在导入模块时会搜索的目录。
当你尝试导入一个模块时，Python 会按照 sys.path 中的目录顺序依次查找模块文件。
"""


import os
import sys
# 将当前目录添加到系统路径中。这样，当你在代码中使用import语句导入模块时，Python 将会在当前目录及其子目录中查找模块文件。
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# for i in sys.path: print(i)
