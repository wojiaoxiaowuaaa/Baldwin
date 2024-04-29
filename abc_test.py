import os
import psutil


def show_memory_info(s):
    """计算当前进程占用的内存大小"""
    pid = os.getpid()
    p = psutil.Process(pid)
    info = p.memory_full_info()
    memory = info.uss / 1024 / 1024
    print('{} memory used: {} M'.format(s, memory))


def test_iterable():
    show_memory_info('init iterable')
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