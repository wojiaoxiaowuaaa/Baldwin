import multiprocessing
import os


def worker():
    """多进程测试  子进程ID各不相同 子进程的getppid(父进程)与__main__函数中主进程ID相同"""
    print(f"Worker process ID: {os.getpid()}")
    # print(f"Worker father process ID: {os.getppid()}")


if __name__ == "__main__":
    print(f"Main process ID: {os.getpid()}")

    processes = []
    for _ in range(5):
        process = multiprocessing.Process(target=worker)
        process.start()
        processes.append(process)

    for process in processes:
        process.join()
