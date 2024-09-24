import httpx
import asyncio
from loguru import logger


async def fetch_data(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.text


async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3",
    ]

    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)

    for result in results:
        logger.info(result)


if __name__ == "__main__":
    # fetch_data 函数负责异步地获取指定 URL 的内容;main 函数则是协调执行多个异步任务;
    asyncio.run(main())
