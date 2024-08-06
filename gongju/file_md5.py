import hashlib
import os
from config.setting import MD5_SALT


def calculate_md5(file_path, block_size=1024):
    md5 = hashlib.md5()
    with open(
        file_path, "rb"
    ) as file:  # 二进制模式意味着文件将以字节流的形式读取,而不是文本.
        for block in iter(
            lambda: file.read(block_size), b""
        ):  # 创建一个迭代器,该迭代器会重复调用 lambda: file.read(block_size),直到返回值为 b''(空字节串,即文件末尾)迭代器停止.
            md5.update(
                block
            )  # 这个方法会更新 MD5 对象的状态,考虑到了新的数据块.在整个文件读取过程中,这个方法会不断更新 MD5 对象,将所有的数据块一一加入计算.
    return md5.hexdigest()  # 获取 MD5 摘要的十六进制表示


def get_md5(username, str):
    """MD5加密处理"""
    str = username + str + MD5_SALT  # 把用户名也作为str加密的一部分
    md5 = hashlib.md5()  # 创建md5对象
    md5.update(str.encode("utf-8"))  # Python3中需要先转换为 bytes 类型,才能加密
    return (
        md5.hexdigest()
    )  # 计算输入数据的 MD5 哈希值,并将其以十六进制字符串的形式返回.


def video_md5(pwd):
    """获取视频的md5值 节约内存型"""
    md5_hash = hashlib.md5()
    with open(pwd, "rb") as f:
        while chunk := f.read(4096):
            md5_hash.update(chunk)
    print(md5_hash.hexdigest())


def md5_video(pwd):
    """获取视频的md5 快速型(一次性加载全部数据到内存)
    Python的内存管理是基于引用计数和垃圾回收的,一次性读取大文件可能会导致整个文件的内容都存储在内存中,占用大量的内存空间.如果文件过大,超出了系统的可用内存限制,就会导致内存溢出
    """
    with open(pwd, "rb") as f:
        md5 = hashlib.md5(f.read()).hexdigest()
    print(md5)


md5_value = calculate_md5(os.path.abspath(__file__))
print(md5_value)
