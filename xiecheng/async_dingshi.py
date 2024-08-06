import asyncio
from loguru import logger
from color_pr import color_print_red

"""
在需要执行定时任务的应用中，可以使用异步操作来管理定时任务的执行。这样，你可以在单个线程中安排多个定时任务而不需要创建多个线程。
这个示例说明了在单个线程中使用异步操作的场景，其中 asyncio 是 Python 中用于支持异步编程的标准库。
异步操作可以提高程序的性能，特别是在需要处理大量 I/O 操作的情况下。
"""


async def task_one():
    logger.info("Task One executed.")


async def task_two():
    # logger.info("Task Two executed.")
    logger.info("--------------------")


async def main():
    loop = asyncio.get_event_loop()
    end = loop.time() + 5.0
    while True:
        if loop.time() > end:
            break
        # 在这个脚本中，所有的异步任务task_one() 和 task_two() 都在单个线程中执行，由事件循环调度执行。
        await asyncio.gather(task_one(), task_two())

        # 每秒执行一次任务
        await asyncio.sleep(1)


# 脚本执行时，主进程是运行 Python 解释器的进程。在这个例子中，主进程会执行异步脚本并创建一个事件循环。
asyncio.run(main())
