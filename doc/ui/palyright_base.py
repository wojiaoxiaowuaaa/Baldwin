from playwright.sync_api import sync_playwright

"""录制命令
playwright codegen -o script.py -b firefox
博客教程
https://cuiqingcai.com/36045.html
系统教程文档
https://www.h3blog.com/article/431/

Playwrigt 会安装 Chromium, Firefox 等浏览器并配置一些驱动，我们不必关心中间配置的过程，Playwright 会为我们配置好。
(部分机器不会安装,脚本执行时会报错,配置好环境变量后执行playwright install即可)
使用 sync_playwright 方法启动浏览器。 
sync_playwright方法返回的是一个PlaywrightContextManager对象,可以理解是一个浏览器上下文管理器，我们将其赋值为变量p
使用 browser.new_page() 方法创建新的浏览器页面。 
使用 page.goto(url) 方法打开指定网页。 
使用 page.title() 方法获取网页标题。 
使用 browser.close() 方法关闭浏览器"""

with sync_playwright() as p:
    # slow_mo(单位是毫秒）减慢执行速度。它的作用范围是全局的，从启动浏览器到操作元素每个动作都会有等待间隔，方便在出现问题的时候看到页面操作情况。
    browser = p.chromium.launch(headless=False, slow_mo=100)
    # launch 方法返回的是一个 Browser 对象，调用 browser的new_page方法相当于新建了一个选项卡
    page = browser.new_page()
    # 调用 page 的一系列 API 来进行各种自动化操作了.比如调用goto方法就是加载某个页面.screenshot截图.
    page.goto("http://www.baidu.com")
    page.screenshot(path=f"screenshot-.png")

    # 等待5秒
    page.wait_for_timeout(5000)

    page.goto("https://www.h3blog.com")
    title = page.title()
    print(title)

    browser.close()
