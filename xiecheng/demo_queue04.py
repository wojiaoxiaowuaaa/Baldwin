# 消费者
def consumer():
    msg = ''
    while True:
        """n = yield msg 的执行过程如下：
        1. 当代码执行到 yield msg 时，生成器会暂停执行，并将 msg 的值返回给调用方。
        2. 调用方可以通过某种方式（如 c.send(n)）向生成器发送一个值 n。
        3. 当生成器接收到发送的值 n 时，n = yield msg 中的 n 会被赋值为接收到的值，然后生成器继续执行后续的代码。
        它们之间的关系是，c.send(n) 用于向生成器发送数据，而 n = yield msg 用于在生成器内部接收和处理发送的数据。通过这种方式，生成器和调用方可以进行交互和通信。"""
        n = yield msg
        if not n:
            return
        print(f"消费者消费:{n}")
        msg = '消费完成'

# 生产者
def produce(c):
    # 启动协程. c 是对 consumer 生成器对象的引用，而 c.send(n) 用于与生成器进行交互，发送数据并接收返回值。
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print(f"生产者生产: {n}")
        # 发送数据给生成器
        # 并接收协程返回的参数
        msg = c.send(n)
        print(f"收到消费者消息: {msg}")
    # c.close() 的作用是关闭生成器。当调用 c.close() 时，会向生成器发送一个特殊的信号，通常表示生成器的工作已经完成或不再需要继续
    c.close()

# 调用生产者
produce(consumer())
