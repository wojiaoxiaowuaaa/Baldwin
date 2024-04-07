`asyncio.run()` 是 Python 3.7 中引入的一个函数，用于运行最高层级的协程，并管理事件循环的创建和关闭。它的主要作用是简化了 asyncio 应用程序的启动和结束过程，使得编写异步代码变得更加方便。

以下是 `asyncio.run()` 函数的一些重要特点和用法：

1. **运行最高层级的协程**：`asyncio.run()` 函数接受一个协程对象作为参数，并在运行时执行这个协程。这个协程通常是整个 asyncio 应用程序的入口点，称为主协程（main coroutine）。

2. **创建和管理事件循环**：`asyncio.run()` 函数会在内部自动创建一个事件循环（Event Loop），并在协程执行完成后关闭这个事件循环。这样就不需要显式地创建和管理事件循环对象了。

3. **阻止主程序**：在运行 `asyncio.run()` 函数时，它会阻止主程序的执行，直到主协程执行完成并事件循环关闭为止。这样可以确保主协程的执行顺序和事件循环的正确管理。

4. **异常处理**：`asyncio.run()` 函数会捕获主协程中的异常，并将其打印到标准错误输出。这样可以方便地查看和调试异步代码中的异常情况。

5. **用法简单**：由于 `asyncio.run()` 函数封装了事件循环的创建和关闭过程，因此使用起来非常简单，只需要传入一个协程对象即可。

基本用法示例如下：

```python
import asyncio

async def main():
    # 主协程的逻辑
    await asyncio.sleep(1)
    print("Hello, asyncio!")

asyncio.run(main())
```

在上面这个示例中，我们定义了一个简单的主协程 `main()`，它会等待 1 秒钟后打印 "Hello, asyncio!"。然后使用 `asyncio.run(main())` 来运行主协程，`asyncio.run()` 函数会自动创建和管理事件循环，并在主协程执行完成后关闭事件循环。



```python
import asyncio
from loguru import logger
from time import time
stat = time()


# 定义一个异步函数，模拟一个耗时的IO操作
async def do_io_operation(task_name, delay):
    logger.info(f'{task_name} 开始执行')
    await asyncio.sleep(delay)
    logger.info(f'{task_name} 执行完成')


# 定义一个协程函数，用于启动多个异步IO操作
async def main():
    # 显示的创建一个事件循环对象(不推荐)
    # loop = asyncio.get_event_loop()

    # 创建一个任务队列，用于存放要执行的异步IO操作
    tasks = [
        do_io_operation('任务1', 2),
        do_io_operation('任务2', 1),
        do_io_operation('任务3', 3)
    ]

    # 将任务队列中的任务添加到事件循环中执行
    await asyncio.gather(*tasks)


# 运行主协程(run() 函数会自动创建一个事件循环并运行传入的协程。)这样做更加简洁，并且符合 Python 3.7 引入的 asyncio.run() 函数的使用方式。
asyncio.run(main())

print(f'总耗时：{time() - stat}')
