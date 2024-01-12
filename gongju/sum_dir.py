import os

# def get_folder_size(floder='.'):
#     total_size = 0
#
#     for dirpath, dirnames, filenames in os.walk(floder):
#         for filename in filenames:
#             file_path = os.path.join(dirpath, filename)
#             total_size += os.path.getsize(file_path)
#
#     return total_size


# def format_size(size):
#     # 将字节数转换为更大单位的字符串表示
#     for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
#         if size < 1024.0:
#             return f"{size:.2f} {unit}"
#         size /= 1024.0
#
#
# if __name__ == "__main__":
#     floder = '/Users/wl/Documents/douyin'  # 替换为要计算大小的文件夹路径
#     total_size = get_folder_size(floder)
#     formatted_size = format_size(total_size)
#     print(f"The total size of the folder {floder} is: {formatted_size}")

# 计算指定文件夹的大小
floder = '/Users/wl/Documents/douyin'

folder_size = sum([os.path.getsize(os.path.join(dirpath, filename)) for dirpath, dirnames, filenames in os.walk(floder) for filename in filenames])

print(folder_size / 1024 / 1024 / 1024, 'GB')  # 默认单位是B-字节,这里除以三次1024换算到GB
