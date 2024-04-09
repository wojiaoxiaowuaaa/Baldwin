import concurrent.futures
from loguru import logger
import threading
import os


def task(task_id):
    # 获取当前线程 ID
    thread_id = threading.get_ident()
    logger.info(f"Task {task_id} started in thread {thread_id}")

    # 获取当前进程 ID
    process_id = os.getpid()
    logger.info(f"Task {task_id} started in process {process_id}")

    # 在这里执行任务的具体逻辑
    logger.info(f"Task {task_id} finished")


def main():
    # 设置线程池大小为 CPU 核心数量
    num_threads = 3

    # 创建线程池
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        # 提交任务到线程池
        tasks = [executor.submit(task, i) for i in range(num_threads)]

        # 等待所有任务完成
        for future in concurrent.futures.as_completed(tasks):
            future.result()


if __name__ == "__main__":
    main()
