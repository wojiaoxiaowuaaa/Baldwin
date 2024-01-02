# 协程（Coroutine）： 协程是一种轻量级的并发模型，它可以在单线程中实现并发执行多个任务。使用协程可以避免阻塞主线程的执# 行，并能够提高程序的性能和可维护性。以下是一个使用协程处理异步操作的示例：

import asyncio
import os.path


async def read_file_async(filename):
    # 模拟异步读取文件的操作
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


# 运行协程函数
asyncio.run(main())


# 在上述示例中，read_file_async 函数是一个协程函数，它通过关键字 await 来防止阻塞主线程的执行，并在异步操作完成后返回结果或抛出异常。
# main 函数也是一个协程函数，它使用关键字 await 来等待并运行 read_file_async 函数，来处理文件读取操作的结果。
