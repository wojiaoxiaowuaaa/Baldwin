# -*- coding: utf-8 -*-
from locust import HttpUser, task, TaskSet
import json
import os


class WebsiteTask(TaskSet):
    api_header = {"Content-Type": 'application/json'}  # 类变量保存每个接口都需要的header信息

    def __login(self):
        login_api = 'http://test.ssa.jd.com/sso/login?ReturnUrl=http://test.dp.jd.com/jbdpEdc/template-manage/role'

        login_data = {
            'fp': '6WRKXJ6ZPCNIZJWRVTQVJTUE6REKKM4ZDZVYLUJ26XGJUZBPNCRRQLBBZOMIMBQLJFAGLUIFF7XMCQMR3BBKZXEU3E',
            'loginKey': '',
            'username': 'wangqiaohui',
            'password': 'e6uLz2uL1jtvMdUzj+UeANENScuIFWvpjMw4sbns6pkWmj36S+0EJZPf7RKOHX4xrTm7E5tztmGMk/iX05GjGHDPFI9RPKAD+3WHbd4gIUyMpu0T5OW6HirCTkyEqSz3U4p7BgBC4XVL5FkUpme7MOtVEZ66Q4ffp4pYHRZohqs=',
            'noPwdFlag': '',
            'uuid': '79ed2daf8ef2403eb678478efe1be9ba',
            'checkType': '1',
            'authInfo': '',
            'checkCode': '',
        }

        cookie = {
            'jd.erp.lang': 'zh_CN',
            'jdd69fo72b8lfeoe': '6WRKXJ6ZPCNIZJWRVTQVJTUE6REKKM4ZDZVYLUJ26XGJUZBPNCRRQLBBZOMIMBQLJFAGLUIFF7XMCQMR3BBKZXEU3E',
            '__jda': '134439668.1660280106496622070314.1660280106.1660635581.1660638266.4',
            '__jdv': '82619667|test-c.dp.jd.com|-|referral|-|1660280106497',
            '__jdu': '1660280106496622070314',
            '__jdb': '134439668.14.1660280106496622070314|4.1660638266',
            '__jdc': '134439668',
        }

        login_header = {
            'Host': 'test.ssa.jd.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:103.0) Gecko/20100101 Firefox/103.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Origin': 'http://test.ssa.jd.com',
            'Referer': 'http://test.ssa.jd.com/sso/login?ReturnUrl=http://test.dp.jd.com/jbdpEdc/withdrawal-manage/task',
            # Requests sorts cookies= alphabetically
            # 'Cookie': 'jd.erp.lang=zh_CN; jdd69fo72b8lfeoe=6WRKXJ6ZPCNIZJWRVTQVJTUE6REKKM4ZDZVYLUJ26XGJUZBPNCRRQLBBZOMIMBQLJFAGLUIFF7XMCQMR3BBKZXEU3E; __jda=134439668.1660280106496622070314.1660280106.1660635581.1660638266.4; __jdv=82619667|test-c.dp.jd.com|-|referral|-|1660280106497; __jdu=1660280106496622070314; __jdb=134439668.14.1660280106496622070314|4.1660638266; __jdc=134439668',
            'Upgrade-Insecure-Requests': '1',
        }

        # 登录并维持会话
        res = self.client.post(login_api, login_data, headers=login_header, cookies=cookie)
        print('====== 登录成功 ======')

    def on_start(self):
        self.__login()  # 执行操作前先进行登录,并且只登录一次

    def on_stop(self):
        print("---test over---")

    @task
    def api_get_member(self):
        # 获取项目空间成员接口
        role_data = {
            "projectId": 100404,
            "pageStart": 1,
            "page": 1,
            "pageSize": 10
        }
        res = self.client.post('/jbdpEdc/api/getRolePage', json.dumps(role_data), headers=self.api_header)
        print(res.json())
        print(res.status_code, '--->')


class WebsiteUser(HttpUser):
    tasks = [WebsiteTask]
    between = [1, 2]
    host = 'test.dp.jd.com'


if __name__ == '__main__':
    import os
    os.system("locust -f locust_demo01.py --headless -u 10 -r 1 -t 10 --html report.html")