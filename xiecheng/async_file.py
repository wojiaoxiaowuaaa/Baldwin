import asyncio
import aiofiles
import os


async def read_file(filename):
    async with aiofiles.open(filename, mode='r', encoding='utf-8') as f:
        contents = await f.read()
        return contents


async def read_all_files_in_directory():
    files = os.listdir('.')  # 获取当前文件夹下的所有文件名&目录名
    tasks = [read_file(file) for file in files if os.path.isfile(file)]  # 创建一个任务列表，每个任务都是异步读取一个文件的操作
    results = await asyncio.gather(*tasks)  # 并行执行所有异步读取文件的任务
    # logger.info(results)
    return results


async def main():
    files_content = await read_all_files_in_directory()
    for file, content in zip(os.listdir('.'), files_content):
        print(f"File: {file}, Content: {content}")


if __name__ == "__main__":
    asyncio.run(main())
