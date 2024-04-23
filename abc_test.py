import threading
import time


def count(n):
    c = 0
    while c < n:
        c += 1


def main():
    start = time.time()
    threads = []
    for _ in range(12):
        t = threading.Thread(target=count, args=(100000000,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(time.time() - start)  # 2.197813034057617


if __name__ == "__main__":
    main()
