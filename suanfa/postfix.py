import os
from color_pr import color_print_green


# 遍历文件夹查找指定格式的文件
def find_func(file, pwd):
    kings = []
    # os.walk：Python 的标准库函数，用于以递归的方式遍历目录树。
    # 它返回一个生成器，每次迭代都会返回一个包含三个元素的元组：当前目录的路径，当前目录下的子目录列表，以及当前目录下的文件列表。
    for root, dirs, files in os.walk(pwd):
        for f in files:
            name, postfix = os.path.splitext(f)
            if postfix == file:
                kings.append(f)
    return len(kings), kings


def total_func(pwd):
    # walk()是 Python 中用于遍历目录树的函数。它接受一个起始目录路径作为参数，并返回一个生成器，用于生成目录树中每个目录的信息.
    for root, dirs, files in os.walk(pwd):
        print(f"Directory: {root}")
        print(f"Total files: {len(files)}")
        total_size = sum(os.path.getsize(os.path.join(root, name)) for name in files)
        print(f"Total size: {total_size} bytes")
        color_print_green()


# landing = find_func('.py', '/Users/wl/Desktop')
# print(landing[0])

total_func('/Users/wl/Desktop')
