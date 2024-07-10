# 显示当前 python 程序占用的内存大小
import os
import psutil


def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))


def test_iterator():
    show_memory_info('initing iterator')
    list_1 = [i for i in range(100000000)]
    show_memory_info('after iterator initiated')
    print(sum(list_1))
    show_memory_info('after sum called')


def test_generator():
    show_memory_info('initing generator')
    list_2 = (i for i in range(100000000))
    show_memory_info('after generator initiated')
    print(sum(list_2))
    show_memory_info('after sum called')


test_generator()
print('---------'*10)
test_iterator()


"""
测试结果输出如下所示:
initing generator memory used: 30.3515625 MB
after generator initiated memory used: 30.3515625 MB
4999999950000000
after sum called memory used: 30.3515625 MB
------------------------------------------------------------------------------------------
initing iterator memory used: 30.3515625 MB
after iterator initiated memory used: 2862.09375 MB
4999999950000000
after sum called memory used: 3579.6015625 MB
"""