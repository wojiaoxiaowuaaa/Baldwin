from threading import Thread, Lock
from queue import Queue
from time import sleep
import random


# 生产者函数
def producer(queue, lock):
    for i in range(5):
        item = f"Item {i}"
        sleep(random.uniform(0.1, 0.5))  # 模拟生产过程中的延迟
        with lock:
            queue.put(item)
            print(f"Produced: {item}")


# 消费者函数
def consumer(queue, lock):
    while True:
        with lock:
            if not queue.empty():
                item = queue.get()
                sleep(random.uniform(0.1, 0.5))  # 模拟消费过程中的延迟
                print(f"Consumed: {item}")
            else:
                break


if __name__ == "__main__":
    queue = Queue()
    lock = Lock()

    # 创建生产者线程和消费者线程
    producer_thread = Thread(target=producer, args=(queue, lock))
    consumer_thread = Thread(target=consumer, args=(queue, lock))

    # 启动线程
    producer_thread.start()
    consumer_thread.start()

    # 等待线程结束
    producer_thread.join()
    consumer_thread.join()
