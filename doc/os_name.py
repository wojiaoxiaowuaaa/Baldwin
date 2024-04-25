import os
import re


def rename_files(path):
    # 批量修改文件名去除特殊字符
    for file_name in os.listdir(path):
        if os.path.isfile(os.path.join(path, file_name)):
            name_parts = re.findall(r"[a-zA-Z0-9.]+", file_name)
            new_name = "".join(name_parts)
            os.rename(os.path.join(path, file_name), os.path.join(path, new_name))

            print(f"Renamed {file_name} ------>  {new_name}")


# 指定要修改文件名的文件夹路径
rename_files("/Users/wl/Documents/douyin_download")

"""
def add_webp_extension(folder_path):
    for file in os.listdir(folder_path):
        # 获取文件的绝对路径
        file_path = os.path.join(folder_path, file)

        # 判断是否为文件
        if os.path.isfile(file_path):
            # 如果文件名中不包含.webp后缀，则添加后缀
            if not file.endswith(".webp"):
                new_file_name = file + ".webp"
                new_file_path = os.path.join(folder_path, new_file_name)

                # 重命名文件
                os.rename(file_path, new_file_path)
                print(f"Renamed file: {file} to {new_file_name}")


# 当前文件夹路径
folder_path = '/Users/wl/Documents/douyin_download'

add_webp_extension(folder_path)

"""
