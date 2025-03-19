import os
import asyncio
import aiofiles
from loguru import logger


async def read_file_async(filename, callback):
    """callback回调函数,用于处理异步操作的结果.通过这种方式,可以在异步操作完成后获取结果或处理错误,而不会阻塞主线程的执行"""
    async with aiofiles.open(filename) as f:
        data = await f.read()
    if data:
        callback(None, data)  # 异步操作成功，调用回调函数传递结果
    else:
        callback(Exception("读取文件失败"))  # 异步操作失败，调用回调函数传递错误


def on_file_read_complete(error, data):
    # 回调函数用于处理异步操作的结果
    if error:
        logger.info(f"发生错误：{error}")
    else:
        logger.info(f"文件内容：{data}")


# 使用代理函数进行文件读取操作
async def main():
    await read_file_async(os.path.abspath(__file__), on_file_read_complete)


asyncio.run(main())
