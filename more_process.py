from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    p1 = Process(target=download_task, args=('群鸦的盛宴.pdf',))
    p1.start()
    p2 = Process(target=download_task, args=('权力的游戏.mp4',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()


"""
Python 的多进程模块 multiprocessing 允许在多个 CPU 核上并行执行代码。每个进程都拥有自己的 Python 解释器和独立的内存空间，
因此它们能够在不同的 CPU 核上同时运行。这使得 Python 的多进程模型能够充分利用多核系统，实现真正的并行性。
与多线程模块 threading 不同，Python 的全局解释器锁（Global Interpreter Lock，GIL）对于多进程是没有影响的。在多线程模型中，
GIL 的存在限制了同一时刻只能有一个线程执行 Python 字节码，因此多线程并不能真正实现并行。
而在多进程模型中，每个进程都有自己的解释器和独立的 GIL，因此可以在多个 CPU 核上同时执行。
因此，通过 multiprocessing 模块创建的多进程是可以真正实现并行执行的，每个进程在不同的 CPU 核上运行，互不干扰。
这对于需要充分利用多核处理器的任务来说是非常有用的，特别是在计算密集型的工作负载下。
"""
