import subprocess
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import unittest
from count_file import count_lines_and_size


class TestCountLinesAndSize(unittest.TestCase):
    def setUp(self):
        self.test_file = "test.json"
        with open(self.test_file, "w") as f:
            f.write('{"name": "是小舞不是小武"}\n' * 10)

    def tearDown(self):
        try:
            os.remove(self.test_file)  # 测试结束后删除测试文件
        except Exception as e:
            print(e)

    def test_count_lines_and_size(self):
        line_count, file_size = count_lines_and_size(self.test_file)
        self.assertEqual(10, line_count)  # 我们写入了10行，所以期望行数为10
        self.assertTrue(file_size > 0)  # 文件大小应该大于0


if __name__ == "__main__":
    unittest.main()
