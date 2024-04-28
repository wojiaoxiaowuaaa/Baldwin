from time import ctime
from loguru import logger
import urllib3
from locust import HttpUser, task, between, events

urllib3.disable_warnings()


@events.test_start.add_listener
def on_test_start(**kwargs):
    logger.info(f'===测试最开始提示===:{ctime()}')


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    logger.info(f'===测试最结束提示==={ctime()}')


class TestTask(HttpUser):
    wait_time = between(1, 2)

    host = 'https://www.baidu.com'

    def on_start(self):
        # 请求次数与与生成的测试用户数有关,执行命令中的-u参数,或者图形界面的number of users(第一行, 用户数---峰值并发.)
        logger.info(f'这是SETUP，每次实例化User前都会执行！{ctime()}')

    @task
    def getBaidu(self):
        res = self.client.get(url="/", verify=False)
        logger.info(res.status_code)

    def on_stop(self):
        logger.info(f'这是TEARDOWN，每次销毁User实例时都会执行！{ctime()}')


# class MyLocust(FastHttpLocust):
#     task_set = TestTask
#     min_wait = 1000
#     max_wait = 60000


if __name__ == "__main__":
    # 执行python3  locust_demo02.py
    # os.system("locust -f locust_demo02.py --host=https://www.baidu.com")
    import os
    os.system("locust -f locust_demo02.py --headless -u 10 -r 1 -t 10 --html report.html")
