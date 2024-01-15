import psutil
import time
from gongju.color_print import color_print


def get_memory_usage():
    """获取内存使用率"""
    memory = psutil.virtual_memory()
    return f"Memory Usage: {memory.percent}%"


def get_cpu_usage():
    """获取 CPU 使用率"""
    cpu = psutil.cpu_percent(interval=1)
    return f"CPU Usage: {cpu}%"


if __name__ == "__main__":
    try:
        while True:
            print(get_memory_usage())
            print(get_cpu_usage())
            color_print()
            time.sleep(3)  # 间隔时间，可以根据需要调整
    except KeyboardInterrupt:
        print('over')
