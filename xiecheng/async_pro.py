import asyncio
import multiprocessing
from os import getpid
from loguru import logger

async def async_task(name, sleep_time=3):
    """异步任务，带睡眠时间的协程"""
    logger.info(f'Coroutine {name} is starting process is: {getpid()}')
    await asyncio.sleep(sleep_time)
    logger.info(f'Coroutine {name} {getpid()} is done')

def run_async_task(name):
    """运行异步任务的函数，包括异常处理"""
    try:
        asyncio.run(async_task(name))
    except Exception as e:
        logger.error(f'Error running async task {name}: {e}')

if __name__ == "__main__":
    processes = []

    for i in range(3):
        p = multiprocessing.Process(target=run_async_task, args=(i, ))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
