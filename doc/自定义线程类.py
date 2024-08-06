import threading
import time
from typing import Callable, NoReturn


# 自定义线程类，继承自 threading.Thread
class MyThread(threading.Thread):
    def __init__(self, name: str, delay: int) -> NoReturn:
        super().__init__()
        self.name = name
        self.delay = delay

    # 重写 run() 方法，定义线程的行为
    def run(self) -> NoReturn:
        print(f"线程 {self.name} 开始运行")
        self.pr_time(self.name, self.delay, 5)
        print(f"线程 {self.name} 结束运行")

    # 自定义的方法，用于打印时间
    def pr_time(self, thread_name: str, delay: int, counter: int) -> NoReturn:
        while counter:
            time.sleep(delay)
            print(f"{thread_name}: {time.ctime(time.time())}")
            counter -= 1


# 创建两个线程实例
thread1 = MyThread("Thread-1", 1)
thread2 = MyThread("Thread-2", 1)

# 启动线程.调用 start() 方法启动线程。此时，线程将开始执行 run() 方法中的代码.
thread1.start()
thread2.start()

# 等待所有线程完成
thread1.join()
thread2.join()

print("主线程结束")
