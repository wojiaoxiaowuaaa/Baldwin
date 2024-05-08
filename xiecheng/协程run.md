###### _**事件循环**_
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
    # gather用于并发地执行多个异步任务，并将它们的结果收集起来。它可以接受多个协程或任务作为参数，并按照添加的顺序返回结果。
    await asyncio.gather(*tasks)


# 运行主协程(run() 函数会自动创建一个事件循环并运行传入的协程。)这样做更加简洁，并且符合 Python 3.7 引入的 asyncio.run() 函数的使用方式。
asyncio.run(main())

print(f'总耗时：{time() - stat}')

```
###### _**核心概念**_
在异步编程中，"异步" 意味着在执行某些操作时，不会等待该操作完成而是继续执行后续的代码。这是与传统的同步编程（同步指的是按顺序执行，一个操作完成后再执行下一个操作）相对立的概念。

异步编程的目标是通过在执行长时间运行的操作（如 I/O 操作或网络请求）时释放 CPU，以提高程序的性能和并发性。

在 Python 中，异步编程通常涉及到 `asyncio` 模块和 `async/await` 关键字。以下是一些关键概念：

1. **协程（Coroutines）：** 异步编程中的基本单元是协程。协程是一种可以在执行过程中暂停并允许其他协程执行的特殊函数。在 Python 中，使用 `async def` 声明一个协程函数。

   ```python
   async def my_coroutine():
       print("Start")
       await asyncio.sleep(2)
       print("End")
   ```

2. **`await` 关键字：** 在协程中，使用 `await` 关键字等待一个异步操作的完成，例如等待 I/O 操作或另一个协程。

   ```python
   async def main():
       print("Before")
       await my_coroutine()
       print("After")
   ```

3. **事件循环（Event Loop）：** 异步编程中，事件循环负责调度和执行协程。`asyncio` 提供了一个事件循环，它负责在程序执行过程中管理协程的执行。

   ```python
   import asyncio

   async def main():
       print("Before")
       await my_coroutine()
       print("After")

   asyncio.run(main())
   ```
###### _**异步任务**_
异步编程允许在执行 I/O 操作时释放 CPU，以便执行其他任务，而不是等待 I/O 操作完成。这提高了程序的并发性和性能，
特别是在需要处理大量并发操作的情况下，如网络服务、Web 开发和大规模数据处理等。

在 asyncio 中，`asyncio.create_task` 是一个用来创建一个异步任务（Task）的函数。异步任务通常用于并发执行一些耗时的异步操作，比如IO操作或者其他需要等待的操作。

`asyncio.create_task` 函数介绍：

- **作用**：创建一个异步任务，将一个协程对象或一个Future对象包装为一个任务对象，可以通过 `await` 来等待任务的执行结果。

- **参数**：接受一个协程对象或一个Future对象作为参数。

- **返回值**：返回一个Task对象，表示一个异步任务。


```python
import asyncio


async def say_hello():
    await asyncio.sleep(1)
    return 'Hello'


async def say_world():
    await asyncio.sleep(1)
    return 'World'


async def main():
    task1 = asyncio.create_task(say_hello())  # 创建一个任务对象
    task2 = asyncio.create_task(say_world())  # 创建另一个任务对象
    print(await task1)  # 等待任务1完成
    print(await task2)  # 如果不使用 await 那么这里打印出的是协程对象而不是执行结果。


asyncio.run(main())

```
在 `main` 函数中，通过 `asyncio.create_task` 函数分别创建了这两个协程函数的任务对象 `task1` 和 `task2`。然后使用 `await` 关键字等待这两个任务的执行结果。
使用 `asyncio.create_task` 函数可以方便地创建异步任务，使得在异步编程中能够更加方便地并发执行多个异步操作。

###### _**异步编程**_
在Python中，`async` 关键字用于定义一个异步函数（也称为协程）。异步函数是使用`asyncio`库的一部分，它允许你编写单线程并发代码，这种代码可以在等待IO操作（如网络请求、文件读写等）完成时执行其他任务。

异步函数的基本语法如下：

```python
async def my_async_function():
    # 异步操作
    await some_async_operation()
```

这里的 `async` 关键字告诉Python这个函数是异步的，而 `await` 关键字用于等待一个异步操作完成。当你在异步函数中使用 `await` 时，它会暂停当前函数的执行，直到等待的异步操作完成。在此期间，事件循环可以继续执行其他任务。

异步编程的一个关键概念是事件循环（event loop），它是异步IO的核心。事件循环负责调度和管理所有的异步任务，并在后台运行，允许你的程序在等待一个操作完成时继续执行其他代码。

要运行异步函数，你需要一个运行在事件循环上的异步环境。这通常是通过调用 `asyncio.run()` 函数来实现的，它接受一个异步函数作为参数，并启动事件循环来运行它。

下面是一个简单的例子，展示了如何定义和运行一个异步函数：

```python
import asyncio

async def main():
    print("Starting")
    await asyncio.sleep(1)  # 模拟IO操作
    print("Ending")

# 运行异步主函数
asyncio.run(main())
```

在这个例子中，`main()` 函数是一个异步函数，它使用 `asyncio.sleep()` 来模拟一个异步等待操作。`asyncio.run()` 启动了事件循环并运行了 `main()` 函数。程序会立即打印 "Starting"，然后等待1秒钟，最后打印 "Ending"。

异步编程是处理高并发场景的强大工具，特别是在需要频繁进行IO操作的网络应用或API服务中。通过使用 `async` 和 `await`，你可以编写出更高效、响应更快的代码。