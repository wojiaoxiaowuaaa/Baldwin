import os
import unittest
from dir_file import count_lines_and_size


class TestCountLinesAndSize(unittest.TestCase):
    """单元测试示例.测试count_lines_and_size函数.执行需要重命名文件将开头的demo改为test"""
    def setUp(self):
        self.test_file = "aaa.json"
        with open(self.test_file, "w") as f:
            f.write('{"name": "是小舞不是小武"}\n' * 10)

    def tearDown(self):
        try:
            os.remove(self.test_file)  # 测试结束后删除测试文件
        except Exception as e:
            print(e)

    def test_count_lines_and_size(self):
        line_count, file_size = count_lines_and_size(self.test_file)
        self.assertEqual(10, line_count)  # 我们写入了10行,所以期望行数为10
        self.assertTrue(file_size > 0.3)  # 文件大小应该大于0


if __name__ == "__main__":
    # python3 test_count_file.py 终端运行测试用例
    unittest.main()


"""
import os
import sys
import pytest
# if (BASE_PATH := os.path.dirname(os.path.abspath(__file__))) not in sys.path: sys.path.insert(0, BASE_PATH)
# from gongju.dir_file import count_lines_and_size
from count_file import count_lines_and_size


@pytest.fixture(scope="module")
def temp_json_file():
    test_file = 'test.json'
    with open(test_file, 'w') as f:
        f.write('\n'.join(['{"key": "value"}' for _ in range(3)]))  # 3行内容
    yield test_file
    os.remove(test_file)


def test_count_lines_and_size(temp_json_file):
    line_count, size_kb = count_lines_and_size(temp_json_file)

    assert line_count == 3, "行数计算不正确"
    expected_size_kb = os.path.getsize(temp_json_file) / 1024
    assert pytest.approx(size_kb, abs=0.001) == expected_size_kb, "文件大小计算不准确"

# 在命令行中执行  pytest -v test_count_file.py

"""
