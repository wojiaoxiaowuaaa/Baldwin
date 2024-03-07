import os
from loguru import logger
from config.setting import desktop

# def get_folder_size(floder='.'):
#     total_size = 0
#
#     for root, dir, filenames in os.walk(floder):
#         for filename in filenames:
#             file_path = os.path.join(root, filename)
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
folder_size = sum([os.path.getsize(os.path.join(root, filename)) for root, dir, filenames in os.walk(desktop) for filename in filenames])

logger.info(folder_size / 1024 / 1024 / 1024)  # 默认单位是B-字节,这里除以三次1024换算到GB
