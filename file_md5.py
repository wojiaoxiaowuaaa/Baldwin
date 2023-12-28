import hashlib
import os


def calculate_md5(file_path, block_size=1024):
    md5 = hashlib.md5()
    with open(file_path, 'rb') as file:
        for block in iter(lambda: file.read(block_size), b''):
            md5.update(block)  # 这个方法会更新 MD5 对象的状态，考虑到了新的数据块。在整个文件读取过程中，这个方法会不断更新 MD5 对象，将所有的数据块一一加入计算。
    return md5.hexdigest()


md5_value = calculate_md5(os.path.abspath(__file__))
print(md5_value)