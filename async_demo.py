import asyncio
import aiohttp
import time
from loguru import logger
from tqdm.asyncio import tqdm

DOMAINS = [
    'https://www.google.com',
    'https://www.github.com',
    'https://www.wikipedia.org',
    'https://www.stackoverflow.com',
    'https://www.reddit.com',
    'https://www.microsoft.com',
    'https://www.baidu.com',
    'https://www.tencent.com',
    'https://www.taobao.com',
    'https://www.jd.com',
    'https://www.1688.com',
    'https://www.alibaba.com',
]

USE_PROXY = False
PROXY_URL = 'http://127.0.0.1:7890'  # 可选：启用 HTTP/HTTPS 代理


async def fetch(session, url):
    start_time = time.perf_counter()
    try:
        kwargs = {}
        if USE_PROXY:
            kwargs['proxy'] = PROXY_URL

        async with session.get(url, timeout=10, **kwargs) as response:
            await response.text()
            elapsed = (time.perf_counter() - start_time) * 1000
            return {'url': url, 'status': response.status, 'elapsed_ms': int(elapsed), 'error': None}
    except Exception as e:
        elapsed = (time.perf_counter() - start_time) * 1000
        return {'url': url, 'status': None, 'elapsed_ms': int(elapsed), 'error': str(e)}


async def main():
    conn = aiohttp.TCPConnector(ssl=False)  # 有些站点 SSL 验证容易失败，可关掉
    async with aiohttp.ClientSession(connector=conn) as session:
        tasks = [fetch(session, url) for url in DOMAINS]
        return [await coro for coro in tqdm.as_completed(tasks, total=len(tasks), desc="访问中......")]


if __name__ == "__main__":
    results = asyncio.run(main())
    logger.info("📊 请求结果")
    for r in results:
        if r['error']:
            logger.info(f"[❌ FAIL] {r['url']:<40} - {r['error']} ({r['elapsed_ms']} ms)")
        else:
            logger.info(f"[✅ OK  ] {r['url']:<40} - {r['status']} ({r['elapsed_ms']} ms)")
