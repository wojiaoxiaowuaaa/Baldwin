import multiprocessing


"""
进程：程序运行在操作系统上的一个实例，就称之为进程。进程需要相应的系统资源：内存、时间片、pid等。

Python 的多进程模块 multiprocessing 允许在多个 CPU 核上并行执行代码。每个进程都拥有自己的 Python 解释器和独立的内存空间，
因此它们能够在不同的 CPU 核上同时运行。这使得 Python 的多进程模型能够充分利用多核系统，实现真正的并行性。
与多线程模块 threading 不同，Python 的全局解释器锁（Global Interpreter Lock，GIL）对于多进程是没有影响的。在多线程模型中，
GIL 的存在限制了同一时刻只能有一个线程执行 Python 字节码，因此多线程并不能真正实现并行。
而在多进程模型中，每个进程都有自己的解释器和独立的 GIL，因此可以在多个 CPU 核上同时执行。
因此，通过 multiprocessing 模块创建的多进程是可以真正实现并行执行的，每个进程在不同的 CPU 核上运行，互不干扰。
这对于需要充分利用多核处理器的任务来说是非常有用的，特别是在计算密集型的工作负载下。
"""


def square_and_sum(l, queue):
    """q 是一个进程共享的队列，它是由 multiprocessing.Manager().Queue() 创建的。multiprocessing.Manager() 提供了一种方式来创建在多个进程之间共享的对象，包括队列、字典、列表等。Manager().Queue() 返回一个可以在多个进程之间共享的队列对象。
    在多进程的环境中，每个进程都有自己独立的内存空间，无法直接共享变量。为了在多个进程之间共享数据，可以使用 multiprocessing 模块提供的 Manager 对象来创建共享的数据结构，其中包括队列。队列用于在多个进程之间传递数据，实现进程间的通信。
    在这个具体的例子中，q 是一个用于存储每个进程计算得到的部分和的队列。每个进程在完成计算后，将其部分和放入队列中，最后通过对队列中的值进行求和，得到整体的和。这样，通过队列，多个进程可以协同工作，共同完成任务，并在最后将结果合并。"""
    square_sum = sum(x ** 2 for x in l)
    queue.put(square_sum)


if __name__ == "__main__":
    """这段Python代码的主要目的是计算一个大整数列表（numbers）中所有元素平方和的总和，但通过使用多进程并行计算来提高效率。以下是详细的步骤：
    导入multiprocessing模块，该模块提供了在多个CPU核心上并行执行代码的能力。
    定义函数square_and_sum(numbers, q)，该函数接受一个数字列表numbers和一个进程共享的队列q作为参数。它计算列表中所有元素的平方和，然后将结果存入队列q。
    首先，定义一个从1到10000的整数列表numbers。确定每个进程应处理的数字数量（chunk_size），这里将列表划分为12份，每份包含尽可能相等数量的元素。将numbers列表拆分成12个子列表（chunks），每个子列表包含chunk_size个元素。
    使用multiprocessing.Manager().Queue()创建一个进程共享的队列q，允许不同进程之间传递数据。
    创建一个包含12个进程的进程池（with multiprocessing.Pool(processes=12) as pool:）。
    使用pool.starmap()方法并行调用square_and_sum函数，将每个子列表和队列q作为参数传递给每个进程。
    所有进程完成后，从队列q中获取每个进程计算的平方和部分结果（共12个），并求和得到最终结果。
    这段代码利用了Python的多进程特性，将计算任务分解为多个子任务，并行执行，从而提高了计算速度，尤其是在处理大量数据时。通过使用进程共享队列，不同进程间可以有效地通信，将各自计算的部分结果汇总。"""
    numbers = list(range(1, 10001))
    # 将列表划分为若干块，每个进程处理一块
    chunk_size = len(numbers) // 12
    # 将列表通过切片 拆分为若干个小列表 每个嵌套的子列表中包含若干个元素
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
    # 使用 multiprocessing.Manager().Queue() 创建进程共享的队列  manager = multiprocessing.Manager()
    q = multiprocessing.Manager().Queue()
    # 创建一个具有多个进程的进程池 可以方便地并行执行多个任务。
    with multiprocessing.Pool(processes=12) as pool:
        # 在每个进程中执行 square_and_sum 函数
        pool.starmap(square_and_sum, [(chunk, q) for chunk in chunks])
        # 汇总结果
        total_sum = sum(q.get() for _ in range(12))

    print("Total sum of squares:", total_sum)
