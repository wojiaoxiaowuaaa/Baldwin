"""文件读写模式:
r	用于读,文件不存在会报错 IOError ,如果不传 mode 参数时默认为该模式
w	用于写,文件不存在会自动创建
a	用于追加,文件不存在会自动创建
b	二进制模式
r+	相当于 r+w ,可读可写,如果文件不存在会报错 IOError
w+	相当于 w+r ,可读可写,如果文件不存在会自动创建
a+	相当于 a+r ,可追加可写,如果文件不存在会自动创建
默认都是以文本模式打开文件,如果要以二进制模式打开,那么就给对应模式加上 b 即可,如 rb、wb、ab、rb+、wb+、ab+ 等

序列化&反序列化:
Python的json模块提供了把内存中的对象序列化的方法.dump的功能就是把Python对象encode为json对象,一个编码过程.
注意json模块提供了json.dumps和json.dump方法,区别是dump可以直接写到文件中,而dumps到一个字符串,这里的s可以理解为string.
"""

import time
import os
from secrets import token_hex
from random import random

start = time.time()


def logs_reduce(pwd):
    # 以追加模式打开文件,(如果有则)清空文件内容truncate(0).
    with open(pwd, "a+") as f:
        f.truncate(0)
    # while True   为一直写入数据到手动停止
    # while后跟判断条件.循环条件是:当前时间与开始时间的差小于3秒.
    while time.time() - start < 3:
        # time.sleep(0.5)
        d = {"str": token_hex(10), "num": random()}
        with open(pwd, "a") as f:
            # a为追加模式,w为覆盖模式(每次都会清空文件导致只能写入一行数据). json.dumps(d)可以写入json类型的数据.
            # write() 方法接受一个字符串作为参数.writelines() 方法接受一个字符串序列(例如列表、元组)作为参数.
            f.writelines(str(d) + "\n")

    os.system(f"cat {pwd}")


if __name__ == "__main__":
    logs_reduce("config/logs.txt")
