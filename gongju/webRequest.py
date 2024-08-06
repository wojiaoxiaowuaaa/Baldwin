# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     WebRequest
   Description :   Network Requests Class
   Author :        J_hao
   date:          2017/7/31
-------------------------------------------------
"""
from requests.models import Response
from lxml import etree
import requests
import random
import time
from urllib3 import disable_warnings
from log_register import LogRegister

disable_warnings()
# requests.packages.urllib3.disable_warnings()


class WebRequest(object):
    """封装的请求类 包含自定义日志记录"""

    name = "webRequest"  # 类变量 日志文件名

    def __init__(self, *args, **kwargs):
        self.log = LogRegister(self.name, file=False)  # 实例变量 日志记录
        self.response = Response()

    @property
    def user_agent(self):
        """
        return an User-Agent at random
        :return:
        """
        ua_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
            "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
        ]
        return random.choice(ua_list)

    @property
    def header(self):
        """
        basic header
        :return:
        """
        return {
            "User-Agent": self.user_agent,
            "Accept": "*/*",
            "Connection": "keep-alive",
            "Accept-Language": "zh-CN,zh;q=0.8",
        }

    def get(
        self,
        url,
        header=None,
        retry_time=3,
        retry_interval=3,
        timeout=5,
        *args,
        **kwargs
    ):

        headers = self.header
        if header and isinstance(header, dict):
            headers.update(header)
        while True:
            try:
                self.response = requests.get(
                    url, headers=headers, timeout=timeout, *args, **kwargs
                )
                return self
            except Exception as e:
                self.log.error("requests: %s error: %s" % (url, str(e)))
                retry_time -= 1
                if retry_time <= 0:
                    resp = Response()
                    resp.status_code = 500
                    return self
                self.log.info("retry %s second after" % retry_interval)
                time.sleep(retry_interval)

    def post(
        self,
        url,
        data=None,
        json=None,
        header=None,
        retry_time=3,
        retry_interval=3,
        timeout=5,
        *args,
        **kwargs
    ):
        headers = self.header
        if header and isinstance(header, dict):
            headers.update(header)
        while True:
            try:
                self.response = requests.post(
                    url,
                    data=data,
                    json=json,
                    headers=headers,
                    timeout=timeout,
                    *args,
                    **kwargs
                )
                return self
            except Exception as e:
                self.log.error("requests: %s error: %s" % (url, str(e)))
                retry_time -= 1
                if retry_time <= 0:
                    resp = Response()
                    resp.status_code = 200  # 注意:这里设置状态码为200可能不合适,因为请求实际上失败了.应考虑使用更合适的错误处理
                    return self
                self.log.info("retry %s second after" % retry_interval)
                time.sleep(retry_interval)

    @property
    def tree(self):
        return etree.HTML(self.response.content)

    @property
    def text(self):
        return self.response.text

    @property
    def json(self):
        try:
            # return self.response.json()
            return self.response.json
        except Exception as e:
            self.log.error(str(e))
            return {}


if __name__ == "__main__":
    web_log = WebRequest().log
    baidu = WebRequest().get("https://www.baidu.com").json
    # web_log.info(baidu)
    # print(dir(web_log))
