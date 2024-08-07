import os
import shutil
import subprocess


def clean_up(dir):
    """删除当前脚本下的指定目录
    :param dir: 当前脚本所在目录下待删除的目录"""
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
    #  使用subprocess模块来运行系统命令如subprocess.run(['ls'])也可以使用os.system('echo $PATH')--这种方式更简洁轻便但是不具备复杂情况的处理能力
    subprocess.run(["rm", "-rf", pwd], check=True)


if __name__ == "__main__":
    clean_up(".idea")
    rm_rf(".pytest")

"""
import os
import tempfile
import unittest
from clean_dir import clean_up
from loguru import logger

# 针对clean_up函数编写单测
class TestCleanUp(unittest.TestCase):
    def setUp(self):
        # 创建一个临时目录
        self.test_dir = tempfile.mkdtemp()
        logger.info(self.test_dir)

    def tearDown(self):
        # 测试完成后清理临时目录
        if os.path.exists(self.test_dir):
            os.rmdir(self.test_dir)
            logger.info(os.path.exists(self.test_dir))

    def test_clean_up_existing_directory(self):
        # 测试删除存在的目录
        dir_name = os.path.join(self.test_dir, 'test_subdir')
        os.mkdir(dir_name)
        self.assertTrue(os.path.exists(dir_name))
        clean_up(dir_name)
        self.assertFalse(os.path.exists(dir_name))

    def test_clean_up_non_existing_directory(self):
        # 测试尝试删除不存在的目录
        dir_name = os.path.join(self.test_dir, 'non_existing_dir')
        self.assertFalse(os.path.exists(dir_name))
        clean_up(dir_name)  # 不应该抛出异常
        self.assertFalse(os.path.exists(dir_name))  # 确认目录仍然不存在


if __name__ == '__main__':
    unittest.main()

"""
