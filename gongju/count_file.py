import os
import sys


# sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def count_lines_and_size(json_file):
    line_count = 0
    file_size = os.path.getsize(json_file) / 1024  # 将文件大小转换为KB  默认的单位是字节

    with open(json_file, "r") as f:
        for _ in f:
            line_count += 1

    return line_count, file_size


# file:待计算的文件路径
file = os.path.abspath(__file__)
line_count, file_size = count_lines_and_size(file)

print(f"Line count: {line_count}")
print(f"File size: {file_size} KB")
