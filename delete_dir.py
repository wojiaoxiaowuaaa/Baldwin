import os
import shutil
from typing import Optional
from log_util import logger
import logging

# 初始化配置（程序入口调用一次）
# logger.initialize(level=logging.DEBUG, log_file="app.log")


def clean_dir(dir_path: str) -> None:
    """
    设置日志配置并清理指定目录，如果目录存在则删除，否则报告目录不存在。
    :param dir_path: 要清理的目录的绝对路径
    """
    # 设置日志配置
    # logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s  - [%(filename)s:%(lineno)d]')

    logger.info(f"Attempting to clean directory: {dir_path}")

    if os.path.exists(dir_path):
        try:
            shutil.rmtree(dir_path)
            logger.info(f"Directory '{dir_path}' deleted successfully.")
        except PermissionError:
            logger.error(f"Permission denied: Unable to delete '{dir_path}'.")
        except Exception as e:
            logger.error(f"Error during clean up: {e}")
    else:
        logger.warning(f"Directory '{dir_path}' does not exist.")


def main(args: Optional[list[str]] = None) -> None:
    import sys
    if args is None:
        args = sys.argv[1:]

    if args:
        abs_path = os.path.abspath(args[0])
        clean_dir(abs_path)
    else:
        logger.error("Usage: python clean_dir.py <absolute_directory_path>")


if __name__ == "__main__":
    main()



# def clean_dir(dir_path: str) -> None:
#     """
#     清理指定目录，如果目录存在则删除，否则报告目录不存在。
#     :param dir_path: 要清理的目录路径（相对于脚本所在目录）
#     """
#     # 设置日志
#     logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#     # 获取完整的目录路径
#     full_path = os.path.abspath(os.path.join(os.path.dirname(__file__), dir_path))
#     logging.info(f"Attempting to clean directory: {full_path}")
#     if os.path.exists(full_path):
#         try:
#             shutil.rmtree(full_path)
#             logging.info(f"Directory '{full_path}' deleted successfully.")
#         except PermissionError:
#             logging.error(f"Permission denied: Unable to delete '{full_path}'.")
#         except Exception as e:
#             logging.error(f"Error during clean up: {e}")
#     else:
#         logging.warning(f"Directory '{full_path}' does not exist.")

