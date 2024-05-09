import time
from secrets import token_hex
import random

start = time.time()


def logs_reduce(pwd):
    # (如果有则)清空文件内容
    with open(pwd, "a") as f: f.truncate(0)
    # while True   为一直写入数据到手动停止
    # while后跟判断条件
    while time.time() - start < 3:
        # time.sleep(1)
        d = {"str": token_hex(10), "num": random.random()}
        with open(pwd, "a") as f:
            # a为追加模式,w为覆盖模式(每次都会清空文件导致只能写入一行数据). json.dumps(d)可以写入json类型的数据.
            f.writelines(str(d) + "\n")


if __name__ == "__main__":
    logs_reduce("doc/logs.txt")