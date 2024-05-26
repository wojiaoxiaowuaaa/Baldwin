import os.path
import time
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

"""
# 协程（Coroutine):协程是一种轻量级的并发模型，它可以在单线程中实现并发执行多个任务。
# 使用协程可以避免阻塞主线程的执行，并能够提高程序的性能和可维护性.

import asyncio
import os.path


async def read_file_async(filename):
    # 模拟异步读取文件的操作
    # read_file_async 函数是一个协程函数，它通过关键字 await 来防止阻塞主线程的执行，并在异步操作完成后返回结果或抛出异常。
    # main 函数也是一个协程函数，它使用关键字 await 来等待并运行 read_file_async 函数，来处理文件读取操作的结果。
    await asyncio.sleep(1)
    with open(filename, "r+") as f:
        data = f.read()
    if data:
        return data  # 异步操作成功，返回结果
    else:
        raise Exception("读取文件失败")  # 异步操作失败，抛出异常


# 使用协程进行文件读取操作，并获取结果
async def main():
    try:
        data = await read_file_async(os.path.abspath(__file__))
        print(f"文件内容：{data}")
    except Exception as e:
        print(f"发生错误：{e}")


asyncio.run(main())




"""