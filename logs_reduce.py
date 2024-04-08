import json
import time
import random
start = time.time()


def logs_reduce():
    # while True   为一直写入数据到手动停止
    # while后跟判断条件
    while time.time() - start < 10:
        time.sleep(1)
        d = {"key": random.choice("abcdefg"), "value": random.random()}
        print(d)
        with open("doc/logs.txt", "a+") as f:
            f.writelines([json.dumps(d) + "\n"])


if __name__ == '__main__':
    logs_reduce()
