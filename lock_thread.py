import threading

# 共享资源  全局变量
shared_data = 0


def increment_shared_data():
    global shared_data

    for _ in range(1000000):
        # 无锁状态下，多个线程同时访问和修改共享资源
        shared_data += 1


def decrement_shared_data():
    global shared_data

    for _ in range(1000000):
        # 无锁状态下，多个线程同时访问和修改共享资源
        shared_data -= 1


# 创建两个线程分别对共享资源进行增加和减少操作
thread1 = threading.Thread(target=increment_shared_data)
thread2 = threading.Thread(target=decrement_shared_data)

# 启动线程
thread1.start()
thread2.start()

# 等待两个线程结束
thread1.join()
thread2.join()

# 打印最终共享资源值
print("Final shared_data value without lock:", shared_data)

"""
在某些情况下，即使在没有显式使用锁的情况下，多线程并发操作共享资源时可能看起来没有问题，最终结果仍然是正确的。
这是因为Python的全局解释器锁（Global Interpreter Lock，GIL）的存在。
GIL是Python解释器中的一个机制，它确保同一时刻只有一个线程执行Python字节码。尽管这有助于简化内存管理等方面的问题，
但它也意味着在多核CPU上并发执行Python线程时，由于GIL的存在，多线程并不能充分利用多核处理器的优势。
在上面的例子中，由于 GIL 的存在，两个线程在同一时刻只有一个能够执行 Python 字节码，
因此对 `shared_data` 的增加和减少操作是原子的。在这种情况下，即使没有显式使用锁，最终结果可能仍然是正确的。
然而，GIL并不是通用的解决并发问题的工具，因为它只在特定条件下生效。在其他情况下，特别是在涉及到更复杂的共享资源和更多线程的情况下，
使用锁或其他同步机制是保证程序正确性的最佳做法。不依赖GIL是更好的实践，尤其是在构建多线程应用时。
"""
