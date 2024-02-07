import queue, threading

q = queue.Queue()


def product(arg):
    q.put(str(arg) + "生产者")


def consumer(arg):
    print(f"消费者{arg}---", q.get())


for i in range(3):
    t = threading.Thread(target=product, args=(i,))
    t.start()

for j in range(3):
    t = threading.Thread(target=consumer, args=(j,))
    t.start()

# print(dir(q))
