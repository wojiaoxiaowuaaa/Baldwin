import os
import sys


def count_lines_and_size(json_file):
    """统计制定文件的行数与存储空间占用"""
    count = 0
    size = os.path.getsize(json_file) / 1024  # 将文件大小转换为KB  默认的单位是字节

    with open(json_file, "r") as f:
        for _ in f:
            count += 1  # 循环结构会逐行读取文件 json_file 的内容.可使用 _.strip() 去掉每行末尾的换行符.

    return count, size


# if __name__ == '__main__':
# line_count, file_size = count_lines_and_size(os.path.abspath(__file__))
# print(f"Line count: {line_count}")
# print(f"File size: {file_size} KB")
