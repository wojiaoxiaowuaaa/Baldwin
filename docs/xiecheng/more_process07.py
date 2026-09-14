import os
from multiprocessing import Process
import time


def pro_func(name, age, **kwargs):
    for i in range(5):
        print("子进程正在运行中，name=%s,age=%d,pid=%d" % (name, age, os.getpid()))
        print(kwargs)
        time.sleep(0.2)


if __name__ == "__main__":
    p = Process(
        target=pro_func, args=("小明", 18), kwargs={"city": "北京", "temperature": 20}
    )
    p.start()
    time.sleep(0.5)
    p.terminate()  # 0.5秒钟之后,立刻结束子进程.由于子进程会被主进程终止，因此子进程可能不会完成所有5次循环。
    p.join()

"""

import multiprocessing
import os


def worker():
    # 在多核处理器上，操作系统会尽力将不同的进程分配到不同的 CPU 核心上，以实现并行执行。然而，这个分配过程由操作系统的调度程序自动管理，程序本身并不能直接控制进程被分配到哪个核心。
    # 使用 Python 的 multiprocessing 模块创建的多个进程，操作系统会尝试将这些进程分配到不同的 CPU 核心上，以优化性能和资源利用。这意味着，如果你的机器有多个 CPU 核心，操作系统有可能会将这些进程分配到不同的核心上执行。
    # 你可以通过以下示例代码来创建多个进程，并查看每个进程的 PID 和分配的 CPU 核心：
    pid = os.getpid()
    try:
        cpu = os.sched_getaffinity(pid)
    except AttributeError:
        cpu = 'Not available on this OS'
    print(f"Process ID: {pid}, CPU: {cpu}")


if __name__ == "__main__":
    processes = []
    for _ in range(5):
        p = multiprocessing.Process(target=worker)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

"""
