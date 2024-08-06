from suanfa.is_prime import is_prime

"""
1. if 语句：用于判断一个条件是否为真。如果条件为真，则执行 if 代码块中的语句。
2. elif 语句：是“else if”的缩写，用于在前面的 if 或 elif 条件不满足时，检查另一个条件。如果 elif 条件为真，则执行 elif 代码块中的语句。
3. else 语句：用于在所有前面的 if 和 elif 条件都不满足时执行代码块"""


def file_write():
    filenames = (
        "/Users/wl/Desktop/aaa.txt",
        "/Users/wl/Desktop/aaab.txt",
        "/Users/wl/Desktop/aaac.txt",
    )
    l = []
    try:
        for file in filenames:
            l.append(open(file, "w"))
        for num in range(1, 1000):
            if is_prime(num):

                if num <= 10:
                    l[0].write(str(num) + "\n")
                elif num <= 100:
                    l[1].write(str(num) + "\n")
                else:
                    l[2].write(str(num) + "\n")
    except IOError as e:
        print(e)
    finally:
        for f in l:
            f.close()


if __name__ == "__main__":
    file_write()
