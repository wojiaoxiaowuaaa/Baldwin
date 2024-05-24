import os
import re

import os
import re


def clean_filename(filename):
    # 使用正则表达式去除特殊字符，保留字母、数字、下划线和点
    return re.sub(r'[^a-zA-Z0-9_.]', '', filename)


def rename_files_in_directory(directory):
    # 获取指定目录下的所有文件和文件夹
    for filename in os.listdir(directory):
        # 获取文件的完整路径
        full_path = os.path.join(directory, filename)

        # 如果是文件而不是文件夹
        if os.path.isfile(full_path):
            # 清理文件名
            clean_name = clean_filename(filename)

            # 获取新的完整路径
            new_full_path = os.path.join(directory, clean_name)

            # 重命名文件
            os.rename(full_path, new_full_path)
            print(f'Renamed: {filename} -> {clean_name}')


# 使用示例
directory_path = '../config/pic'
rename_files_in_directory(directory_path)

"""
def add_webp_extension(folder_path):
    for file in os.listdir(folder_path):
        # 获取文件的绝对路径
        file_path = os.path.join(folder_path, file)

        # 判断是否为文件
        if os.path.isfile(file_path):
            # 如果文件名中不包含.webp后缀，则添加后缀
            if not file.endswith("1--11.webp"):
                new_file_name = file + "1--11.webp"
                new_file_path = os.
                path.join(folder_path, new_file_name)
                # 重命名文件
                os.rename(file_path, new_file_path)
                print(f"Renamed file: {file} to {new_file_name}")


# 当前文件夹路径
folder_path = '/Users/wl/Documents/douyin_download'

add_webp_extension(folder_path)

"""
