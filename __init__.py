import os
import sys

"""
---介绍下sys.path.append(os.path.abspath('.'))

sys.path 是一个包含模块搜索路径的列表。当 Python 解释器寻找要导入的模块时，它会搜索这些路径。
sys.path.append(path) 是将指定的路径 path 添加到 sys.path 列表中。
因此，sys.path.append(os.path.abspath('.')) 的作用是将当前工作目录的绝对路径添加到 sys.path 列表中。
这通常用于确保 Python 解释器能够找到项目中的模块，特别是当项目的某个模块需要被其他模块导入时。

sys.path 是一个列表，它指定了 Python 在导入模块时会搜索的目录。
当你尝试导入一个模块时，Python 会按照 sys.path 中的目录顺序依次查找模块文件。

将当前目录添加到系统路径中。这样，当你在代码中使用import语句导入模块时，Python 将会在当前目录及其子目录中查找模块文件。
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
for i in sys.path: print(i)

可变类型 Vs 不可变类型
可变类型（mutable）:     列表，字典
不可变类型（unmutable):  数字，字符串，元组
这里的可变不可变，是指内存中的那块内容（value）是否可以被改变.。如果是不可变类型，在对对象本身操作的时候，必须在内存中新申请一块区域(因为老区域不可变)如果是可变类型，对对象操作的时候，不需要再在其他地方申请内存，只需要在此对象后面连续申请(+/-)即可，也就是它的address会保持不变，但区域会变长或者变短。

curl -X POST "http://127.0.0.1:8000/items/" -H "Content-Type: application/json" -d '{"name": "Sample Item", "description": "This is a sample item", "price": 10.5, "tax": 1.5}'

"""


# 项目根路径
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_PATH)