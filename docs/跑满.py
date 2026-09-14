import multiprocessing
import os

def worker(num):
    """一个模拟CPU密集型任务的工作函数 跑满cpu"""
    print(f"Worker {num} started, PID: {os.getpid()}")
    # 增加计算任务的复杂度以延长运行时间
    total = 0
    for _ in range(10**8):  # 增加循环次数
        total += 1
    print(f"Worker {num} finished, Total: {total}")

if __name__ == "__main__":
    # 设置进程数为12，等于CPU核心数
    num_cores = 12
    processes = []

    # 创建并启动多个进程
    for i in range(num_cores):
        process = multiprocessing.Process(target=worker, args=(i,))
        processes.append(process)
        process.start()

    # 等待所有进程完成
    for process in processes:
        process.join()

    print("All processes finished.")
