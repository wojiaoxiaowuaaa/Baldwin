import os
import asyncio
import multiprocessing
from loguru import logger


async def get_directory_info(directory):
    # 多进程+多任务. async for 语法用于异步迭代，但是在这个脚本中，os.walk() 并不是异步操作，因此无法直接在 async for 中使用。
    for root, dirs, files in os.walk(directory):
        logger.info(f"Directory: {root}")
        # for name in files:
        #     file_path = os.path.join(root, name)
        #     file_size = os.path.getsize(file_path)
        #     print(f"File: {file_path}, Size: {file_size} bytes")
        # await asyncio.sleep(0)  # 让出控制权，避免阻塞事件循环


def process_func(directory):
    asyncio.run(get_directory_info(directory))


if __name__ == "__main__":
    processes = []
    for _ in range(multiprocessing.cpu_count()):
        p = multiprocessing.Process(target=process_func, args=("/Users/wl/Desktop/01需求日记",))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

"""

import os
from loguru import logger


def total_func(pwd):
    # 对比上面的脚本可以发现多进程多任务在某些场景下能够节约时间
    for root, dirs, files in os.walk(pwd):
        logger.info(f"Directory: {root}")
        # print(f"Total files: {len(files)}")
        total_size = sum(os.path.getsize(os.path.join(root, name)) for name in files)
        # print(f"Total size: {total_size} bytes")
        # color_print_green()


total_func('/Users/wl/go')

"""
