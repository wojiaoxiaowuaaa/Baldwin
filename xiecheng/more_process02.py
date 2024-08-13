import multiprocessing
import os
from loguru import logger


def task(n):
    logger.info(f"执行任务的进程ID: {os.getpid()}")  # 输出的进程 ID 可能是相同的。这是因为在某些操作系统上，进程 ID 是有限的资源，并且在进程池中的进程被销毁和重新创建时，它们可能会被分配相同的进程 ID。
    return n * n


if __name__ == "__main__":
    # 定义要执行的任务列表
    tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    # 使用multiprocessing.cpu_count()获取CPU核心数来设置进程池的大小
    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        # 执行map操作，将任务分配给进程池中的进程
        # map_async是map的异步版本，它立即返回一个AsyncResult对象,而不是等待所有任务完成并返回结果列表。这意味着它不会阻塞主线程，而是立即返回，让你可以继续执行其他代码。
        result = pool.map_async(task, tasks)

        # 获取结果
        results = result.get()

        # 打印结果
        for r in results:
            logger.info(r)
