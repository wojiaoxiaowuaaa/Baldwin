"""
对象含有生产者、队列、消费者
Queue:队列模块，不适合传大文件，通常传一些消息。
多生产者进程和多消费者进程
"""
import time
from multiprocessing import Process, Queue


# 生产者
def producers(q, name, food):
    for i in range(3):
        print(f'{name}生产了{food}{i}')
        res = f'{food}{i}'
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
        print(f'{name}吃掉了{receive}')


if __name__ == '__main__':
    # 创建队列对象
    q = Queue()

    p1 = Process(target=producers, args=(q, '张三丰', '狗不理包子'))
    c1 = Process(target=consumers, args=(q, 'jack'))

    p1.start()
    c1.start()

    p1.join()  # 用join方法保证生产者生产完毕
    # c1.join()  # 取消注释这行运行不会结束

    q.put(None)  # 注释掉这行代码不会结束   阻塞  put none的作用是结束进程
    # q.put(None)  # 几个消费者进程put几次

'''
问题01：
为什么会产生生产9个包子，吃掉了6个包子的问题？
解答：
put一次None，结束一个进程，总共put了3次None，
但是只接收了两个None，所以就会导致生产9个包子，
只吃掉了6个包子。

问题02：
为什么是两次None？
q.put(None)
q.put(None)

问题03：
问什么q.put(None)要写在这个地方？
'''
