import queue
import threading


def producer(q):
    for i in range(5):
        q.put(i)
        print(f"Produced: {i}")
        # 模拟一些耗时操作
        threading.Event().wait(1)


def consumer(q):
    while not q.empty():
        item = q.get()
        print(f"Consumed: {item}")
        # 模拟一些耗时操作
        threading.Event().wait(1)


# 创建一个队列对象
q = queue.Queue()

# 创建生产者线程和消费者线程
producer_thread = threading.Thread(target=producer, args=(q,))
consumer_thread = threading.Thread(target=consumer, args=(q,))

# 启动线程
producer_thread.start()
consumer_thread.start()

# 等待线程结束
producer_thread.join()
consumer_thread.join()
