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
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(coro(name))
    # 这是在 Python 3.7 版本中引入的高级方法，它简化了 asyncio 应用程序的启动和管理。  asyncio.run() 函数会自动创建一个新的事件循环对象，并在执行完传入的协程后自动关闭事件循环。(更优雅 上面的写法不推荐)
    asyncio.run(coro(name))


if __name__ == "__main__":
    processes = []

    for i in range(3):
        p = multiprocessing.Process(target=start_coro, args=(f'Coro_{i}',))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
