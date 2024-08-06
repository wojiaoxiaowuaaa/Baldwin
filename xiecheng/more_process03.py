import time
from multiprocessing import Process, Queue


# 生产者
def producers(q, name, food):
    """
    Queue:队列模块，不适合传大文件，通常传一些消息。
    """
    for i in range(3):
        print(f"{name}生产了{food} {i}")
        res = f"{food} {i}"
        # 把生产者生产的一大堆包子打包成一个变量，然后直接put到队列的管子里（q.put(res)），等待消费者去get
        # 创建队列
        q.put(res)
    # 队列结束标识
    # q.put(None)


# 消费者
def consumers(q, name):
    while True:
        # 把包子接收过来，创建接收队列
        receive = q.get()
        # 然后接收队列进行判断,如果receiv是'我生产完毕了'的话，消费者就停止再继续吃包子了
        if receive is None:
            break
        print(f"{name}吃掉了{receive}")


if __name__ == "__main__":
    # 创建队列对象
    q = Queue()

    p1 = Process(target=producers, args=(q, "张三丰", "狗不理包子"))
    c1 = Process(target=consumers, args=(q, "jack"))

    p1.start()
    c1.start()

    p1.join()  # 在 Python 多进程中，join方法用于等待子进程完成。它会阻塞当前进程，直到子进程执行完毕。(join方法会阻塞主进程，直到子进程完成。可以确保子进程在主进程之前完成，避免出现主进程先结束而子进程还在运行的情况。)
    # c1.join()  # 取消注释这行运行不会结束

    q.put(
        None
    )  # 主程序会等待生产者进程完成，然后向队列中放入结束标识，通知消费者进程结束 q.put(None) 的作用是作为生产者与消费者之间的同步信号。当生产者完成所有工作后，它会向队列中放入一个 None 对象。消费者在从队列中获取并处理元素时，如果发现拿到的是 None，则知道所有生产已经完成，因此可以停止消费并退出循环。
    # q.put(None)  # 几个消费者进程put几次
