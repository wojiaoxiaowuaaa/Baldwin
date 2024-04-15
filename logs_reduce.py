import json
import time
import random
import loguru
start = time.time()


def logs_reduce():
    # while True   为一直写入数据到手动停止
    # while后跟判断条件
    while time.time() - start < 3:
        time.sleep(1)
        d = {"key": random.choice("abcdefghijklmn"), "value": random.random()}
        # loguru.logger.info(d)
        with open("doc/logs.txt", "a") as f:
            f.writelines([json.dumps(d) + "\n"])


if __name__ == '__main__':
    logs_reduce()
