import asyncio
import os


async def async_walk(pwd):
    # 用于异步遍历目录的函数 返回指定目录下的所有文件的绝对路径
    for root, dirs, filenames in os.walk(pwd):
        for filename in filenames:
            # yield 语句的作用是将每个文件的路径作为生成器的值返回给调用者。它实现了一种惰性计算的方式，在每次迭代时生成一个文件路径，而不是一次性将所有文件路径都生成出来。这种方式可以节省内存，特别是在处理大量文件时。
            yield os.path.join(root, filename)


async def main():
    l = []
    # async for 循环会等待异步生成器产生的值，而异步生成器会在需要时异步地生成值并将其返回给循环. os用于获取当前脚本所在目录的上级目录的绝对路径.
    async for res in async_walk(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]):
        l.append(res)
    print(len(l))
    return l


# yield 语句用于在异步生成器中生成值，而 async for 循环用于异步地迭代生成器产生的值。
asyncio.run(main())
