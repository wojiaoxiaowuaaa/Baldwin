"""
进程:程序运行在操作系统上的一个实例,就称之为进程.进程需要相应的系统资源:内存、时间片、pid等.

Python 的多进程模块 multiprocessing 允许在多个 CPU 核上并行执行代码.每个进程都拥有自己的 Python 解释器和独立的内存空间,
因此它们能够在不同的 CPU 核上同时运行.这使得 Python 的多进程模型能够充分利用多核系统,实现真正的并行性.
与多线程模块 threading 不同,Python 的全局解释器锁(Global Interpreter Lock,GIL)对于多进程是没有影响的.在多线程模型中,
GIL 的存在限制了同一时刻只能有一个线程执行 Python 字节码,因此多线程并不能真正实现并行.
而在多进程模型中,每个进程都有自己的解释器和独立的 GIL,因此可以在多个 CPU 核上同时执行.
因此,通过 multiprocessing 模块创建的多进程是可以真正实现并行执行的,每个进程在不同的 CPU 核上运行,互不干扰.
这对于需要充分利用多核处理器的任务来说是非常有用的,特别是在计算密集型的工作负载下.
"""
import multiprocessing


def square_and_sum(arr, queue):
    """q 是一个进程共享的队列,它是由 multiprocessing.Manager().Queue() 创建的.multiprocessing.Manager() 提供了一种方式来创建在多个进程之间共享的对象,包括队列、字典、列表等.Manager().Queue() 返回一个可以在多个进程之间共享的队列对象.
    在多进程的环境中,每个进程都有自己独立的内存空间,无法直接共享变量.为了在多个进程之间共享数据,可以使用 multiprocessing 模块提供的 Manager 对象来创建共享的数据结构,其中包括队列.队列用于在多个进程之间传递数据,实现进程间的通信.
    在这个具体的例子中,q 是一个用于存储每个进程计算得到的部分和的队列.每个进程在完成计算后,将其部分和放入队列中,最后通过对队列中的值进行求和,得到整体的和.这样,通过队列,多个进程可以协同工作,共同完成任务,并在最后将结果合并.
    """
    square_sum = sum(x ** 2 for x in arr)
    queue.put(square_sum)


if __name__ == "__main__":
    # 导入multiprocessing模块,该模块提供了在多个CPU核心上并行执行代码的能力.使用multiprocessing.Manager().Queue()创建一个进程共享的队列q,允许不同进程之间传递数据.
    # 这段代码利用了Python的多进程特性,将计算任务分解为多个子任务,并行执行,从而提高了计算速度,尤其是在处理大量数据时.通过使用进程共享队列,不同进程间可以有效地通信,将各自计算的部分结果汇总.

    numbers = list(range(1, 10001))
    # 将列表划分为若干块,每个进程处理一块
    chunk_size = len(numbers) // 12
    # 将列表通过切片 拆分为若干个小列表 每个嵌套的子列表中包含若干个元素
    chunks = [numbers[i: i + chunk_size] for i in range(0, len(numbers), chunk_size)]
    # 使用 multiprocessing.Manager().Queue() 创建进程共享的队列  manager = multiprocessing.Manager()
    queue = multiprocessing.Manager().Queue()
    # 创建一个具有多个进程的进程池 可以方便地并行执行多个任务.
    with multiprocessing.Pool(processes=12) as pool:
        # 在每个进程中执行 square_and_sum 函数
        pool.starmap(square_and_sum, [(chunk, queue) for chunk in chunks])
        # 汇总结果  q.qsize() == 13
        # while not q.empty(): print(q.get())
        total_sum = sum(queue.get() for _ in range(12))

    print("Total sum of squares:", total_sum)


"""

import threading
import time
from queue import Queue


def square_and_sum(l, queue):
    # 多线程版本
    square_sum = sum(x ** 2 for x in l)
    queue.put(square_sum)


if __name__ == "__main__":
    start_time = time.time()
    numbers = list(range(1, 10001))
    chunk_size = len(numbers) // 12
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
    queue = Queue()  # 由于多线程共享内存空间,我们可以使用普通的队列而不是进程安全的队列.
    threads = []

    # 创建并启动线程
    for chunk in chunks:
        thread = threading.Thread(target=square_and_sum, args=(chunk, queue))
        thread.start()
        threads.append(thread)

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    total_sum = sum(queue.get() for _ in range(12))
    print("Total sum of squares:", total_sum)
    print("Execution time:", time.time() - start_time)

"""


"""

async def worker(arr, queue):
    tar = sum(i**2 for i in arr)
    await queue.put(tar)


async def main():
    arr = list(range(1, 10001))
    chunk_size = len(arr) // 12
    chunks = [arr[i:i+chunk_size] for i in range(0, len(arr), chunk_size)]

    queue = asyncio.Queue()

    works = [worker(l, queue) for l in chunks]
    await asyncio.gather(*works)

    res = sum([await queue.get() for i in range(12)])
    print(res)

if __name__ == '__main__':
    s = time()
    asyncio.run(main())
    print(time() - s)
    
"""