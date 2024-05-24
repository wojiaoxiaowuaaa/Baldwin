```python
string0 = "  , Hello  ,  World!     , "

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


json_file = f'{os.path.dirname(__file__)}/doc/demo.json'
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
from locust import HttpUser, TaskSet, wait_time, between, task, FastHttpUser


# locust -f locust_demo.py --headless -u 100 -r 10 -t 60 -H  https://www.baidu.com --html  report.html

# -u或 --users：指定要模拟的并发用户数量。
# -r或 --spawn-rate：指定每秒钟产生新用户的速率。
# -t或 --run-time：指定测试运行的持续时间。
# -H或 --host：指定要测试的目标主机（即被测应用的基本 URL）。
# -c或 --config：指定配置文件的路径，以定义更复杂的测试场景和用户行为。
# --html report.html: 生成html报告

# class UserBehavior(TaskSet):
#     @task
#     def search(self):...


class BaiDu(HttpUser):
    wait_time = between(1, 3)
    
    host = "https://www.baidu.com"

    @task
    def search(self):
        self.client.get("/?tn=54093922_30_hao_pg")
```

```python
from datetime import datetime
# 获取当前时间(可读格式),并将其转换为字符串形式.
time = str(datetime.now())[:-7]
print(time)

import time
 # 当前时刻的时间戳 单位:秒
print(int(time.time())) 

# 在不传递参数的情况下，ctime() 函数会将当前时间（即当前系统时钟所显示的时间）转换为可读的字符串形式。
from time import ctime
print(ctime())

```
```python
# 将字典的键转换为列表，然后获取指定的键.同理可以转换为列表后取value: list(my_dict.values())
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = list(my_dict)[1]  # list(my_dict.keys())将字典的键转换为列表，然后获取第二个键. 同理可以转换为列表后取value的值list(my_dict.values())

# items() 方法是 Python 字典对象的一个内置方法，它返回一个包含字典键值对的视图对象。这个视图对象是一个可迭代的对象，其中每个元素都是一个包含键值对的元组 (key, value)。
# 将字典按value值按升序排列
d = {'a': 24, 'g': 52, 'i': 12, 'k': 33}
print(sorted(d.items(), key=lambda x: x[1]))
```
