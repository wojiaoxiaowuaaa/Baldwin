import os
import sys


# sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def count_lines_and_size(json_file):
    count = 0
    size = os.path.getsize(json_file) / 1024  # 将文件大小转换为KB  默认的单位是字节

    with open(json_file, "r") as f:
        for _ in f:  # 循环结构会逐行读取文件 json_file 的内容.可使用 _.strip() 去掉每行末尾的换行符.
            count += 1

    return count, size


line_count, file_size = count_lines_and_size(os.path.abspath(__file__))
print(f"Line count: {line_count}")
print(f"File size: {file_size} KB")
