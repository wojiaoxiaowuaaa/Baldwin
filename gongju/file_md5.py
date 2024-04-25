import hashlib
import os


def calculate_md5(file_path, block_size=1024):
    md5 = hashlib.md5()
    with open(file_path, 'rb') as file:
        for block in iter(lambda: file.read(block_size), b''):
            md5.update(block)  # 这个方法会更新 MD5 对象的状态，考虑到了新的数据块。在整个文件读取过程中，这个方法会不断更新 MD5 对象，将所有的数据块一一加入计算。
    return md5.hexdigest()  # 获取 MD5 摘要的十六进制表示


md5_value = calculate_md5(os.path.abspath(__file__))
print(md5_value)


"""
import os


def func(path):
    with open(path, 'r') as f:
    # 当使用 iter(lambda: f.read(1024), b'') 时，b'' 表示迭代器的终止条件是一个空的 bytes 对象。这意味着迭代器会一直尝试从文件中读取数据，直至发生异常被中断。
        for i in iter(lambda: f.read(1024), ''):
            print(i)


pwd = os.path.abspath(__file__)
func(pwd)

"""