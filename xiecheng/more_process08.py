import multiprocessing
import threading
import time


# 计算 Fibonacci 数列的函数
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# 多进程执行的函数
def process_task():
    print(fibonacci(35))


# 多线程执行的函数
def thread_task():
    print(fibonacci(35))


# 测试多进程
def test_multiprocessing():
    start_time = time.time()
    processes = []
    num_processes = 12  # CPU 的逻辑核心数
    for _ in range(num_processes):
        p = multiprocessing.Process(target=process_task)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end_time = time.time()
    print(f"多进程执行时间：{end_time - start_time} 秒")


# 测试多线程
def test_threading():
    start_time = time.time()
    threads = []
    num_threads = 12
    for _ in range(num_threads):
        t = threading.Thread(target=thread_task)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end_time = time.time()
    print(f"多线程执行时间：{end_time - start_time} 秒")


if __name__ == "__main__":
    test_threading()
    test_multiprocessing()
