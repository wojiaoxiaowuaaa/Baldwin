import asyncio
from random import randint


async def consumer(queue, id):
    while True:
        item = await queue.get()
        if item is None:  # 检测到结束信号
            break
        print(f"Consumer {id} got {item}")
        await asyncio.sleep(1)


async def producer(queue, id):
    for i in range(5):
        item = randint(1, 10)
        await queue.put(item)
        print(f"Producer {id} put {item}")
        await asyncio.sleep(1)
    await queue.put(
        None
    )  # 定义一个特殊的结束信号None 生产者在完成生产后将这个信号放入队列.消费者在获取到这个信号后退出循环.


async def main():
    queue = asyncio.Queue()
    consumers = [consumer(queue, i) for i in range(5)]
    producers = [producer(queue, i) for i in range(5)]
    await asyncio.gather(*consumers, *producers)
    # p = asyncio.create_task(producer(queue, 'produce'))
    # c = asyncio.create_task(consumer(queue, 'consume'))
    # await asyncio.gather(p, c)


asyncio.run(main())

# import queue
# import threading
#
#
# def producer(q):
#     for i in range(5):
#         q.put(i)
#         print(f"Produced: {i}")
#         # 模拟一些耗时操作
#         threading.Event().wait(1)
#
#
# def consumer(q):
#     while not q.empty():
#         item = q.get()
#         print(f"Consumed: {item}")
#         # 模拟一些耗时操作
#         threading.Event().wait(1)
#
#
# # 创建一个队列对象
# q = queue.Queue()
#
# # 创建生产者线程和消费者线程
# producer_thread = threading.Thread(target=producer, args=(q,))
# consumer_thread = threading.Thread(target=consumer, args=(q,))
#
# # 启动线程
# producer_thread.start()
# consumer_thread.start()
#
# # 等待线程结束
# producer_thread.join()
# consumer_thread.join()
