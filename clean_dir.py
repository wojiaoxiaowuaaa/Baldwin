import os
import shutil
import subprocess


def clean_up(dir):
    """删除当前脚本下的指定目录
    :param dir: 当前脚本所在目录下 要删除的目录
    涉及的关键方法调用:shutil.rmtree()"""
    cache_directory = os.path.join(os.path.dirname(__file__), dir)
    try:
        if os.path.exists(cache_directory):
            # shutil 是 Python 标准库中的一个模块，提供了一些用于文件和目录操作的高级功能。它是 "shell utility" 的缩写，旨在提供类似于 shell 命令的功能。
            shutil.rmtree(cache_directory)
            print(f"Directory '{cache_directory}' deleted successfully.")
        else:
            print(f"Directory '{cache_directory}' does not exist.")
    except Exception as e:
        print(f"Error during clean up: {e}")


def rm_rf(pwd):
    # 使用 subprocess 模块来运行系统命令如subprocess.run(['ls'])也可以使用os.system('ls')
    subprocess.run(["rm", "-rf", pwd], check=True)


# clean_up('gongju/.pytest_cache')
rm_rf('')