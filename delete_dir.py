import os
import shutil
import logging

def clean_dir(dir_path: str) -> None:
    """
    清理指定目录，如果目录存在则删除，否则报告目录不存在。
    :param dir_path: 要清理的目录路径（相对于脚本所在目录）
    """
    # 设置日志
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    # 获取完整的目录路径
    full_path = os.path.abspath(os.path.join(os.path.dirname(__file__), dir_path))
    logging.info(f"Attempting to clean directory: {full_path}")
    if os.path.exists(full_path):
        try:
            shutil.rmtree(full_path)
            logging.info(f"Directory '{full_path}' deleted successfully.")
        except PermissionError:
            logging.error(f"Permission denied: Unable to delete '{full_path}'.")
        except Exception as e:
            logging.error(f"Error during clean up: {e}")
    else:
        logging.warning(f"Directory '{full_path}' does not exist.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        clean_dir(sys.argv[1])
    else:
        print("Usage: python clean_dir.py <directory_path>")
