import asyncio
import multiprocessing
from os import getpid
from loguru import logger


async def coro(name):
    """多进程 + 协程多任务 """
    logger.info(f'Coroutine {name} is starting process is {getpid()}')
    await asyncio.sleep(3)
    logger.info(f'Coroutine {name} {getpid()} is done')


def start_coro(name):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(coro(name))


if __name__ == "__main__":
    processes = []

    for i in range(3):
        p = multiprocessing.Process(target=start_coro, args=(f'Coro_{i}',))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
