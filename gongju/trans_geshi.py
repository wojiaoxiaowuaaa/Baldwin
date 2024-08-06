import os
import re
import sys


def replace_punctuation_in_files(directory: str, exclude_files: list):
    """替换文件夹中的中文标点符号为英文格式 排除指定的文件不做替换"""
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

    # 获取当前脚本的绝对路径
    current_script = os.path.abspath(sys.argv[0])

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # 检查文件是否在排除列表中，或者是否是当前脚本文件
            if file_path in exclude_files or file_path == current_script:
                continue  # 跳过排除的文件

            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            for chinese, english in punctuation_mapping.items():
                content = re.sub(chinese, english, content)

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)


# 排除的文件列表
exclude_files = []
directory = "/Users/wl/Downloads/Baldwin/gongju"
replace_punctuation_in_files(directory, exclude_files)
