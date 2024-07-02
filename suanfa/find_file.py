import os
from pathlib import Path


def find_func(file, pwd):
    # 遍历文件夹查找指定格式的文件并进行数据统计
    # find_func('.py', '/Users/wl/Desktop')
    kings = []
    # os.walk：Python 的标准库函数，用于以递归的方式遍历目录树。
    # 它返回一个生成器，每次迭代都会返回一个包含三个元素的元组：当前目录的路径，当前目录下的子目录列表，以及当前目录下的文件列表。
    for root, dirs, files in os.walk(pwd):
        for f in files:
            name, postfix = os.path.splitext(f)
            if postfix == file:
                kings.append(f)
    return len(kings), kings


def find_files(directory: Path, pattern: str):
    """
    遍历指定目录及其子目录，查找匹配指定模式的文件。

    :param directory: 要遍历的目录路径
    :param pattern: 文件匹配模式（例如 '*.txt'）
    :return: 匹配的文件列表
    """
    if not directory.is_dir():
        raise ValueError(f"{directory} is not a valid directory.")
    # rglob()递归地遍历目录及其子目录,并匹配指定模式的文件或目录.
    matched_files = list(directory.rglob(pattern))
    return matched_files


# var = find_files(Path.cwd(), '*.txt')
for i in (var := find_files(Path('.'), '*.py')): print(i)

