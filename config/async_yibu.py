import aiohttp
import asyncio
from loguru import logger


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    # 同时发起多个网络请求, 使用异步操作，你可以在单个线程中并发处理这些请求，而不必等待每个请求完成。
    # 异步操作允许在同一线程中处理多个任务而不阻塞程序执行。
    urls = [
        "https://www.baidu.com/?tn=02003390_42_hao_pg",
        "https://www.douban.com/",
        "https://www.bing.com/",
    ]
    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)
    # print(results[0])
    for _ in results:
        logger.info(_)


asyncio.run(main())

"""
import time
import asyncio
import aiohttp

# 使用HTTPS提高安全性
host = 'https://example.com'
# 从外部文件或环境变量加载URLs，这里仍然硬编码作为示例
urls_todo = {'/', '/1', '/2', '/3', '/4', '/5', '/6', '/7', '/8', '/9'}


async def fetch(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                # 确保响应状态码表明成功
                if response.status == 200:
                    return await response.read()
                else:
                    print(f"请求失败，状态码：{response.status}")
                    return b""

    except aiohttp.ClientError as e:
        # 捕获网络请求相关的异常
        print(f"请求异常：{e}")
        return b""


if __name__ == '__main__':
    start = time.time()

    # 使用更现代的API管理事件循环和任务
    async def main():
        tasks = [fetch(host + url) for url in urls_todo]
        responses = await asyncio.gather(*tasks)
        # 打印所有响应的长度，仅作为简单示例
        for response in responses:
            print(len(response))

    asyncio.run(main())
    print(time.time() - start)


"""
