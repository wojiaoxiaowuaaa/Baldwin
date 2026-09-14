from multiprocessing import Process, Queue


def worker(q):
    """该脚本会创建两个进程。
    主进程：由主程序执行，负责创建工作进程、向队列中放入数据、等待工作进程结束等。
    工作进程：由 multiprocessing.Process 创建，通过 target=worker 参数指定执行的函数是 worker 函数。
    该进程在一个循环中不断从队列中获取数据，并进行处理，直到获取到特殊的终止信号为止。"""
    while True:
        item = q.get()  # 从队列中获取数据
        if item is None:
            break  # 如果获取到的数据为None，则退出循环
        # 处理数据...
        print("Processed:", item)


if __name__ == "__main__":
    q = Queue()
    p = Process(target=worker, args=(q,))
    p.start()
    for item in range(10):
        q.put(item)
    # 向队列中放入None,表示不再有数据了.注释掉这行，会导致进程一直运行.
    # put(None)的执行时机由主进程来调度.这行代码的作用是向队列中放入一个特殊的"终止"信号,以通知工作进程停止运行.这行代码被放置在主进程放入完所有数据后。因为工作进程会在获取到这个特殊信号后停止循环，并退出进程。
    q.put(None)
    # join()的执行时机由主进程来调度。这行代码的作用是等待工作进程结束。它会阻塞主进程，直到工作进程执行完毕，然后才会继续主进程的执行。这样做可以确保主进程在工作进程结束后,再继续执行后续的代码，以避免出现并发执行的问题。
    p.join()
    # p.close()  主进程退出时，Python 解释器会自动清理和关闭所有未关闭的资源。可以注释该行代码.
