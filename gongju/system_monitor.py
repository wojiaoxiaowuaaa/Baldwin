"""在 asyncio 中,协程函数通常是通过 async def 关键字定义的,而在调用协程函数时,需要使用 await 关键字来等待协程的执行结果.
如果不使用 await,则会得到协程对象本身而不是执行结果.在下面的脚本中,asyncio.create_task 创建了两个协程任务,并且使用 await 关键字来等待
它们的执行结果,然后打印出来.如果不使用await那么print(await memory)和print(await cpu) 语句就会直接打印出协程对象而不是执行结果"""
import asyncio
import time
import psutil
from loguru import logger


class SystemMonitor:
    """监控系统资源使用情况脚本 :param interval: 采样间隔, 秒"""

    def __init__(self, interval=3):
        self.interval = interval

    async def get_memory_usage(self):
        memory = psutil.virtual_memory()
        return f"Memory Usage: {memory.percent}%"

    async def get_cpu_usage(self):
        cpu = psutil.cpu_percent(interval=1)
        return f"CPU Usage: {cpu}%"

    async def monitor(self, duration=30):
        start = time.time()
        try:
            while time.time() - start < duration:
                memory_task = asyncio.create_task(self.get_memory_usage())
                cpu_task = asyncio.create_task(self.get_cpu_usage())
                # await 关键字会等待异步任务执行完成,因此程序会暂停执行,直到这两个任务执行完毕并返回结果.
                logger.info(await memory_task)
                logger.info(await cpu_task)
                await asyncio.sleep(self.interval)
        except KeyboardInterrupt:
            print("Monitoring stopped.")


if __name__ == "__main__":
    monitor = SystemMonitor()
    asyncio.run(monitor.monitor())
