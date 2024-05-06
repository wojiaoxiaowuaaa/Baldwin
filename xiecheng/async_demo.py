import threading
import asyncio
from loguru import logger


async def hello():
    """验证 "协程是在一个线程中执行"。 通过打印当前线程，可以看到两个 coroutine 是由同一个线程 并发 执行的。"""
    logger.info(f'hello_1 ---> {threading.current_thread()}')
    await asyncio.sleep(3)
    logger.info(f'hello_2 ---> {threading.current_thread()}')


loop = asyncio.get_event_loop()
task_list = [asyncio.ensure_future(hello()), asyncio.ensure_future(hello())]
loop.run_until_complete(asyncio.wait(task_list))
loop.close()

"""
hello_1 ---> <_MainThread(MainThread, started 2332)>
hello_1 ---> <_MainThread(MainThread, started 2332)>
hello_2 ---> <_MainThread(MainThread, started 2332)>
hello_2 ---> <_MainThread(MainThread, started 2332)>
"""
