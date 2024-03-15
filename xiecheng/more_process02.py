import multiprocessing


# 定义一个简单的函数，用于执行任务
def task(n):
    """计算并打印n的平方"""
    return n * n


# 定义要执行的任务列表
tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# 创建一个进程池
if __name__ == '__main__':
    # 使用multiprocessing.cpu_count()获取CPU核心数来设置进程池的大小
    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        # 执行map操作，将任务分配给进程池中的进程
        # map_async是map的异步版本，它立即返回一个AsyncResult对象,而不是等待所有任务完成并返回结果列表。这是因为 map_async 是异步的，这意味着它不会阻塞主线程，而是立即返回，让你可以继续执行其他代码。
        result = pool.map_async(task, tasks)

        # 获取结果
        results = result.get()

        # 打印结果
        for r in results:
            print(r)
