import queue
import threading


def producer(q):
    for i in range(5):
        q.put(i)
        print(f"Produced: {i}")
        # sleep 1 second to simulate some time-consuming work
        threading.Event().wait(1)


def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consumed: {item}")
        # sleep 0.5 second to simulate some time-consuming work
        threading.Event().wait(0.5)


# create a Queue object with maxsize=2
q = queue.Queue(maxsize=2)

# create a producer thread and a consumer thread
producer_thread = threading.Thread(target=producer, args=(q,))
consumer_thread = threading.Thread(target=consumer, args=(q,))

# start threads
producer_thread.start()
consumer_thread.start()

# join threads
producer_thread.join()
q.put(None)  # signal the consumer thread to exit
consumer_thread.join()


"""
在上述代码中，展示了如何在 Python 中使用 Queue 类进行多线程安全数据传递：

我们创建了一个 Queue 对象，并在生产者线程中使用 put() 方法将数据放入队列中，在消费者线程中使用 get() 方法从队列中取出数据。

通过多线程实现生产者和消费者之间的并发操作。

此外，我们还通过 maxsize 参数限定了队列长度为 2，当队列已满时，将自动阻塞生产者线程；当队列为空时，将自动阻塞消费者线程。

注意，在消费者线程中我们通过判断 item 是否为 None 来退出循环，这是一种常见的关闭线程的方式。
"""
