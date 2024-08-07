"""生成器方法通常在内存使用方面更优,因为它逐块读取文件,不会一次性加载整个文件到内存中.
os.path.getsize() 方法会一次性加载整个文件到内存中,这可能会导致内存不足或性能下降,特别是对于大型文件而言.

在 Python 中,bytes 类型是一种用于表示二进制数据的类型.它类似于字符串,但与字符串不同的是,bytes 类型可以包含任意字节的数据.
len() 函数用于获取一个对象的长度.当将一个 bytes 类型的对象传递给 len() 函数时,它会返回该 bytes 对象中字节的数量.
需要注意的是,len() 函数对于 bytes 对象的计算是基于字节数的,而不是字符数.每个字节都被视为一个独立的单位.
二进制文件也可以被看作是一个可迭代对象(iterable),其包含了一系列的字节(bytes)"""

import os
from time_count import calculate_execution_time
from loguru import logger
from config.setting import pic


def read_file_in_chunks(file_path, chunk_size=4096):
    """使用生成器,每次读取一个 chunk_size 大小的数据块,直到读取完文件."""
    with open(file_path, "rb") as file:
        while True:
            data = file.read(chunk_size)
            if not data:
                break
            yield data


@calculate_execution_time
def calculate_file_size(file_path):
    """计算文件大小,单位为 MB"""
    total_size = 0
    for chunk in read_file_in_chunks(file_path):
        # 在Python中bytes 对象是一个不可变的字节序列,len() 函数用于计算字节串中的字节数,这种情况下,一个字节串中的长度就代表了文件中读取的数据量(以字节为单位).因此len(chunk) 返回的是字节串 chunk 中的字节数.
        total_size += len(chunk)
    return total_size / 1024 / 1024


if __name__ == "__main__":
    (
        logger.info(f"The size of the file '{pic}' is: {calculate_file_size(pic)} MB")
        if os.path.exists(pic)
        else logger.info("file does not exist")
    )

    # 计算指定文件夹的大小
    # folder_size = sum(
    #     [
    #         os.path.getsize(os.path.join(root, filename))
    #         for root, dir, filenames in os.walk("/Users/wl/Documents")
    #         for filename in filenames
    #     ]
    # )
    # logger.info(f"指定文件夹下的的文件大小总和是{folder_size / 1024 / 1024 / 1024} GB")
