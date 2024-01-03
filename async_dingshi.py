import asyncio

"""
在需要执行定时任务的应用中，可以使用异步操作来管理定时任务的执行。这样，你可以在单个线程中安排多个定时任务而不需要创建多个线程。
这个示例说明了在单个线程中使用异步操作的场景，其中 asyncio 是 Python 中用于支持异步编程的标准库。
异步操作可以提高程序的性能，特别是在需要处理大量 I/O 操作的情况下。
"""


async def task_one():
    print("Task One executed.")


async def task_two():
    print("Task Two executed." + '\n\n')


async def main():
    while True:
        await asyncio.gather(task_one(), task_two())
        await asyncio.sleep(5)  # Run tasks every 5 seconds


asyncio.run(main())
