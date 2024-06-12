"""
from locust import HttpUser, TaskSet, wait_time, between, task, FastHttpUser


# locust -f locust_demo.py --headless -u 100 -r 10 -t 60 -H  https://www.baidu.com --html  report.html

# -u或 --users：指定要模拟的并发用户数量。
# -r或 --spawn-rate：指定每秒钟产生新用户的速率。
# -t或 --run-time：指定测试运行的持续时间。
# -H或 --host：指定要测试的目标主机（即被测应用的基本 URL）。
# -c或 --config：指定配置文件的路径，以定义更复杂的测试场景和用户行为。
# --html report.html: 生成html报告

# class UserBehavior(TaskSet):
#     @task
#     def search(self):...


class BaiDu(HttpUser):
    wait_time = between(1, 3)

    host = "https://www.baidu.com"

    @task
    def search(self):
        self.client.get("/?tn=54093922_30_hao_pg")

"""
import time
import threading
import requests
from loguru import logger


NQ = 1
COUNT = 3000
api = "http://127.0.0.1:7890/hello"


def qps_tc():
    start = time.time()
    req = requests.get(api)
    # logger.info(req.text)
    assert req.status_code == 200
    end = time.time() - start


if __name__ == "__main__":
    # single thread
    # logger.info(f'Single thread perform search action one by one {COUNT} --- {NQ}')
    # time_start = time.time()
    # for k in range(COUNT):
    #     qps_tc()
    # time_cost = time.time() - time_start
    # logger.info(f'Totally time cost{time_cost}')
    # logger.info(f'QPS{ COUNT / time_cost}')

    # multi thread
    logger.info(f'Multi-thread perform search action parallelly {COUNT}  {NQ}')
    threads = []
    time_start = time.time()
    for k in range(COUNT):
        x = threading.Thread(target=qps_tc, args=())
        threads.append(x)
        x.start()
    for th in threads:
        th.join()
    time_cost = time.time() - time_start
    logger.info(f'Totally time cost {time_cost}  sec')
    logger.info(f'QPS: {COUNT / time_cost}')

