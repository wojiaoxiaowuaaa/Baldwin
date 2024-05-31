import time
import os
from secrets import token_hex
from random import random
start = time.time()


def logs_reduce(pwd):
    # 以追加模式打开文件,(如果有则)清空文件内容truncate(0).
    with open(pwd, "a") as f: f.truncate(0)
    # while True   为一直写入数据到手动停止
    # while后跟判断条件.循环条件是:当前时间与开始时间的差小于3秒.
    while time.time() - start < 3:
        time.sleep(1)
        d = {"str": token_hex(10), "num": random()}
        with open(pwd, "a") as f:
            # a为追加模式,w为覆盖模式(每次都会清空文件导致只能写入一行数据). json.dumps(d)可以写入json类型的数据.
            # write() 方法接受一个字符串作为参数。writelines() 方法接受一个字符串序列（例如列表、元组）作为参数。
            f.writelines(str(d) + "\n")

    # os.system(f'cat {pwd}')


if __name__ == "__main__":
    logs_reduce("config/logs.txt")
