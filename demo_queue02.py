import queue, threading

q = queue.Queue()


def product(arg):
    q.put(str(arg) + "包子")


def consumer(arg):
    print(f"consumer{arg}---", q.get())


for i in range(3):
    t = threading.Thread(target=product, args=(i,))
    t.start()
for j in range(3):
    t = threading.Thread(target=consumer, args=(j,))
    t.start()


print(dir(q))
