import psutil
import time
import asyncio
from color_print import color_print_green


async def get_memory_usage():
    """获取内存使用率"""
    memory = psutil.virtual_memory()
    return f"Memory Usage: {memory.percent}%"


async def get_cpu_usage():
    """获取 CPU 使用率"""
    cpu = psutil.cpu_percent(interval=1)
    return f"CPU Usage: {cpu}%"


async def main():
    start = time.time()
    try:
        while time.time() - start < 30:
            memory = asyncio.create_task(get_memory_usage())
            cpu = asyncio.create_task(get_cpu_usage())
            # await 关键字会等待异步任务执行完成，因此程序会暂停执行，直到这两个任务执行完毕并返回结果。
            print(await memory)
            print(await cpu)
            color_print_green()
            await asyncio.sleep(3)  # 间隔时间，可以根据需要调整
    except KeyboardInterrupt:
        print('over')


if __name__ == '__main__':
    asyncio.run(main())


"""在 asyncio 中，协程函数通常是通过 async def 关键字定义的，而在调用协程函数时，需要使用 await 关键字来等待协程的执行结果。
如果不使用 await，则会得到协程对象本身而不是执行结果。
在上面的脚本中，asyncio.create_task 创建了两个协程任务，并且使用 await 关键字来等待它们的执行结果，然后打印出来。
如果不使用 await，那么 print(await memory) 和 print(await cpu) 语句就会直接打印出协程对象而不是执行结果。"""