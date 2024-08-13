from threading import Thread
from DrissionPage import ChromiumPage
from DataRecorder import Recorder


def collect(tab, recorder, title):
    """
    https://g1879.gitee.io/drissionpagedocs/
    :param tab: ChromiumTab 对象
    :param recorder: Recorder 记录器对象
    :param title: 类别标题
    :return: None
    """
    num = 1  # 当前采集页数
    while True:
        # 遍历所有标题元素
        for i in tab.eles(".title project-namespace-path"):
            # 获取某页所有库名称，记录到记录器
            recorder.add_data((title, i.text, num))
        # 如果有下一页，点击翻页
        btn = tab("@rel=next", timeout=2)
        if btn:
            btn.click(by_js=True)
            tab.wait.load_start()
            num += 1
        # 否则，采集完毕
        else:
            break


def main():
    # 新建页面对象
    page = ChromiumPage()
    # 第一个标签页访问网址
    page.get("https://gitee.com/explore/ai")
    # 获取第一个标签页对象
    tab1 = page.get_tab()
    # 新建一个标签页并访问另一个网址
    tab = page.new_tab("https://gitee.com/explore/machine-learning")
    # 获取第二个标签页对象
    tab2 = page.get_tab(tab)
    # 新建记录器对象
    recorder = Recorder("/Users/mac/Desktop/data.csv")

    # 多线程同时处理多个页面
    Thread(target=collect, args=(tab1, recorder, "ai")).start()
    Thread(target=collect, args=(tab2, recorder, "机器学习")).start()


if __name__ == "__main__":
    main()

"""
https://gitee.com/g1879/DrissionPage

https://drissionpage.cn/

DrissionPage是一个基于Selenium 的轻量级自动化测试框架，支持多浏览器，支持多页面，支持多窗

from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://www.baidu.com')
page.close()

"""
