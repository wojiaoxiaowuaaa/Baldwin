import multiprocessing
from os import getpid
from loguru import logger

"""
Process 类表示一个进程，它有 start() 和 join() 方法用于启动进程&&等待进程结束。下面是关于这两个方法的介绍：

start() 方法：
start() 方法用于启动一个进程，使其开始执行进程函数中定义的任务。
一旦调用了 start() 方法，进程会在后台开始执行，并立即返回到主程序中继续执行后续代码，而不会阻塞主程序的执行。
在 start() 方法之后，可以使用 join() 方法等待进程执行完成，也可以通过其他方式来管理进程的执行和交互。

join() 方法：
join() 方法用于等待进程执行完成。主程序会在调用 join() 方法处被阻塞，直到被调用的进程(子进程)执行完毕。
如果在调用 join() 方法时，指定了超时时间参数，主程序会在超时时间内等待进程执行完成，超时后继续执行后续代码。
join() 方法通常用于等待所有子进程完成，然后再继续执行主程序的后续逻辑。"""


def worker(q):
    logger.info(getpid())
    while True:
        task = q.get()
        if task is None:
            break
        print("Processed task --- ", task)


if __name__ == "__main__":
    shared_task_queue = multiprocessing.Manager().Queue()  # 创建共享队列对象。它允许多个进程之间共享数据。

    tasks = list(range(1, 6))  # 创建列表 用作队列的数据源

    num_workers = 5  # 控制创建进程的数量

    worker_processes = [multiprocessing.Process(target=worker, args=(shared_task_queue,)) for _ in range(num_workers)]

    for process in worker_processes:
        process.start()

    for _ in tasks:
        shared_task_queue.put(_)

    for _ in range(num_workers):
        shared_task_queue.put(None)  # 向队列中放入和进程数量相同的特殊标记 None。这个特殊标记表示任务分发结束，每个进程在从队列中取出 None 后会终止循环，结束执行。给每个进程都发送一个结束信号，告诉它们停止处理任务，这样才能保证所有的任务都被处理完毕。

    for process in worker_processes:
        process.join()

    print("main process end")  # 如果写在Main函数外 会重复打印num_workers+1次
