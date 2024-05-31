import os

"""
第18行使用return的效果：
1. 立即终止函数： 当 return 被执行时，函数 func 会立即终止，并且不会再继续执行循环或任何其他代码。 2.停止迭代： 由于 return 会立即退出函数，yield 的生成器也会终止.
第18行使用break的效果：
1. 退出当前循环： 当 break 被执行时，它只会退出当前的 while 循环，而不是整个函数。 2. 继续执行后续代码： 在 break 之后，函数中的其他代码（如果有）仍然会继续执行。 3.完整读取文件： 由于 break 只退出循环，生成器会继续读取文件的所有数据块，直到文件结束"""


def func(pwd):
    block_size = 1024

    with open(pwd, 'r') as f:
        while True:
            data = f.read(block_size)
            if data:
                yield data
            return


for i in func(os.path.abspath(__file__)): print(i)
