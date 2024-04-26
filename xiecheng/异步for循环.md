## 示例一
在Python中，异步`for`循环通常用于异步迭代器或异步可迭代对象。它与普通的`for`循环类似，但是可以在异步上下文中使用，允许在异步任务中逐个处理元素，而不会阻塞事件循环。

异步`for`循环通常与`async for`语法一起使用，语法结构为：

```python
async for target in async_iterable:
    # 异步处理逻辑
```

其中：
- `async for`关键字表示这是一个异步的`for`循环。
- `target`是一个变量，用于存储从异步可迭代对象中获取的每个元素。
- `async_iterable`是一个异步可迭代对象，它返回一个异步迭代器，每次迭代产生一个异步任务。

异步`for`循环的工作原理类似于普通的`for`循环，但是在每次迭代时，它会等待异步迭代器产生下一个元素，并异步处理每个元素。

以下是一个示例，演示了如何在异步上下文中使用异步`for`循环：

```python
import asyncio

async def async_iterable():
    for i in range(5):
        yield i
        await asyncio.sleep(1)  # 模拟异步操作

async def main():
    async for num in async_iterable():
        print(num)

asyncio.run(main())
```

在这个示例中，`async_iterable`函数是一个异步生成器，它会每隔一秒产生一个数字，并在产生每个数字时进行一次异步操作。然后，`main`函数使用异步`for`循环来遍历异步可迭代对象`async_iterable`产生的数字，并在每个数字上进行异步处理。

## 示例二
```python
import asyncio


# 异步函数，模拟异步计算
async def async_compute(num):
    await asyncio.sleep(1)  # 模拟耗时的异步操作
    return num * 2


# 异步生成器函数，返回异步迭代器对象
async def async_iterable():
    for i in range(5):
        result = await async_compute(i)  # 等待异步计算的结果
        yield result  # 使用 yield 返回结果，构建异步迭代器对象


async def main():
    async for result in async_iterable():
        print(result)


asyncio.run(main())

```