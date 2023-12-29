import concurrent.futures
import multiprocessing


def heavy_computation(index):
    result = 0
    for _ in range(100000000):
        result += 1
    print(f"Task {index} finished on process {multiprocessing.current_process().name}")
    return result


if __name__ == "__main__":
    # 获取可用的核心数量
    num_cores = multiprocessing.cpu_count()  # 12

    try:
        # 使用 ProcessPoolExecutor，充分利用多核心
        with concurrent.futures.ProcessPoolExecutor(max_workers=num_cores) as executor:
            # 提交任务
            futures = [executor.submit(heavy_computation, i) for i in range(num_cores)]

            # 等待所有任务完成
            results = [future.result() for future in concurrent.futures.as_completed(futures)]

        # 打印每个任务的结果
        print("Results:", results)
    except concurrent.futures.process.BrokenProcessPool as e:
        print("BrokenProcessPool Error:", e)
