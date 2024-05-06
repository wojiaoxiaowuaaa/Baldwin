from DrissionPage import ChromiumPage

"""
https://gitee.com/g1879/DrissionPage

https://drissionpage.cn/

DrissionPage是一个基于Selenium 的轻量级自动化测试框架，支持多浏览器，支持多页面，支持多窗

"""
page = ChromiumPage()
page.get('https://www.baidu.com')
page.close()
