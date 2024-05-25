import asyncio
import aiofiles
import os
from loguru import logger


async def read_file(filename):
    async with aiofiles.open(filename, mode='r') as f:
        contents = await f.read()
        return filename, contents


async def read_all_files_in_directory():
    files = os.listdir('.')  # 获取文件夹下的所有文件名&目录名
    tasks = [read_file(file) for file in files if os.path.isfile(file)]  # 创建一个任务列表，每个任务都是异步读取一个文件的操作
    result = await asyncio.gather(*tasks)  # 并行 执行所有异步读取文件的任务
    return result


async def main():
    # 这里的result是列表  列表中元素为read_file任务中返回的元祖
    result = await read_all_files_in_directory()
    # 如果要在协程中迭代一个可迭代对象（如列表、元组等），可以直接使用for循环。协程会自动处理迭代过程中的异步操作。
    # for i in result:
    #     logger.info(f"文件名:{i[0]}  文件内容:\n{i[1]}")
    # for k, v in dict(result).items():
    #     logger.info(f"文件名:{k}  文件内容:\n{v}")
    for i in dict(result):
        logger.info(f"文件名:{i}  文件内容:\n{dict(result)[i]}")


if __name__ == "__main__":
    asyncio.run(main())
