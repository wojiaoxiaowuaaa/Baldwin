import asyncio
import random
from loguru import logger


async def producer(queue):
    for i in range(6):
        # 协程的切换是由await关键字触发的。当协程遇到await时，会将控制权让给事件循环，事件循环可以切换到其他协程运行。
        await asyncio.sleep(random.random())
        item = f"item: {i}"
        await queue.put(item)
        logger.info(f"Produced {item}")


async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        logger.info(f"consumer: {item}")
        queue.task_done()


async def main():
    queue = asyncio.Queue()
    # 任务是协程的包装器，表示要并发执行的协程。
    p = asyncio.create_task(producer(queue))
    c = asyncio.create_task(consumer(queue))
    await p
    await queue.put(None)
    await c


asyncio.run(main())
