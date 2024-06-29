import threading
import multiprocessing

# 共享资源  全局变量
shared_data = 0


def increment_shared_data():
    global shared_data

    for _ in range(1000):
        # 无锁状态下，多个线程同时访问和修改共享资源
        shared_data += 1


def decrement_shared_data():
    global shared_data

    for _ in range(1000):
        # 无锁状态下，多个线程同时访问和修改共享资源
        shared_data -= 1


if __name__ == '__main__':
    # 创建两个线程分别对共享资源进行增加和减少操作.这里没有使用锁threading.Lock()来保护共享资源的访问，因此可能存在竞争条件。
    thread1 = threading.Thread(target=increment_shared_data)
    thread2 = threading.Thread(target=decrement_shared_data)

    # 使用多进程总是能拿到预期的结果0
    # thread1 = multiprocessing.Process(target=increment_shared_data)
    # thread2 = multiprocessing.Process(target=decrement_shared_data)

    # 启动线程
    thread1.start()
    thread2.start()

    # 等待两个线程结束
    thread1.join()
    thread2.join()

    # 打印最终共享资源值
    print("Final shared_data value without lock:", shared_data)

"""
在某些情况下，即使在没有显式使用锁的情况下，多线程并发操作共享资源时可能看起来没有问题，最终结果仍然是正确的。这是因为Python
的全局解释器锁（Global Interpreter Lock，GIL）的存在。GIL是Python解释器中的一个机制，它确保同一时刻只有一个线程执行Python
字节码。尽管这有助于简化内存管理等方面的问题，但它也意味着在多核CPU上并发执行Python线程时，由于GIL的存在，多线程并不能充分利用
多核处理器的优势。在上面的例子中，由于 GIL 的存在，两个线程在同一时刻只有一个能够执行 Python 字节码，因此对 `shared_data` 
的增加和减少操作是原子的。在这种情况下，即使没有显式使用锁，最终结果可能仍然是正确的(也可能是错的结果随机)(但是使用多进程则总是
能拿到预期的结果)然而，GIL并不是通用的解决并发问题的工具，因为它只在特定条件下生效。在其他情况下，特别是在涉及到更复杂的共享
资源和更多线程的情况下，使用锁或其他同步机制是保证程序正确性的最佳做法。不依赖GIL是更好的实践，尤其是在构建多线程应用时。
"""


"""由于`multiprocessing`模块使用独立的进程，每个进程都有自己独立的内存空间，因此不存在像多线程那样的全局解释器锁（GIL）
的问题。这就意味着在多进程中，每个进程都能够并行执行，而不受共享资源的竞争影响。
1. **独立内存空间：**
   - 每个进程都有自己独立的内存空间，因此它们不会相互影响。在你的例子中，两个进程分别执行 `increment_shared_data` 和 
   `decrement_shared_data`，它们之间没有共享的内存，因此不会出现竞争条件。
2. **全局变量的复制：**
   - 当你在多进程中启动一个新进程时，`multiprocessing`模块会将主进程中的数据复制到新进程中，每个进程都有自己的独立副本。
   因此，每个进程都对自己的 `shared_data` 进行独立的增加和减少操作，而不会影响其他进程。
3. **进程间通信：**
   - `multiprocessing`模块通过进程间通信（IPC）机制，确保了进程之间的独立性。因此，你在一个进程中对 `shared_data` 
   进行的修改不会影响其他进程。
4. **无竞争条件：**
   - 由于每个进程都有自己独立的内存空间，且进程之间通过IPC保持独立，不存在多进程中的竞争条件，因此最终的 `shared_data` 
   值在每个进程中都能够按照预期的增加和减少操作得到。总体来说，使用多进程避免了多线程中可能存在的全局解释器锁问题，
   使得并行执行成为可能，特别适用于 CPU 密集型任务。"""
