from playwright.sync_api import Playwright, sync_playwright
from loguru import logger


# 创建浏览器
def run(playwright: Playwright) -> None:
    logger.info("开始执行")
    # 创建浏览器
    browser = playwright.chromium.launch(headless=False)

    # 新建窗口
    content = browser.new_context()

    # 新建页面
    page = content.new_page()

    # 访问首页
    page.goto("https://hepai.video/")

    # 点击登录
    page.click('//a[@href="/login"]')

    # 延迟
    page.wait_for_timeout(1000)

    # 密码登录
    page.click('//a[contains(text(), "密码登录")]')

    # 写入账号
    page.fill('//input[@id="username"]', "wlhandsome")

    # 写入密码
    page.fill('//input[@id="password"]', "1qaz2wsx")

    # 点击登录
    page.click('//button[@type="submit"]')

    # 延迟
    page.wait_for_timeout(1000)

    # hover 出菜单（失败）
    # page.hover('//div[@class="nav-adv nav-adv-home u-info"]/p')
    # page.wait_for_selector('//div[@class="nav-adv nav-adv-home u-info"]/ul', state='visible', timeout=30000)
    # page.locator('//div[@class="nav-adv nav-adv-home u-info"]/ul')
    # 延迟
    # page.wait_for_timeout(1000)
    # 点击财务管理
    # page.click('//a[@href="/pipeline-record"]')

    # 上面 hover 失败，那就直接手动加载网页
    page.goto("https://hepai.video/pipeline-record")

    # 延迟
    page.wait_for_timeout(1000)

    # hover 出菜单
    page.hover('//div[@class="u-info"]/img')

    page.wait_for_timeout(3000)

    logger.info("点击button退出登录")

    # 退出登录
    page.click('//a[contains(text(), "退出登录")]')

    # 点击确定按钮
    page.click('//button/span[contains(text(), "确")]/..')

    # 延迟
    page.wait_for_timeout(10000)

    # 关闭上下文
    content.close()

    # 关闭浏览器
    browser.close()

    logger.info("执行完毕")


# 调用
with sync_playwright() as pw:
    run(pw)
