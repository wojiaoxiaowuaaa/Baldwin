import asyncio
import aiohttp
import os

"""在计算机编程中，"异步" 是指一种编程模型，它允许程序在执行某些任务时不阻塞其他任务的执行。传统的同步编程模型是按照顺序逐步执行代码，
如果遇到一个耗时的操作，整个程序会被阻塞，直到该操作完成。相比之下，异步编程通过使用异步任务、事件循环等机制，能够在执行耗时操作时让程序继续执行其他任务。
在 Python 中，使用 `asyncio` 库可以实现异步编程。以下是一些与异步相关的基本概念：
1. **协程（Coroutine）：** 
协程是异步编程中的一种结构，可以看作是比线程更轻量级的执行单元。协程通过使用 `async` 和 `await` 关键字定义，能够在异步程序中暂停和恢复执行。
2. **事件循环（Event Loop）：** 
事件循环是异步编程中的一个核心概念，它管理和调度异步任务的执行。事件循环负责监听异步任务的状态，并在适当的时候执行、暂停或恢复它们的执行。
3. **异步函数（Async Function）：** 
异步函数是使用 `async def` 声明的函数，它可以包含 `await` 关键字，用于等待异步任务的完成。
4. **异步任务（Async Task）：** 
异步任务是由异步函数创建的对象，它代表一个可以异步执行的操作。在事件循环中，异步任务可以被调度并并行执行。

在上面提供的下载脚本中，`asyncio` 和 `aiohttp` 库的结合实现了异步编程的功能。通过异步编程，脚本能够同时发起多个网络请求，而不必等待每个请求的完成，
从而提高了程序的性能和效率。在异步编程中，任务的执行可以在遇到 I/O 操作（如网络请求）时暂停，继续执行其他任务，待 I/O 操作完成后再恢复执行。
这种非阻塞的特性使得程序更灵活、高效地处理并发任务。"""


async def download_and_save(url, session):
    async with session.get(url) as response:
        if response.status == 200:
            content = await response.read()
            # 从 URL 中提取文件名
            filename = url.split("/")[-1].split("?")[0]
            # 拼接得到文件的绝对路径
            filename = os.path.join('/Users/wl/Desktop', filename)
            # 将内容保存到本地文件
            with open(filename, "wb") as f:
                f.write(content)
            print(f"Downloaded and saved: {filename}")
        else:
            print(f"Failed to download {url}. Status code: {response.status}")


async def main():
    urls = []
    # 读取文件中的 URL 添加到列表中
    with open("/Users/wl/Desktop/Baldwin/doc/doc.txt", 'r') as f:
        for i in f:
            urls.append(i.strip())

    async with aiohttp.ClientSession() as session:
        tasks = [download_and_save(url, session) for url in urls]
        await asyncio.gather(*tasks)


asyncio.run(main())
