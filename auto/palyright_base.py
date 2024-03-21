from playwright.sync_api import sync_playwright

# sync_playwright 方法返回的是一个 PlaywrightContextManager 对象，可以理解是一个浏览器上下文管理器，我们将其赋值为变量 p。
with sync_playwright() as p:
    # Playwrigth 会安装 Chromium, Firefox 等浏览器并配置一些驱动，我们不必关心中间配置的过程，Playwright 会为我们配置好。
    browser = p.chromium.launch(headless=False)
    # launch 方法返回的是一个 Browser 对象，我们将其赋值为 browser 变量。然后调用 browser 的 new_page 方法，相当于新建了一个选项卡，
    # 返回的是一个 Page 对象，将其赋值为 page，
    page = browser.new_page()
    # 调用 page 的一系列 API 来进行各种自动化操作了，比如调用 goto，就是加载某个页面.screenshot截图.
    page.goto('http://www.baidu.com')
    page.screenshot(path=f'screenshot-.png')
    print(page.title)
    browser.close()
