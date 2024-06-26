import hashlib
import os


def calculate_md5(file_path, block_size=1024):
    md5 = hashlib.md5()
    with open(file_path, 'rb') as file:  # 二进制模式意味着文件将以字节流的形式读取，而不是文本。
        for block in iter(lambda: file.read(block_size), b''):  # 创建一个迭代器，该迭代器会重复调用 lambda: file.read(block_size)，直到返回值为 b''（空字节串,即文件末尾)迭代器停止。
            md5.update(block)  # 这个方法会更新 MD5 对象的状态，考虑到了新的数据块。在整个文件读取过程中，这个方法会不断更新 MD5 对象，将所有的数据块一一加入计算。
    return md5.hexdigest()  # 获取 MD5 摘要的十六进制表示


md5_value = calculate_md5(os.path.abspath(__file__))
print(md5_value)
