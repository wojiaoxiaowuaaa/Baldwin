import multiprocessing
from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep
from gongju.time_count import calculate_execution_time

# def download_task(filename):
#     print('启动下载进程，进程号[%d]' % getpid())
#     print('开始下载%s...' % filename)
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))
#
#
# def main():
#     start = time()
#     p1 = Process(target=download_task, args=('群鸦的盛宴.pdf',))
#     p1.start()
#     p2 = Process(target=download_task, args=('权力的游戏.mp4',))
#     p2.start()
#     p1.join()
#     p2.join()
#     end = time()
#     print('总共耗费了%.2f秒.' % (end - start))
#
#
# if __name__ == '__main__':
#     main()


"""
Python 的多进程模块 multiprocessing 允许在多个 CPU 核上并行执行代码。每个进程都拥有自己的 Python 解释器和独立的内存空间，
因此它们能够在不同的 CPU 核上同时运行。这使得 Python 的多进程模型能够充分利用多核系统，实现真正的并行性。
与多线程模块 threading 不同，Python 的全局解释器锁（Global Interpreter Lock，GIL）对于多进程是没有影响的。在多线程模型中，
GIL 的存在限制了同一时刻只能有一个线程执行 Python 字节码，因此多线程并不能真正实现并行。
而在多进程模型中，每个进程都有自己的解释器和独立的 GIL，因此可以在多个 CPU 核上同时执行。
因此，通过 multiprocessing 模块创建的多进程是可以真正实现并行执行的，每个进程在不同的 CPU 核上运行，互不干扰。
这对于需要充分利用多核处理器的任务来说是非常有用的，特别是在计算密集型的工作负载下。
"""


def square_and_sum(numbers, result_queue):
    """result_queue 是一个进程共享的队列，它是由 multiprocessing.Manager().Queue() 创建的。multiprocessing.Manager() 提供了一种方式来创建在多个进程之间共享的对象，包括队列、字典、列表等。Manager().Queue() 返回一个可以在多个进程之间共享的队列对象。
    在多进程的环境中，每个进程都有自己独立的内存空间，无法直接共享变量。为了在多个进程之间共享数据，可以使用 multiprocessing 模块提供的 Manager 对象来创建共享的数据结构，其中包括队列。队列用于在多个进程之间传递数据，实现进程间的通信。
    在这个具体的例子中，result_queue 是一个用于存储每个进程计算得到的部分和的队列。每个进程在完成计算后，将其部分和放入队列中，最后通过对队列中的值进行求和，得到整体的和。这样，通过队列，多个进程可以协同工作，共同完成任务，并在最后将结果合并。"""
    square_sum = sum(x ** 2 for x in numbers)
    result_queue.put(square_sum)


if __name__ == "__main__":
    # 定义列表
    numbers = list(range(1, 100000001))
    # 将数字划分为若干块，每个进程处理一块
    chunk_size = len(numbers) // 12
    # 将列表通过切片 拆分为若干个小列表 每个嵌套的子列表中包含若干个元素 len(chunks) == 13
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]

    # 使用 multiprocessing.Manager().Queue() 创建进程共享的队列  manager = multiprocessing.Manager()
    result_queue = multiprocessing.Manager().Queue()

    # 使用 multiprocessing.Pool 创建进程池
    with multiprocessing.Pool(processes=12) as pool:
        # 在每个进程中执行 square_and_sum 函数
        pool.starmap(square_and_sum, [(chunk, result_queue) for chunk in chunks])

        # 汇总结果
        total_sum = sum(result_queue.get() for _ in range(12))

    print("Total sum of squares:", total_sum)
