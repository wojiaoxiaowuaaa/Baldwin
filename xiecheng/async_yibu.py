import aiohttp
import asyncio


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    # 同时发起多个网络请求, 使用异步操作，你可以在单个线程中并发处理这些请求，而不必等待每个请求完成。
    # 异步操作允许在同一线程中处理多个任务而不阻塞程序执行。
    urls = ["https://www.baidu.com/?tn=02003390_42_hao_pg", "https://www.douban.com/", 'https://www.bing.com/']
    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)
    print(results[1])


asyncio.run(main())
