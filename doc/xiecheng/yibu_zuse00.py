import os
import asyncio
from loguru import logger


async def read_file_async(filename, callback):
    """模拟异步读取文件的操作.read_file_async 函数模拟了一个异步的文件读取操作。它接受一个文件名和一个回调函数作为参数,
    并在异步操作完成后调用回调函数来处理结果或错误。on_file_read_complete作为回调函数，用于处理异步操作的结果。
    通过这种方式，可以在异步操作完成后获取结果或处理错误，而不会阻塞主线程的执行"""
    await asyncio.sleep(1)
    with open(filename, "r") as f:
        data = f.read()
    if data:
        callback(None, data)  # 异步操作成功，调用回调函数传递结果
    else:
        callback(Exception("读取文件失败"))  # 异步操作失败，调用回调函数传递错误


def on_file_read_complete(error, data):
    # 回调函数用于处理异步操作的结果
    if error:
        print(f"发生错误：{error}")
    else:
        logger.info(f"文件内容：{data}")


# 使用代理函数进行文件读取操作
async def main():
    await read_file_async(os.path.abspath(__file__), on_file_read_complete)


asyncio.run(main())

