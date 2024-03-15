from loguru import logger
import asyncio


async def task():
    logger.info("before!")
    await asyncio.sleep(3)  # 模拟耗时操作
    logger.info("after!")


async def main():
    try:
        await asyncio.wait_for(task(), timeout=3)  # 设置超时时间为3秒
    except asyncio.TimeoutError:
        logger.info("Task timed out!")


asyncio.run(main())
