import os
from pathlib import Path


def find_file(file: str, pwd: str) -> tuple:
    """
    遍历文件夹查找指定格式(后缀)的文件并进行数据统计
    os.walk：Python 的标准库函数用于以递归的方式遍历目录树 它返回一个生成器 每次迭代都会返回一个包含三个元素的元组：当前目录的路径，当前目录下的子目录列表，以及当前目录下的文件列表.
    :param file: 文件后缀
    :param pwd: 文件夹路径
    """
    results = []
    for root, dirs, files in os.walk(pwd):
        for f in files:
            name, postfix = os.path.splitext(f)
            if postfix == file:
                results.append(f)

    return len(results), results


def find_file01(directory: Path, pattern: str) -> list[Path]:
    """
    遍历指定目录及其子目录，查找匹配指定模式的文件。
    :param directory: 要遍历的目录路径的Path对象 (例如 Path("/Users/wl/Downloads"))
    :param pattern: 文件匹配模式（例如 '*.txt'）
    :return: 匹配的文件列表
    """
    if not directory.is_dir():
        raise ValueError(f"{directory} is not a valid directory.")

    # rglob()递归地遍历目录及其子目录,并匹配指定模式的文件或目录.
    matched_files = list(directory.rglob(pattern))
    return matched_files


def find_file02(file: str, pwd: str) -> None:
    """
    遍历目录查找指定的文件文件名所在的绝对路径 这里的文件名必须是完整的不能使用通配符
    :param file: 文件名
    :param pwd: 目录路径
    """
    for root, dirs, files in os.walk(pwd):
        if file in files:
            result = os.path.join(root, file)
            print(result)


# for i in (var := find_file01(Path.cwd().parent, "*.py")): print(i)
# find_file02("__init__.py", "/Users/wl/Downloads")
