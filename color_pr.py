"""
Red: \033[1;31m
Blue: \033[1;34m
Yellow: \033[1;33m
Magenta: \033[1;35m
Cyan: \033[1;36m
White: \033[1;37m
"""
import os

import psutil


def show_memory_info(s='this process'):
    """计算当前进程占用的内存大小"""
    pid = os.getpid()
    p = psutil.Process(pid)
    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print(' {} pid is {} memory used: {} M'.format(s, pid, memory))


def color_print_green():
    print("\033[1;32m" + "*" * 30 + "\033[0m")


def color_print_red():
    print("\033[1;31m" + "*" * 30 + "\033[0m")


if __name__ == "__main__":
    color_print_green()
    color_print_red()
    print("-------------------分割线-------------------")
    show_memory_info()

