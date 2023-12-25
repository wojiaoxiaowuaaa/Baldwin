from locust import HttpUser, TaskSet, wait_time, between, task


class BaiDu(HttpUser):
    wait_time = between(1, 3)

    @task
    def search(self):
        self.client.get("/?tn=54093922_30_hao_pg")


# locust -f locust_demo.py --headless -u 100 -r 10 -t 3600 -H  https://www.baidu.com --html  report.html

# -u或 --users：指定要模拟的并发用户数量。
# -r或 --spawn-rate：指定每秒钟产生新用户的速率。
# -t或 --run-time：指定测试运行的持续时间。
# -H或 --host：指定要测试的目标主机（即被测应用的基本 URL）。
# -c或 --config：指定配置文件的路径，以定义更复杂的测试场景和用户行为。
