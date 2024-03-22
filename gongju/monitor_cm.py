import psutil
import time

start = time.time()


def monitor_cpu_memory(interval=3):
    while time.time() - start < 15:
        # 获取 CPU 使用率
        cpu_percent = psutil.cpu_percent(interval=interval)
        # print(f"CPU 使用率：{cpu_percent}%")

        # 获取内存使用情况
        memory_info = psutil.virtual_memory()
        memory_percent = memory_info.percent
        used_memory = memory_info.used / (1024 ** 3)  # 转换为 GB
        total_memory = memory_info.total / (1024 ** 3)  # 转换为 GB
        available_memory = memory_info.available / (1024 ** 3)  # 转换为 GB
        # print(f"总内存：{total_memory:.2f} GB")
        # print(f"可用内存：{available_memory:.2f} GB")
        print(f"内存使用率：{memory_percent}%")
        print(f"已使用内存：{used_memory:.2f} GB")
        time.sleep(interval)


if __name__ == "__main__":
    monitor_cpu_memory()
