import asyncio
import multiprocessing
from os import getpid
from loguru import logger


async def async_task(name, sleep_time=3):
    """定义异步任务"""
    logger.info(f"Coroutine {name} is starting process is: {getpid()}")
    await asyncio.sleep(sleep_time)
    logger.info(f"Coroutine {name} {getpid()} is done")


def run_async_task(name):
    """定义函数 尝试运行异步任务.run_async_task函数起到了桥接的作用,它是一个普通的同步函数,可以被multiprocessing.Process直接调用.在run_async_task函数内部,它通过asyncio.run(async_task(name))来运行异步协程函数,这样既满足了multiprocessing.Process对可调用目标的需求,又能执行异步任务."""
    try:
        asyncio.run(async_task(name))
    except Exception as e:
        logger.error(f"Error running async task {name}: {e}")


if __name__ == "__main__":
    # 使用异步编程和多进程来执行并行任务
    processes = []

    for i in range(3):
        p = multiprocessing.Process(target=run_async_task, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
