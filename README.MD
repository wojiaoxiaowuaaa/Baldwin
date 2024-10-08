```python
# 嵌套循环
arr = [(i, j) for i in ['a', 'b', 'c'] for j in [1, 2, 3]]
```
```python
from pathlib import Path
# 读取本地存储的文件内容
demo_json = Path('./config/demo.json').read_text()
```
```python
string0 = "  , !Hello & , ) World! _ + = 1  , "
# 去除开头和结尾的空格. strip()方法移除字符串开头和结尾的指定字符（默认是空白字符、空格、换行符、制表符等).
new_string1 = string0.strip()
# 去除所有的空格
string2 = new_string1.replace(" ", "")
# 去除开头和结尾的逗号
new_string3 = string2.strip(",")
```

```python
import json
import os


def func(json_file):
    """读取本地存储的json文件,转化为dic类型
    json.load 用于从文件中加载 JSON 数据，接收文件对象作为参数,例如f。
    json.loads 用于从json字符串中加载 JSON 数据，接收字符串作为参数例如f.read()或变量名"""
    with open(json_file, 'r') as f:
        data = json.load(f)  # <class 'dict'>
        return data


json_file = f'{os.path.dirname(__file__)}/config/demo.json'
data = func(json_file)
print(data)
```

```python
# 使用 iter() 函数创建迭代器，使用 lambda 函数作为可调用对象
# iter() 函数接受两个参数，分别是可调用对象和哨兵值。它会不断调用可调用对象，直到返回哨兵值为止。
# 哨兵值（sentinel value）是一个特殊的值，用于表示迭代的终止条件。当迭代器产生哨兵值时，for 循环会认为迭代结束，从而退出循环。
my_iterator = iter(lambda: input("Enter a number or 'stop' to end: "), 'stop')

# 使用 for 循环遍历迭代器
for i in my_iterator:
    print(i)
```

```python
from datetime import datetime
# 获取当前时间(可读格式),并将其转换为字符串形式.
time = str(datetime.now())[:-7]
print(time)

import time
 # 当前时刻的时间戳 单位:秒
print(int(time.time()))
```
```python
# 将字典的键转换为列表，然后获取指定的键.同理可以转换为列表后取value: list(my_dict.values())
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = list(my_dict)[1]  # list(my_dict.keys())将字典的键转换为列表，然后获取第二个键. 同理可以转换为列表后取value的值list(my_dict.values())

# items() 方法是 Python 字典对象的一个内置方法，它返回一个包含字典键值对的视图对象。这个视图对象是一个可迭代的对象，其中每个元素都是一个包含键值对的元组 (key, value)。
# 将字典按value值按升序排列
d = {'a': 24, 'g': 52, 'i': 12, 'k': 33}
# print(sorted(d.items(), key=lambda x: x[1]))
# 字典推导式对换一个字典的键跟值
# print({v: k for k, v in d.items()})
```

```python
# 将列表按照指定步长拆分
l =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chunk_size = 3
print([l[i:i+chunk_size] for i in range(0, len(l), chunk_size)])
```