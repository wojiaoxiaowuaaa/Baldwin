import multiprocessing
import time


# 定义一个简单的进程函数
def worker(x):
    print("Worker started")
    time.sleep(x)  # 模拟任务执行时间
    print("Worker finished")


if __name__ == "__main__":

    # 创建一个进程对象
    process = multiprocessing.Process(target=worker, args=(1,))

    # 启动进程
    process.start()

    # 等待进程执行完成
    process.join()

    print("Main program finished")

