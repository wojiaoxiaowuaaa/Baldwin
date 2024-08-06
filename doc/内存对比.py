import os
import psutil


# range(start, stop, step)
# range() 返回的是一个可迭代对象，但不是一个迭代器(没有__next__方法),这个有点和列表list一样.但range是惰性计算.


# 对比列表与range对象的内存占用
def show_memory_info(s="this process"):
    """计算当前进程占用的内存大小"""
    pid = os.getpid()
    p = psutil.Process(pid)
    info = p.memory_full_info()
    memory = info.uss / 1024 / 1024
    print("{} pid {} memory used: {} M".format(s, pid, memory))


def wl_iterable():
    show_memory_info("init iterable")
    # 生成包含 1 亿个元素的列。这个列表会被加载到内存中，并占用一定的内存空间。但在Python中，当一个对象不再被引用时，垃圾回收机制会自动将其释放，因此在脚本执行完毕后，这个大型列表占用的内存空间会被自动释放掉。
    [x * x for x in range(100000000)]
    show_memory_info("after iterable ")
    print("********")


def wl_range():
    show_memory_info("init range")
    range(100000000)
    show_memory_info("after range ")


wl_iterable()
wl_range()
