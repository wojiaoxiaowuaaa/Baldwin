# -*- coding: utf-8 -*-
from locust import HttpUser, task, TaskSet, events
import json
import os

# 全局存储登录凭证
global_cookies = {}


@events.test_start.add_listener
def on_test_start(**kwargs):
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
    
    login_header = {
        'Host': 'test.ssa.jd.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:103.0) Gecko/20100101 Firefox/103.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Origin': 'http://test.ssa.jd.com',
        'Referer': 'http://test.ssa.jd.com/sso/login?ReturnUrl=http://test.dp.jd.com/jbdpEdc/withdrawal-manage/task',
        'Upgrade-Insecure-Requests': '1',
    }

    # 全局单次登录
    import requests
    session = requests.Session()
    response = session.post(login_api, data=login_data, headers=login_header)
    global global_cookies
    global_cookies = session.cookies.get_dict()
    print('====== 全局登录成功 ======')


class WebsiteTask(TaskSet):
    api_header = {
        "Content-Type": "application/json",
    }

    def on_start(self):
        # 使用全局cookies
        if global_cookies:
            self.client.cookies.update(global_cookies)

    def on_stop(self):
        print("---test over---")

    @task
    def api_get_member(self):
        role_data = {
            "projectId": 100404,
            "pageStart": 1,
            "page": 1,
            "pageSize": 10
        }
        res = self.client.post('/jbdpEdc/api/getRolePage', json.dumps(role_data), headers=self.api_header)
        print(res.status_code, '--->')


class WebsiteUser(HttpUser):
    tasks = [WebsiteTask]
    between = [1, 2]
    host = 'test.dp.jd.com'

