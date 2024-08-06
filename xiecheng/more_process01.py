import multiprocessing
from os import getpid
import time


def worker(x):
    print(
        f"Processing  {x}  in process:  {getpid()}"
    )  # multiprocessing.current_process().pid
    time.sleep(3)  # 模拟耗时操作
    return x * x


if __name__ == "__main__":
    # 创建进程池，指定进程数量为3(3个不同的pid每个重复2次,设置进程数量为6则会有6个不同的pid)
    with multiprocessing.Pool(processes=6) as pool:
        # # 使用map方法提交任务
        # results_map = pool.map(worker, range(6))
        # print('Results using map:', results_map)

        # 使用apply方法提交任务
        # results_apply = [pool.apply(worker, args=(i,)) for i in range(6)]
        # print('Results using apply:', results_apply)

        # 使用apply_async方法提交异步任务
        results_apply_async = [pool.apply_async(worker, args=(i,)) for i in range(6)]
        # 使用get方法获取异步任务的结果
        results_async = [result.get() for result in results_apply_async]
        print("Results using apply_async:", results_async)
