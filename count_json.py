import os


def count_lines_and_size(json_file):
    line_count = 0
    file_size = os.path.getsize(json_file) / 1024  # 将文件大小转换为KB  默认的单位是字节

    with open(json_file, "r") as f:
        for _ in f:
            line_count += 1

    return line_count, file_size


# 示例用法
json_file_path = "/Users/wl/Desktop/mock/xuqiu_json/kswitch线上.json"
line_count, file_size = count_lines_and_size(json_file_path)

print(f"Line count: {line_count}")
print(f"File size: {file_size} KB")
