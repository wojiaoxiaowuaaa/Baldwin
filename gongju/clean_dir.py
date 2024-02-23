import os
import shutil


def clean_up(dir):
    """删除当前脚本下的指定目录
    :param dir: 当前脚本所在目录下要删除的目录
    方法调用:shutil.rmtree()"""
    cache_directory = os.path.join(os.path.dirname(__file__), dir)
    try:
        if os.path.exists(cache_directory):
            shutil.rmtree(cache_directory)
            print(f"Directory '{cache_directory}' deleted successfully.")
        else:
            print(f"Directory '{cache_directory}' does not exist.")
    except Exception as e:
        print(f"Error during clean up: {e}")


clean_up('.pytest_cache')
