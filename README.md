```python
# 字符串处理Demo 去除空格指定符号等
string0 = "  , Hello  ,  World!     , "

# 默认去除开头和结尾的空格
new_string1 = string0.strip()

# 去除所有的空格
string2 = new_string1.replace(" ", "")

# 去除开头和结尾的逗号
new_string3 = string2.strip(",")

print(new_string1)
print(string2)
print(new_string3)
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
import os
import psutil

# range(start, stop, step)
# range() 返回的是一个可迭代对象，但不是一个迭代器(没有__next__方法),这个有点和列表list一样.但range是惰性计算.

# 对比列表与range对象的内存占用  
def show_memory_info(s='this process'):
    """计算当前进程占用的内存大小"""
    pid = os.getpid()
    p = psutil.Process(pid)
    info = p.memory_full_info()
    memory = info.uss / 1024 / 1024
    print('{} pid {} memory used: {} M'.format(s, pid, memory))


def test_iterable():
    show_memory_info('init iterable')
    # 生成包含 1 亿个元素的列。这个列表会被加载到内存中，并占用一定的内存空间。但在Python中，当一个对象不再被引用时，垃圾回收机制会自动将其释放，因此在脚本执行完毕后，这个大型列表占用的内存空间会被自动释放掉。
    [x * x for x in range(100000000)]
    show_memory_info('after iterable initiated')
    print('********')


def test_range():
    show_memory_info('init range')
    range(100000000)
    show_memory_info('after range initiated')
    print('********')


test_iterable()
test_range()
```

