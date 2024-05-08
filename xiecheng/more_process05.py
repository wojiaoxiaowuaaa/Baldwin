import multiprocessing
import time
import os


def producer(queue):
    # 负责向共享队列中放入数据。
    print(os.getpid(), "Producer starts")
    for i in range(5):
        time.sleep(3)
        data = f"Message {i}"
        print(f"Producer puts: {data}")
        queue.put(data)


def consumer(queue):
    # 负责从共享队列中取出数据。
    print(os.getpid(), "Consumer starts")
    for i in range(5):
        time.sleep(3)
        data = queue.get()
        print(f"Consumer gets: {data}")
        print("\033[1;32m" + "*" * 30 + "\033[0m")


if __name__ == "__main__":
    # 主进程是整个脚本的执行起点,主要负责创建并控制其他两个子进程。
    print(os.getpid(), "Main process start")
    # 创建共享队列
    shared_queue = multiprocessing.Manager().Queue()

    # 创建两个进程，一个作为生产者，一个作为消费者
    producer_process = multiprocessing.Process(target=producer, args=(shared_queue,))
    consumer_process = multiprocessing.Process(target=consumer, args=(shared_queue,))

    # 启动进程
    producer_process.start()
    consumer_process.start()

    # 主进程通过 join() 等待两个子进程的结束，以保证整个脚本的正确执行.
    producer_process.join()
    consumer_process.join()
