```python
arr = [(i, j) for i in ['a', 'b', 'c'] for j in [1, 2, 3]]
```

```python
demo_json = Path(__file__).read_text()  # 读取本地存储的文件内容 from pathlib import Path  pwd = Path('.').resolve()  # 获取当前目录路径或者Path.cwd()  # wl_dir = Path(__file__).resolve().parents[2]
```

```python
# 使用 iter() 函数创建迭代器，使用 lambda 函数作为可调用对象. iter() 函数接受两个参数，分别是可调用对象和哨兵值。它会不断调用可调用对象，直到返回哨兵值为止。 哨兵值（sentinel value）是一个特殊的值，用于表示迭代的终止条件。当迭代器产生哨兵值时，for 循环会认为迭代结束，从而退出循环。
my_iterator = iter(lambda: input("Enter a number or 'stop' to end: "), 'stop')
for i in my_iterator: print(i)
```

```python
print(str(datetime.now())[:-7])  # from datetime import datetime 获取当前时间(可读格式),并将其转换为字符串形式.  # 当前时刻的时间戳 单位:秒  import time   print(int(time.time())) 
```


```python
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([l[i:i + 3] for i in range(0, len(l), 3)])  # chunk_size = 3  # 将列表按照指定步长拆分
```

```python
# 生成长度为k的随机列表(从指定序列中随机抽取k个不重复的元素并以列表形式返回这些元素)  import random
l = random.sample(range(10), 10)
```

