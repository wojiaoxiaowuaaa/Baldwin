"""在asyncio.gather(*tasks)中,星号*是必要的,它用于解包序列(这里是tasks列表)并将其中的元素作为单独的参数传递给asyncio.gather()函数.asyncio.gather()函数接受一个或多个awaitable对象(如Future或Coroutine)作为参数,并等待它们全部完成.
为什么需要*,如果不使用星号*,asyncio.gather()将接收到整个tasks列表作为一个单一参数,而不是列表中的各个任务.asyncio.gather()函数并不接受一个包含任务的列表作为单个参数,而是需要各个任务作为独立的参数输入.因此,*的作用是将列表解包,使asyncio.gather()能够正确识别并等待列表中的每一个任务.
示例: 假设tasks = [task1, task2, task3],那么:asyncio.gather(*tasks)相当于asyncio.gather(task1, task2, task3),这是正确的用法.
如果写成asyncio.gather(tasks),那么实际上是在调用asyncio.gather([task1, task2, task3]),这会导致TypeError,因为asyncio.gather()期望的是多个awaitable对象,而不是一个包含这些对象的列表.
因此,在使用asyncio.gather()时,使用星号*来解包任务列表是非常重要的,它确保了每个任务都能被正确地识别和等待"""
from loguru import logger
import asyncio
import aiofiles
import os


async def read_file(filename):
    """读取文件 并返回文件名和文件内容"""
    async with aiofiles.open(filename, mode="r") as f:
        contents = await f.read()
        return filename, contents


async def read_all_files_in_directory():
    """异步读取目录下的所有文件"""
    files = os.listdir(".")
    tasks = [read_file(file) for file in files if os.path.isfile(file)]  # 任务列表 每个任务都是异步读取一个文件内容的操作
    result = await asyncio.gather(*tasks)  # 并行执行所有异步读取文件的任务 *用于拆包
    return result


async def main():
    # 这里的result是列表  列表中元素为read_file任务中返回的元祖
    result = await read_all_files_in_directory()
    # 如果要在协程中迭代一个可迭代对象(如列表、元组等),可以直接使用for循环.协程会自动处理迭代过程中的异步操作.
    # 内置函数 dict 的构造函数能够接受一个元素为元组(tuple)的列表作为参数,并将每个元组的第一个元素作为键(key),第二个元素作为值(value),创建一个新的字典.
    for i in dict(result):
        logger.info(f"\n文件名:\n{i}  \n文件内容:\n{dict(result)[i]}")


if __name__ == "__main__":
    asyncio.run(main())


