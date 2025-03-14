#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Date: 2025/3/14 13:59


# import asyncio
# from pydoll.browser.chrome import Chrome

# async def visit_baidu():
#     # 创建 Chrome 浏览器实例
#     async with Chrome() as browser:
#         await browser.start()
#         print(dir(browser))
#         # 获取一个页面
#         page = await browser.get_page()
#         # print(dir(page))
#         # 访问百度
#         await page.go_to('https://www.baidu.com')
#         # 获取页面标题
#         # title = await page.title()
#         # print(f"页面标题: {title}")
#         # 关闭页面
#         await page.close()

# # 运行异步函数
# asyncio.run(visit_baidu())


# import asyncio
# from pydoll.browser.chrome import Chrome
# from pydoll.constants import By

# async def main():
#     # Start the browser with no additional webdriver configuration!
#     async with Chrome() as browser:
#         await browser.start()
#         page = await browser.get_page()

#         # Navigate through captcha-protected sites without worry
#         await page.go_to('https://example-with-cloudflare.com')
#         button = await page.find_element(By.CSS_SELECTOR, 'button')
#         await button.click()

# asyncio.run(main())
