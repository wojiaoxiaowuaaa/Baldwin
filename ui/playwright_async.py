import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            # print(browser_type.name)
            browser = await browser_type.launch()  # launch参数为空 走默认为逻辑 无头模式
            page = await browser.new_page()
            await page.goto('https://www.baidu.com')
            await page.screenshot(path=f'screenshot_{browser_type.name}.png')  # 使用浏览器类型来命名截图文件,否则只会保留最后一张.前面的被覆盖.
            print(await page.title())
            await browser.close()


asyncio.run(main())
