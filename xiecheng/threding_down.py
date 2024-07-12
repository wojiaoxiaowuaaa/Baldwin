import concurrent.futures
import time
from typing import List
import requests


def down_one(url: str) -> None:
    resp = requests.get(url)
    print(len(resp.content), url)


def down_all(urls: List[str]) -> None:
    """单线程版本: for _ in urls:down_one(_)
    (并发之)多线程版本:创建一个线程池,用于并发执行多个任务.max_workers=5 指定了线程池中的最大线程数为5.这在处理I/O密集型任务时特别有用,如网络请求、文件读写等
    另外，虽然线程的数量可以自己定义，但是线程数并不是越多越好，因为线程的创建、维护和删除也会有一定的开销。所以如果你设置的很大，反而可能会导致速度变慢.我们往往需要根据实际的需求做一些测试,来寻找最优的线程数量
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(down_one, urls)


def main():
    sites = [
        "https://en.wikipedia.org/wiki/Portal:Arts",
        "https://en.wikipedia.org/wiki/Portal:History",
        "https://en.wikipedia.org/wiki/Portal:Society",
        "https://en.wikipedia.org/wiki/Portal:Biography",
        "https://en.wikipedia.org/wiki/Portal:Mathematics",
        "https://en.wikipedia.org/wiki/Portal:Technology",
        "https://en.wikipedia.org/wiki/Portal:Geography",
        "https://en.wikipedia.org/wiki/Portal:Science",
        "https://en.wikipedia.org/wiki/Computer_science",
        "https://en.wikipedia.org/wiki/Python_(programming_language)",
        "https://en.wikipedia.org/wiki/Java_(programming_language)",
        "https://en.wikipedia.org/wiki/PHP",
        "https://en.wikipedia.org/wiki/Node.js",
        "https://en.wikipedia.org/wiki/The_C_Programming_Language",
        "https://en.wikipedia.org/wiki/Go_(programming_language)",
    ]
    s = time.perf_counter()
    down_all(sites)
    e = time.perf_counter()
    print(f"Finished in {e - s:.2f} seconds")


main()


"""
import asyncio
import aiohttp
import time
from typing import List, Optional


async def download_one(url: str) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.content_type, url)


async def download_all(urls: List[str]) -> None:
    # 并发之协程多任务
    tasks = [asyncio.create_task(download_one(url)) for url in urls]
    await asyncio.gather(*tasks)


def main():
    sites = [
        "https://en.wikipedia.org/wiki/Portal:Arts",
        "https://en.wikipedia.org/wiki/Portal:History",
        "https://en.wikipedia.org/wiki/Portal:Society",
        "https://en.wikipedia.org/wiki/Portal:Biography",
        "https://en.wikipedia.org/wiki/Portal:Mathematics",
        "https://en.wikipedia.org/wiki/Portal:Technology",
        "https://en.wikipedia.org/wiki/Portal:Geography",
        "https://en.wikipedia.org/wiki/Portal:Science",
        "https://en.wikipedia.org/wiki/Computer_science",
        "https://en.wikipedia.org/wiki/Python_(programming_language)",
        "https://en.wikipedia.org/wiki/Java_(programming_language)",
        "https://en.wikipedia.org/wiki/PHP",
        "https://en.wikipedia.org/wiki/Node.js",
        "https://en.wikipedia.org/wiki/The_C_Programming_Language",
        "https://en.wikipedia.org/wiki/Go_(programming_language)",
    ]
    s = time.perf_counter()
    asyncio.run(download_all(sites))
    print(time.perf_counter() - s)


if __name__ == "__main__":
    main()

"""
