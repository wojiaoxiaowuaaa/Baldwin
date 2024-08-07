import threading
import time

"""在下面这个例子里,我们创建两个线程，每个线程都会增加全局变量`counter`一百万次。如果线程是并行运行的，`counter`的最终值是200万。
但是，由于GIL的存在，这两个线程不能同时运行，所以实际的结果小于200万(每次也不行结果都不同)"""
counter = 0


def increment_counter():
    global counter
    for _ in range(1000000):
        counter += 1


thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(counter)

"""全局解释器锁（Global Interpreter Lock，简称GIL）是Python解释器中的一个重要概念。它是一种互斥锁，
用于确保在任何给定时刻只有一个线程在解释器中执行Python字节码，即在单个进程内，Python解释器的并发性被限制在一个线程上执行.这意味着在多线程程序中，多个线程不能同时利用多核处理器的能力.
GIL的存在主要是为了简化Python解释器的实现，以避免在解释器内部处理线程间的资源竞争和复杂性。然而，它也导致了Python在CPU密集型任务上的性能限制.对于I/O密集型任务，GIL通常不会成为性能瓶颈，因为线程在等待I/O操作时会释放GIL.下面是一个简单的示例来说明GIL的影响"""


# 考虑一个计算密集型任务计算一个大素数列表的示例：
def calculate_prime(n):
    primes = []
    for num in range(2, n + 1):
        # all() 是Python内置函数之一，用于判断可迭代对象中的所有元素是否都为真（True）。如果可迭代对象中的所有元素都为真，all() 函数返回 True；否则，返回 False
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primes.append(num)
    return primes


start = time.time()

# 创建两个线程来计算素数
t1 = threading.Thread(target=calculate_prime, args=(500000,))
t2 = threading.Thread(target=calculate_prime, args=(500000,))

t1.start()
t2.start()

t1.join()
t2.join()

# 测试使用多进程这里可以节约一倍的时间
print(time.time() - start)

"""尽管我们使用了两个线程来计算不同的素数列表，但由于GIL的存在，这两个线程不会并行执行，而是交替执行。这导致多线程在计算密集型任务上无法充分利用多核处理器的性能。
要注意，GIL只影响了CPython（Python的标准实现）。其他Python实现，如Jython（用于Java虚拟机）或IronPython（用于.NET Framework），不一定有GIL，因此在某些情况下可以更好地利用多核处理器。 对于解决GIL的问题，可以考虑以下方法：
1. 使用多进程而不是多线程，每个进程都有自己独立的Python解释器和内存空间，因此不受GIL的限制。
2. 使用其他语言编写计算密集型部分的代码，例如C/C++，然后通过Python的C扩展来调用这些代码。
3. 对于I/O密集型任务，可以使用异步编程和协程，例如`asyncio`库，以避免线程等待I/O时浪费时间.请根据您的具体需求和性能要求来选择适当的方法.


通常情况下，一个普通的Python脚本在执行时是以一个主线程的方式在运行。这个主线程执行脚本的顶层代码，包括全局变量的初始化、函数调用以及主要的程序逻辑。
Python解释器使用全局解释器锁（Global Interpreter Lock，GIL）来确保在多线程环境中只有一个线程可以执行Python字节码。
这意味着，虽然您可以使用`threading`模块创建多个线程，但这些线程在执行Python字节码时会交替运行，而不是真正并行执行。
这也是为什么Python中的多线程不适用于CPU密集型任务，但对于I/O密集型任务仍然有用，因为在I/O操作等待时，GIL会释放，允许其他线程执行。
如果您希望充分利用多核处理器并实现真正的并行执行，可以考虑使用`multiprocessing`模块创建多个进程。每个进程都有自己独立的Python解释器和内存空间，
因此它们可以在多个核上同时运行，不受GIL的限制。这适用于CPU密集型任务。

在Python脚本执行时，它会在操作系统中创建一个独立的进程，这个进程是一个Python解释器进程，用来运行您的脚本。这个Python解释器进程是您的脚本的主进程，负责执行脚本中的顶层代码和主要逻辑。
这个主进程通常是由您的操作系统分配的，它会在执行脚本时启动，执行脚本中的代码，然后在脚本执行完成后退出。如果您在脚本中使用多线程或多进程，还会创建相应数量的子线程或子进程，这些子线程或子进程由主进程管理。
主进程的行为会受到操作系统的管理，包括进程的创建、销毁、资源管理等。如果您在脚本中使用多线程或多进程，主进程也会负责管理这些辅助线程或子进程。总之，主进程是执行Python脚本的起点，它是您的脚本在操作系统中的代表"""
