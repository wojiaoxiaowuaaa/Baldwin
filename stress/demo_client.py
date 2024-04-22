from locust import HttpUser, task, between
from loguru import logger


class QuickstartUser(HttpUser):
    host = 'http://127.0.0.1:7890'

    between(1, 2)

    def on_start(self):
        # 测试开始后，每个虚拟用户（Locust实例）的运行逻辑都会遵循如下规律：先执行on_start作为初始化.
        login_result = self.client.post("/login", json={"username": "Tom", "password": "123456"}).text
        # logger.info(f"login_result:{login_result}")

    def on_stop(self):
        logout_result = self.client.post("/logout", json={"username": "Jim", "password": "456789"}).text
        # logger.info(f"logout_result:{logout_result}")

    @task
    def hello(self):
        res = self.client.get("/hello")
        # logger.info(f'hello response:{res.text}')

    @task(2)
    def world(self):
        res = self.client.get("/world")
        # logger.info(f'world response:{res.text}')


# if __name__ == '__main__':
#     import os
#     os.system("locust -f demo_client.py --headless  -u 30 -r 3 -t 10 --html report.html")
