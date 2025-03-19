# 终端命令示例如下:
# locust -f locust_demo.py --headless -u 100 -r 10 -t 60 -H  https://www.baidu.com --html  report.html
# -u或 --users：指定要模拟的并发用户数量。
# -r或 --spawn-rate：指定每秒钟产生新用户的速率。
# -t或 --run-time：指定测试运行的持续时间。
# -H或 --host：指定要测试的目标主机（即被测应用的基本 URL）。
# -c或 --config：指定配置文件的路径，以定义更复杂的测试场景和用户行为。
# --html report.html: 生成html报告
from locust import HttpUser, task, between
from loguru import logger


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    # host参数是HttpUser类的一个属性,用于定义请求的基础域名,这样在发送请求时,只需要指定接口路径即可.Locust会自动将host属性的值与路径拼接起来形成完整的URL.
    host = "https://apissl.gifshow.com"

    url = "/rest/zt/frigate/col/loc/query"

    params = {
        "c": "BETA",
        "klg": "1",
        "did": "FE314352-35BC-457E-ACD6-215B8A548B8D",
        "earphoneMode": "1",
        "koinfo": "CMHi8eAKEAUY9vrdl-gxIAE",
        "klp": "MY_PROFILE",
        "mod": "iPhone10,2",
        "kpf": "IPHONE",
        "kpn": "KUAISHOU",
        "ud": "2695455579",
        "did_tag": "0",
        "ll_client_time": "1711617212858.862",
        "kli": "CMOXm7sGEg7kuK3lm73nlLXkv6FfNRjdzqyY6DEgAQ",
        "cdid_tag": "7",
        "vague": "0",
        "sys": "ios13.6.1",
        "sh": "2208",
        "klzs": "",
        "oDid": "FE314352-35BC-457E-ACD6-215B8A548B8D",
        "grant_browse_type": "AUTHORIZED",
        "keyconfig_state": "1",
        "sw": "1242",
        "deviceBit": "0",
        "isp": "",
        "kltag": "high",
        "cold_launch_time_ms": "1711617827107",
        "rdid": "FE314352-35BC-457E-ACD6-215B8A548B8D",
        "kltype": "1",
        "kls": "OFF",
        "lkvr": "MjlGNEY0RjUtMEVBJuchBwuPmyo8aKNo8gZTRZO0gRICRvqwmu3OMXmoyH9OVvuYUc_yPg",
        "userRecoBit": "0",
        "kcv": "1571",
        "is_background": "0",
        "klu": "1",
        "browseType": "4",
        "appver": "12.2.40.2106838",
        "net": "中国电信_5",
        "ver": "12.2",
        "egid": "DFPA8FD08B5D40335211D96606AE02E51BB6A55072AF8938477CF73AEA1668E4",
        "darkMode": "false",
        "__NS_sig3": "21304f73e5a800077a696a6bbe6a0af55546771574787660",
        "__NStokensig": "1e5d0baeb366f7e1bc1edcdff182378e05c706cd6959477e29a2bec1484a5b7f",
        "client_key": "56c3713c",
        "country_code": "cn",
        "cs": "false",
        "global_id": "DFPA8FD08B5D40335211D96606AE02E51BB6A55072AF8938477CF73AEA1668E4",
        "kuaishou.api_st": "Cg9rdWFpc2hvdS5hcGkuc3QSoAFssNq8K5z-qvU9E5jEnsxBkM-7J5O8N7jjA_TLQRV9bC9Q5E05S9kevh7cF9D8-4C5aIPK6Owh6uFGZgYn9KU0t-lYANDbbgFnhdaGh2taQVlgQ4JD_3IpsHW29tMaA7X71A8vp4rJPFtL_qP44uHPTq5I3ZVAPPYWJsPNz5VcIIBYv9Wf8c0cP6qdAj2cw-oiQko-4at0RhKpBjPUtGH9GhJyESpTOl5I_JMcRn3Byf2u1vciIEpkAwV2oFiYun4NnEDO1rGDVW1h1XGX2UkOXBLL1iDcKAUwAQ",
        "language": "zh-Hans-CN;q=1, zh-Hant-CN;q=0.9, en-CN;q=0.8",
        "power_mode": "0",
        "sig": "d00aaf12e508a584f06b78897c992eb3",
        "thermal": "10000",
        "token": "346a12b87e534e15a0a8591f07559206-2695455579",
        "uQaTag": "2#3333333333999999999",
        "videoModelCrowdTag": "1_100",
    }

    def on_start(self) -> None:
        # 在压测开始的时候执行一次  用于检测服务接口的可用性
        logger.info((res := self.client.get(self.path, params=self.params)).json())

    @task
    def get_request(self) -> None:
        self.client.get(self.url, params=self.params)


if __name__ == "__main__":
    # locust -f kuaishou_poi.py  --headless -u 100 -r 100 -t 50 --html report.html
    import os

    os.system("locust -f kuaishou_poi.py")
