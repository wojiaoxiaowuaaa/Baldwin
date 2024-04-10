from playwright.sync_api import Playwright, sync_playwright
from loguru import logger
from time import sleep
# 启动浏览器
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # 打开指定网页
    page.goto('https://www.h3blog.com')
    # 获取网页标题
    title = page.title()
    print(title)
    logger.info(dir(browser))
    sleep(5)
    # 关闭浏览器
    browser.close()
