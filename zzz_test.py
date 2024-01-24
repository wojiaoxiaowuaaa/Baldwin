from DrissionPage import ChromiumPage, SessionPage, WebPage
from time import sleep
from time_count import calculate_execution_time


@calculate_execution_time
def func():
    page = ChromiumPage()

    page.get('https://www.google.com')

    sleep(3)

    page.quit()


if __name__ == '__main__':
    func()


