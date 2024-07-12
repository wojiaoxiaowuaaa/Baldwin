import sys
from pathlib import Path
from multiprocessing import Pool, cpu_count
from loguru import logger
from typing import List

# sys.path.insert(0, str(Path.cwd().parent))
from gongju.time_count import calculate_execution_time


class ManyProcess:
    def __init__(self):
        self.numbers: List = [10000000 + x for x in range(20)]

    @staticmethod
    def cpu_bound(number: int) -> int:
        # CPU(计算)密集型任务
        # logger.info(sum(i * i for i in range(number)))
        return sum(i * i for i in range(number))

    def calculate_p(self):
        # 多进程执行(进程池)
        with Pool(cpu_count()) as pool:
            # 将cpu_bound函数应用于numbers列表中的每个元素. map函数会自动分配任务到进程池中的进程上执行.
            pool.map(self.cpu_bound, self.numbers)

    def calculate_d(self):
        # 单进程执行(在Python中,当你直接在一个进程的主线程中顺序执行代码,没有显式地创建新的进程或线程来并行处理任务时，就可以认为是单进程执行)
        for _ in self.numbers:
            self.cpu_bound(_)


@calculate_execution_time
def one_p():
    ManyProcess().calculate_d()


@calculate_execution_time
def many_p():
    ManyProcess().calculate_p()


if __name__ == "__main__":
    many_p()
    one_p()
