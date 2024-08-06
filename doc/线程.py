import threading
import multiprocessing

"""Python 解释器进程是指执行 Python 代码的进程，它负责解释和执行 Python 程序。在运行 Python 脚本时，操作系统会创建一个 Python 解释器进程，并将脚本加载到该进程中进行解释执行。
Python 解释器进程通常由操作系统的执行器（例如，在 Linux 上是 `python` 命令，Windows 上是 `python.exe`）启动。一旦 Python 解释器进程启动，它会按照所运行的脚本的指令逐行解释和执行代码。
Python 解释器进程负责管理内存、线程、资源分配和进程间通信等任务。它也会维护全局解释器锁（GIL），控制多线程环境下的并发访问。
需要注意的是，当我们在命令行或集成开发环境（IDE）中运行一个 Python 脚本时，实际上是通过启动一个 Python 解释器进程来执行该脚本。每次执行脚本都会创建一个新的 Python 解释器进程"""


def print_thread_info():
    current_thread = threading.current_thread()
    print(f"当前线程名称：{current_thread.name}")
    print(f"当前线程ID：{current_thread.ident}")


def print_process_info():
    current_process = multiprocessing.current_process()
    print(f"当前进程名称：{current_process.name}")
    print(f"当前进程ID：{current_process.pid}")


if __name__ == "__main__":
    print("线程信息:")
    print_thread_info()

    print("\n进程信息：")
    print_process_info()
