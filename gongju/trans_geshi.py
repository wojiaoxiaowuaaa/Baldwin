import os
import re


def replace_punctuation_in_files(directory: str):
    """替换文件夹中的中文标点符号为英文格式"""
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

    for root, dirs, files in os.walk(directory):
        for file in files:
            # if file.endswith(".py"):
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            for chinese, english in punctuation_mapping.items():
                content = re.sub(chinese, english, content)

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)


directory = "/Users/wl/proxy_pool"
replace_punctuation_in_files(directory)
