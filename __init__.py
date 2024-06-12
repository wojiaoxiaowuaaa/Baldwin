import os
import sys

"""
echo $PATH命令在Mac终端（或任何Linux系统）中用于显示当前用户的环境变量PATH的内容。PATH环境变量包含了一系列的目录，这些目录被操作系统用来搜索可执行文件。

---介绍下sys.path.append(os.path.abspath('.'))
sys.path 是一个列表，它指定了 Python 在导入模块时会搜索的目录。当你尝试导入一个模块时，Python 会按照 sys.path 中的目录顺序依次查找模块文件。
for i in sys.path: print(i)  # 打印本地所有的搜索路径
sys.path.append(path) 是将指定的路径 path 添加到 sys.path 列表中。因此，sys.path.append(os.path.abspath('.')) 的作用是将当前工作目录的绝对路径添加到 sys.path 列表中。
这通常用于确保 Python 解释器能够找到项目中的模块，特别是当项目的某个模块需要被其他模块导入时。

可变类型 Vs 不可变类型
可变类型（mutable）:     列表，字典
不可变类型（unmutable):  数字，字符串，元组
这里的可变不可变，是指内存中的那块内容（value）是否可以被改变.如果是不可变类型，在对对象本身操作的时候，必须在内存中新申请一块区域(因为老区域不可变)如果是可变类型，对对象操作的时候，不需要再在其他地方申请内存，只需要在此对象后面连续申请(+/-)即可，也就是它的address会保持不变，但区域会变长或者变短。

Python的json模块提供了把内存中的对象序列化的方法.dump的功能就是把Python对象encode为json对象,一个编码过程。注意json模块提供了json.dumps和json.dump方法,区别是dump可以直接写到文件中,而dumps到一个字符串,这里的s可以理解为string。

基于指定的解释器创建虚拟环境(这里是基于pypy创建虚拟环境)
virtualenv  -p  /Users/wl/Documents/pypy3.10-v7.3.15-macos_x86_64/bin/pypy  venv_name
激活虚拟环境
source /venv_name/bin/activate
退出虚拟环境
deactivate

curl -X POST "http://127.0.0.1:8000/items/" -H "Content-Type: application/json" -d '{"name": "Sample Item", "description": "This is a sample item", "price": 10.5, "tax": 1.5}'
"""

# BASE_PATH(可作为项目拼接路径的参数) BASE_PATH = os.path.dirname(os.path.abspath(__file__))
# 添加项目目录到系统查询路径中 sys.path.insert(0, BASE_PATH)
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

