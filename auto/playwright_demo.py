from playwright.sync_api import Playwright, sync_playwright

"""下载驱动命令为playwright install下载后会自动配置驱动路径,即开即用.mac下的浏览器驱动存储的默认路径 /Users/wl/Library/Caches/ms-playwright 
该库的源码在github加星列表,由微软开源"""


def run(playwright: Playwright) -> None:
    # 创建浏览器
    browser = playwright.chromium.launch(headless=False)

    # 使用 selenium 如果要打开多个网页，需要创建多个浏览器，但是 playwright 中只需要创建多个上下文即可
    # 例如：content1 = browser.new_context()、content2 = browser.new_context() 分别去访问网页做处理
    content = browser.new_context()

    # 每个 content 就是一个会话窗口，可以创建自己的页面，也就是浏览器上的 tab 栏，在每个会话窗口中，可以创建多个页面，也就是多个 tab 栏
    # 例如：page1 = content.new_page()、page2 = content.new_page() 分别去访问页面
    page = content.new_page()

    # 页面打开指定网址
    page.goto('https://www.baidu.com')

    # 找到百度输入框（ locator 会自动识别传入的选择器是 css xpath .... 不需要像 selenium 指定 By.XPATH/ID 这样的 ）
    # page.locator('//input[@id="kw"]').fill('周杰伦') # 也可以写成下面这样：
    page.fill('//input[@id="kw"]', '周杰伦')

    # 点击百度一下进行搜索
    # page.locator('//input[@id="su"]').click() # 也可以写成下面这样：
    page.click('//input[@id="su"]')

    # 延迟关闭（为啥需要延迟一下，这里是用于测试，因为代码执行完马上就回关闭，运行太快了，还以为崩溃了
    # 暂时没找到配置不需要进行自动关闭，但是肯定跟 selenium 一样有这个配置）
    # sleep(10) # 之前使用使用 sleep 的方式进行等待，传入的是单位是秒
    # 但是在 playwright 中有自带的延迟等待，单位是毫秒
    page.wait_for_timeout(10000)

    # 使用完成关闭上下文（也就是会话窗口）
    content.close()

    # 关闭浏览器
    browser.close()


# 调用
with sync_playwright() as playwright:
    run(playwright)
