# print("# -------------------设置分块任务-------------------")

"""
Red: \033[1;31m
Blue: \033[1;34m
Yellow: \033[1;33m
Magenta: \033[1;35m
Cyan: \033[1;36m
White: \033[1;37m
"""


def color_print_green():
    print("\033[1;32m" + "*" * 30 + "\033[0m")


def color_print_red():
    print("\033[1;31m" + "*" * 30 + "\033[0m")


def main():
    color_print_green()
    color_print_red()


if __name__ == "__main__":
    main()
