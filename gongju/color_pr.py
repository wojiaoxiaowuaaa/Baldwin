"""
通过嵌入特定的ANSI转义序列来控制文本的颜色样式。
Red: \033[1;31m
Blue: \033[1;34m
Yellow: \033[1;33m
Magenta: \033[1;35m
Cyan: \033[1;36m
White: \033[1;37m
"""

import os
import psutil

banner = """
______                        ______             _
| ___ \_                      | ___ \           | |
| |_/ / \__ __   __  _ __   _ | |_/ /___   ___  | |
|  __/|  _// _ \ \ \/ /| | | ||  __// _ \ / _ \ | |
| |   | | | (_) | >  < \ |_| || |  | (_) | (_) || |___
\_|   |_|  \___/ /_/\_\ \__  |\_|   \___/ \___/ \_____\\
                       __ / /
                      /___ /

"""


def show_memory_info(s="this process"):
    """计算当前进程占用的内存大小"""
    pid = os.getpid()
    p = psutil.Process(pid)
    info = p.memory_full_info()
    memory = info.uss / 1024.0 / 1024
    print("\033[31m {} pid is {} memory used: {} M \033[0m".format(s, pid, memory))


def color_print_green(s="*"):
    """打印自定义彩色字符"""
    print("\033[1;32m" + s * 30 + "\033[0m")


def color_print_red(s="-"):
    """打印自定义彩色字符"""
    print("\033[1;31m" + s * 30 + "\033[0m")

def show_color_demo():
    print("\033[31m    \033[0m")
    print("\033[31mThis is red text\033[0m")
    print("\033[32mThis is green text\033[0m")
    print("\033[33mThis is yellow text\033[0m")
    print("\033[34mThis is blue text\033[0m")
    print("\033[35mThis is purple text\033[0m")
    print("\033[36mThis is cyan text\033[0m")
    print("\033[37mThis is white text\033[0m")
    print("\033[41m\033[37mThis is white text on red background\033[0m")
    print("\033[42m\033[37mThis is white text on green background\033[0m")
    print("\033[43m\033[37mThis is white text on yellow background\033[0m")
    print("\033[44m\033[37mThis is white text on blue background\033[0m")
    print("\033[45m\033[37mThis is white text on purple background\033[0m")
    print("\033[46m\033[37mThis is white text on cyan background\033[0m")
    print("\033[42m\033[37mThis is white text on green background\033[0m")
    



if __name__ == "__main__":
    # color_print_green()
    # color_print_red()
    # print("-------------------分割线-------------------")
    show_memory_info()
    show_color_demo()
