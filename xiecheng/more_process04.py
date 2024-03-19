import multiprocessing


def worker(task_queue):
    while True:
        task = task_queue.get()
        if task is None:
            break
        print("Processed task --- ", task)


if __name__ == "__main__":
    shared_task_queue = multiprocessing.Manager().Queue()  # 创建共享队列对象。它允许多个进程之间共享数据。

    tasks = list(range(1, 6))  # 创建列表 用作队列的数据源

    num_workers = 3  # 控制创建进程的数量

    worker_processes = [multiprocessing.Process(target=worker, args=(shared_task_queue,)) for _ in range(num_workers)]  # 创建三个进程

    for process in worker_processes:
        process.start()

    for _ in tasks:
        shared_task_queue.put(_)

    for _ in range(num_workers):
        shared_task_queue.put(None)  # 向队列中放入和进程数量相同的特殊标记 None。这个特殊标记表示任务分发结束，每个进程在从队列中取出 None 后会终止循环，结束执行。

    for process in worker_processes:
        process.join()
