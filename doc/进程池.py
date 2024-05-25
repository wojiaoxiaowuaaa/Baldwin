import multiprocessing
from loguru import logger
import time


# 定义一个简单的任务函数，用于演示
def task(num):
    logger.info(f"Task {num} started")
    time.sleep(3)  # 模拟任务执行时间
    logger.info(f"Task {num} finished")
    return f"Result from Task {num}"


if __name__ == "__main__":
    # 创建一个进程池，指定进程数量为 12
    with multiprocessing.Pool(processes=12) as pool:
        # 提交多个任务给进程池执行.使用进程池的 map 方法将任务函数 task 应用到范围为 0 到 11 的每个数字上，并发执行多个任务。
        results = pool.map(task, range(12))
        logger.info(results)

    # 打印任务执行结果.<class 'list'>.
    # for result in results:
    #     logger.info(result)
