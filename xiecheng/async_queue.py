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
        # 在生产者 - 消费者模式中：
        # queue.task_done()用于告知队列中的一个任务已经处理完毕。join()用于等待队列中的所有任务都被处理完毕。
        # 如果你的代码中没有使用join()方法来等待所有任务完成，那么task_done()调用与否对程序的执行流程没有影响。但是，如果你想要确保所有队列中的任务都被正确处理，直到队列为空，再继续执行后续的代码，那么正确使用task_done()和join()就变得非常重要了。
        # queue.task_done()


async def main():
    queue = asyncio.Queue()
    p = asyncio.create_task(producer(queue))    # 任务是协程的包装器 表示要并发执行的协程
    c = asyncio.create_task(consumer(queue))
    await p
    await queue.put(None)
    await c

asyncio.run(main())
