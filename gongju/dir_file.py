"""
import os
import tempfile
import unittest
from clean_dir import clean_up
from loguru import logger

# 针对clean_up函数编写单测
class TestCleanUp(unittest.TestCase):
    def setUp(self):
        # 创建一个临时目录
        self.test_dir = tempfile.mkdtemp()
        logger.info(self.test_dir)

    def tearDown(self):
        # 测试完成后清理临时目录
        if os.path.exists(self.test_dir):
            os.rmdir(self.test_dir)
            logger.info(os.path.exists(self.test_dir))

    def test_clean_up_existing_directory(self):
        # 测试删除存在的目录
        dir_name = os.path.join(self.test_dir, 'test_subdir')
        os.mkdir(dir_name)
        self.assertTrue(os.path.exists(dir_name))
        clean_up(dir_name)
        self.assertFalse(os.path.exists(dir_name))

    def test_clean_up_non_existing_directory(self):
        # 测试尝试删除不存在的目录
        dir_name = os.path.join(self.test_dir, 'non_existing_dir')
        self.assertFalse(os.path.exists(dir_name))
        clean_up(dir_name)  # 不应该抛出异常
        self.assertFalse(os.path.exists(dir_name))  # 确认目录仍然不存在


if __name__ == '__main__':
    unittest.main()

"""
import os
import re
import sys
import subprocess
import shutil
from pathlib import Path
import requests
import uuid


def clean_dir(dir):
    """删除当前脚本下的指定目录
    :param dir: 当前脚本所在目录下待删除的目录"""
    cache_directory = os.path.join(os.path.dirname(__file__), dir)
    print(cache_directory)
    try:
        if os.path.exists(cache_directory):
            # shutil 是 Python 标准库中的一个模块，提供了一些用于文件和目录操作的高级功能。
            # 它是 "shell utility" 的缩写，旨在提供类似于 shell 命令的功能。
            shutil.rmtree(cache_directory)
            print(f"Directory '{cache_directory}' deleted successfully.")
        else:
            print(f"Directory '{cache_directory}' does not exist.")
    except Exception as e:
        print(f"Error during clean up: {e}")


def rm_rf(pwd):
    """删除制定的目录 pwd:待删除目录路径.
    使用subprocess模块来运行系统命令如subprocess.run(['ls'])
    也可以使用os.system('echo $PATH')这种方式虽然更简洁轻便但是不具备复杂情况的处理能力 """
    subprocess.run(["rm", "-rf", pwd], check=True)


def delete_file(path, suffix):
    """递归遍历目录 删除指定后缀的文件如.log"""
    if not os.path.exists(path):
        return False

    for root, dirs, files in os.walk(path):
        for _ in files:
            if _.endswith(suffix):
                os.remove(os.path.join(root, _))

        print(f'删除{suffix}后缀文件完成')


def count_lines_and_size(json_file):
    """统计制定文件的行数与存储空间占用"""
    count = 0
    size = os.path.getsize(json_file) / 1024  # 将文件大小转换为KB  默认的单位是字节

    with open(json_file, "r") as f:
        for _ in f:
            count += 1  # 循环结构会逐行读取文件 json_file 的内容.可使用 _.strip() 去掉每行末尾的换行符.

    return count, size


# def add_webp_extension(folder_path):
#     for file in os.listdir(folder_path):
#         # 获取文件的绝对路径
#         file_path = os.path.join(folder_path, file)
#
#         # 判断是否为文件
#         if os.path.isfile(file_path):
#             # 如果文件名中不包含.webp后缀,则添加后缀
#             if not file.endswith("1--11.webp"):
#                 new_file_name = file + "1--11.webp"
#                 new_file_path = os.path.join(folder_path, new_file_name)
#                 # 重命名文件
#                 os.rename(file_path, new_file_path)
#                 print(f"Renamed file: {file} to {new_file_name}")


def clean_filename(filename):
    # 使用正则表达式去除特殊字符,保留字母、数字、下划线和点
    return re.sub(r"[^a-zA-Z0-9_.]", "", filename)


def rename_files_in_directory(directory):
    """批量重命名指定目录下的文件"""
    for filename in os.listdir(directory):
        # 获取文件的完整路径
        full_path = os.path.join(directory, filename)

        # 如果是文件而不是文件夹
        if os.path.isfile(full_path):
            # 去除特殊字符
            clean_name = clean_filename(filename)

            # 获取新的完整路径
            new_full_path = os.path.join(directory, clean_name)

            # 重命名文件
            os.rename(full_path, new_full_path)
            print(f"Renamed: {filename} -> {clean_name}")


punctuation_mapping = {
    "，": ",",
    "。": ".",
    "！": "!",
    "？": "?",
    "；": ";",
    "：": ":",
    "（": "(",
    "）": ")",
    "【": "[",
    "】": "]",
    "“": '"',
    "”": '"',
    "‘": "'",
    "’": "'",
}


def replace_punctuation_in_dir(directory: str, exclude_files: list):
    """替换文件夹中的中文标点符号为英文格式 排除指定的文件不做替换"""

    current_script = os.path.abspath(sys.argv[0])  # 获取当前脚本的绝对路径

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # 检查文件是否在排除列表中，或者是否是当前脚本文件  跳过排除的文件
            if file_path in exclude_files or file_path == current_script:
                continue

            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            for chinese, english in punctuation_mapping.items():
                content = re.sub(chinese, english, content)

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

            print("目录标点替换完成")


def replace_punctuation_in_file(file_path: str):
    """替换文件中的中文标点符号为英文格式"""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    for chinese, english in punctuation_mapping.items():
        content = re.sub(chinese, english, content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print("文件标点替换完成")


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


def download_images_from_file(filename, output_dir):
    """根据指定文件中的URL下载图片到指定目录"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(filename, "r") as file:
        for line in file:
            url = (
                line.strip()
            )  # strip()方法移除字符串开头和结尾的指定字符(默认是空白字符、空格、换行符、制表符等)
            response = requests.get(url)
            if response.status_code == 200:
                image_name = str(uuid.uuid4()).replace("-", "") + ".webp"
                save_path = os.path.join(output_dir, image_name)
                with open(save_path, "wb") as f:
                    f.write(response.content)  # response.content 是 requests 库中的一个属性,它包含了服务器返回的原始响应数据.对于图片资源,response.content 包含的是图片的二进制数据.
                print(f"已下载图片:{save_path}")
            else:
                print(f"无法下载图片:{url}")

    # shutil.rmtree(output_dir)


if __name__ == "__main__":
    ...
    # clean_dir(".idea")
    # rm_rf(".pytest")
    # delete_file("", ".log")

    # line_count, file_size = count_lines_and_size(os.path.abspath(__file__))
    # print(f"Line count: {line_count}")
    # print(f"File size: {file_size} KB")

    # 批量去除文件名中的特殊字符
    # directory_path = "../config/pic"
    # rename_files_in_directory(directory_path)

    # 排除的文件列表
    # exclude_files = []
    # directory = "/Users/wl/Downloads/Baldwin/gongju"
    # replace_punctuation_in_dir(directory, exclude_files)
    # replace_punctuation_in_file("/Users/wl/Downloads/Baldwin/gongju/webRequest.py")

    # for i in (var := find_file01(Path.cwd().parent, "*.py")): print(i)
    # find_file02("__init__.py", "/Users/wl/Downloads")

    # download_images_from_file("../config/url.txt", "../config/pic")