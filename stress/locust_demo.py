from locust import HttpUser, TaskSet, task, between
from loguru import logger
import requests
import time

cookies = {
    '__jdu': '1658391070137334238237',
    'pinId': 'lPhtT2OwOjs8udM_MW6XwbV9-x-f3wj7',
    'shshshfpa': 'dd504387-bbe0-7d63-83de-21415b6ad26f-1662210772',
    'shshshfpb': 'tsPxXKwLETUi0M5twG_PeCg',
    'pin': 'jd_6f9e1931f53e5',
    'unick': '%E5%87%89%E7%94%9F%E7%9A%84%E5%89%91%E5%8D%A7%E8%96%AA%E5%B0%9D%E8%83%86',
    '_tp': 'GuWTejsOX%2BEoD%2BLZp1eou%2BOX8kMoRcs8j9MgQxVIJFM%3D',
    '_pst': 'jd_6f9e1931f53e5',
    'user-key': '762691c2-2cca-49fb-8340-4accc96c6ab0',
    '__jdv': '134439668|direct|-|none|-|1665727647642',
    'PCSYCityID': 'CN_110000_110100_0',
    'TrackID': '18rG5IOHAY5x-ywTDTH7lG1AHxPoeHnQlKGri-XLHzwH2UJgxCy9tSKDYB39B1IV075qt25Hicf1LMsVe4ZOgTNG8gW_QTBUM-IqS6CyjVRFDYVk-NGb8ApOvselwoANI',
    'ceshi3.com': '103',
    'cn': '4',
    'areaId': '1',
    'ipLoc-djd': '1-2802-54745-0',
    'mt_xid': 'V2_52007VwMVVlRaWloeTxhcB2EBEFdeWltZHU8pDABuBhRXXg9OCR1KHUAANwoTTlRQB1IDQEtaAWZXGgZbDAJcL0oYXwZ7AxNOXV5DWhZCGlUOZwIiUG1bYlkeTxFZAFcBGlBd',
    'shshshfp': 'ef105dcfa173e3545719bf22b0b381d4',
    '3AB9D23F7A4B3C9B': 'TV4BCKDYZBPBL3M7HI5FKHLUPPAPYJJXWXKOFDLWS7Q2S45GJWCGDWA3QXOMNI4RYYSGPEGIHOUVLKUI5YTOC6CPUA',
    'jd.erp.lang': 'zh_CN',
    'jdd69fo72b8lfeoe': 'KNP7DSQOYN45PFCY7ZC5SVRACEKCHZMDFL7LR4QERN7QJTTZMZ3N2SZSMTVOVCC4F3WO5R2HPDIDX7YY4QZ3RBKJ3Q',
    'logbook_u': 'ext.wanglei48',
    'fp': 'c778e9a4228d63371715d7f0916acb8c',
    'X-JACP-TOKEN': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJtb2JpbGUiOiIxODUwNjgzMjg1MCIsInVzZXJJZCI6ImV4dC53YW5nbGVpNDgiLCJlbWFpbCI6ImV4dC53YW5nbGVpNDhAamQuY29tIiwidXNlcm5hbWUiOiJleHQud2FuZ2xlaTQ4IiwiaWF0IjoxNjY2MTY0NjgzLCJpc3MiOiJ4aW5neXVuLmpkLmNvbSIsInN1YiI6InNzbyIsImV4cCI6MTY2NjI1MTA4M30.evBOMhb36xQQpgXSGL-1vUcu1T0YTi5YzPQmKcfKUFbAN7ZOsRtzOYcZ5DngEfjr-uK7n9mFWlV9G0MZ1b9WrtLcuUmTZqv_L-A-xgz8kU19DUhWXpqMxQ_EH0MAntfQP1EwhzEJioPF7lbpd0UclQmWCSsijRTEyq5Li_9VDribP9M8yA0L3RXGxwtStM7Osx6Ow-Z6-s5ixm8ZGFnSQ8eRsUTILg27R9uMmR3YM3dZ96nZjl2vKPBkNOIZQAAeOTAQmexOt9tcPUN09VfCTXEGIijOp4k0P7U_aftSZYYkg-UHaDRCnlqXACtAZBFsfZsoSCezvmMZBgxrd5RD_w',
    '_pan_': '2F9B282D12C50E12E2B88824FBDB0D42ADCB8D7EB2B5DC449C12BBC782CDB6893E47D95DCB9FA8595C3382737E0CB0AECF844C36E66DDA19E8F9C8C2C3D7B325424CF282D11423FBB73A17BCEAA3247A',
    'mba_muid': '1658391070137334238237',
    '__jd_ref_cls': 'elive_live_close_browser_pc',
    'RT': '"sl=0&ss=l9cdmsug&tt=0&z=1&dm=jd.com&si=0bwjzcnkgtlr&ld=3ffu&nu=cd2784a37d44147054c04fef26cbdb4b&cl=10m159&ul=33qtgv&hd=33qtjf"',
    'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IkRvQ3kyWVFsMWhhR29QRVVhRjRIIiwiaWF0IjoxNjY1OTcyMTkxLCJleHAiOjE2NjY1NzY5OTF9.kk-U0TYRhZp15LIxW9NBUH92dA2aie6MbmWa7T4Lqw4',
    'sso.jd.com': 'BJ.D16004BAC422F39EAC8BE3464FF6FE29.1420221020135942',
    'focus-team-id': '00046419',
    'focus-client': 'WEB',
    'focus-token': '2d1d330546bbf10c75a0400b00a0640a',
    'SSAID': 'e3b5099d6313d35fed4f2e982d823136019a248e30cb8a72bcad855a14492bef5fbbfe06ec48e2c97caa6d41b52b222efe258ceff1de846a187423db74f6192213a43e77a107603a87e695663dd6befbf08edc5116811be322dc75dfd45bf54a6d6d2a3f9d17d03b07be073b406ffba0197521c8e281fc9797a36a471eb15e8691f37eba0e4f5030693e6cc3875ba37f68b46b33022a92051b5e6874ae620b2eed53345c867dd185251c1da9e548bdc6a2bc78b4d1c85e5532425a96d95fd52c',
    '__jda': '26439548.1658391070137334238237.1658391070.1663223609.1666249460.248',
    '__jdc': '26439548',
    '__jdb': '26439548.7.1658391070137334238237|248.1666249460',
}

headers = {
    'Host': 'pre.dp.jd.com',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'Origin': 'http://pre.dp.jd.com',
    'Referer': 'http://pre.dp.jd.com/jbdpEdc/template-manage/template',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '__jdu=1658391070137334238237; pinId=lPhtT2OwOjs8udM_MW6XwbV9-x-f3wj7; shshshfpa=dd504387-bbe0-7d63-83de-21415b6ad26f-1662210772; shshshfpb=tsPxXKwLETUi0M5twG_PeCg; pin=jd_6f9e1931f53e5; unick=%E5%87%89%E7%94%9F%E7%9A%84%E5%89%91%E5%8D%A7%E8%96%AA%E5%B0%9D%E8%83%86; _tp=GuWTejsOX%2BEoD%2BLZp1eou%2BOX8kMoRcs8j9MgQxVIJFM%3D; _pst=jd_6f9e1931f53e5; user-key=762691c2-2cca-49fb-8340-4accc96c6ab0; __jdv=134439668|direct|-|none|-|1665727647642; PCSYCityID=CN_110000_110100_0; TrackID=18rG5IOHAY5x-ywTDTH7lG1AHxPoeHnQlKGri-XLHzwH2UJgxCy9tSKDYB39B1IV075qt25Hicf1LMsVe4ZOgTNG8gW_QTBUM-IqS6CyjVRFDYVk-NGb8ApOvselwoANI; ceshi3.com=103; cn=4; areaId=1; ipLoc-djd=1-2802-54745-0; mt_xid=V2_52007VwMVVlRaWloeTxhcB2EBEFdeWltZHU8pDABuBhRXXg9OCR1KHUAANwoTTlRQB1IDQEtaAWZXGgZbDAJcL0oYXwZ7AxNOXV5DWhZCGlUOZwIiUG1bYlkeTxFZAFcBGlBd; shshshfp=ef105dcfa173e3545719bf22b0b381d4; 3AB9D23F7A4B3C9B=TV4BCKDYZBPBL3M7HI5FKHLUPPAPYJJXWXKOFDLWS7Q2S45GJWCGDWA3QXOMNI4RYYSGPEGIHOUVLKUI5YTOC6CPUA; jd.erp.lang=zh_CN; jdd69fo72b8lfeoe=KNP7DSQOYN45PFCY7ZC5SVRACEKCHZMDFL7LR4QERN7QJTTZMZ3N2SZSMTVOVCC4F3WO5R2HPDIDX7YY4QZ3RBKJ3Q; logbook_u=ext.wanglei48; fp=c778e9a4228d63371715d7f0916acb8c; X-JACP-TOKEN=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJtb2JpbGUiOiIxODUwNjgzMjg1MCIsInVzZXJJZCI6ImV4dC53YW5nbGVpNDgiLCJlbWFpbCI6ImV4dC53YW5nbGVpNDhAamQuY29tIiwidXNlcm5hbWUiOiJleHQud2FuZ2xlaTQ4IiwiaWF0IjoxNjY2MTY0NjgzLCJpc3MiOiJ4aW5neXVuLmpkLmNvbSIsInN1YiI6InNzbyIsImV4cCI6MTY2NjI1MTA4M30.evBOMhb36xQQpgXSGL-1vUcu1T0YTi5YzPQmKcfKUFbAN7ZOsRtzOYcZ5DngEfjr-uK7n9mFWlV9G0MZ1b9WrtLcuUmTZqv_L-A-xgz8kU19DUhWXpqMxQ_EH0MAntfQP1EwhzEJioPF7lbpd0UclQmWCSsijRTEyq5Li_9VDribP9M8yA0L3RXGxwtStM7Osx6Ow-Z6-s5ixm8ZGFnSQ8eRsUTILg27R9uMmR3YM3dZ96nZjl2vKPBkNOIZQAAeOTAQmexOt9tcPUN09VfCTXEGIijOp4k0P7U_aftSZYYkg-UHaDRCnlqXACtAZBFsfZsoSCezvmMZBgxrd5RD_w; _pan_=2F9B282D12C50E12E2B88824FBDB0D42ADCB8D7EB2B5DC449C12BBC782CDB6893E47D95DCB9FA8595C3382737E0CB0AECF844C36E66DDA19E8F9C8C2C3D7B325424CF282D11423FBB73A17BCEAA3247A; mba_muid=1658391070137334238237; __jd_ref_cls=elive_live_close_browser_pc; RT="sl=0&ss=l9cdmsug&tt=0&z=1&dm=jd.com&si=0bwjzcnkgtlr&ld=3ffu&nu=cd2784a37d44147054c04fef26cbdb4b&cl=10m159&ul=33qtgv&hd=33qtjf"; token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IkRvQ3kyWVFsMWhhR29QRVVhRjRIIiwiaWF0IjoxNjY1OTcyMTkxLCJleHAiOjE2NjY1NzY5OTF9.kk-U0TYRhZp15LIxW9NBUH92dA2aie6MbmWa7T4Lqw4; sso.jd.com=BJ.D16004BAC422F39EAC8BE3464FF6FE29.1420221020135942; focus-team-id=00046419; focus-client=WEB; focus-token=2d1d330546bbf10c75a0400b00a0640a; SSAID=e3b5099d6313d35fed4f2e982d823136019a248e30cb8a72bcad855a14492bef5fbbfe06ec48e2c97caa6d41b52b222efe258ceff1de846a187423db74f6192213a43e77a107603a87e695663dd6befbf08edc5116811be322dc75dfd45bf54a6d6d2a3f9d17d03b07be073b406ffba0197521c8e281fc9797a36a471eb15e8691f37eba0e4f5030693e6cc3875ba37f68b46b33022a92051b5e6874ae620b2eed53345c867dd185251c1da9e548bdc6a2bc78b4d1c85e5532425a96d95fd52c; __jda=26439548.1658391070137334238237.1658391070.1663223609.1666249460.248; __jdc=26439548; __jdb=26439548.7.1658391070137334238237|248.1666249460',
}

json_data = {
    'relStatusList': [],
    'runStatusList': [],
    'pageStart': 1,
    'page': 1,
    'pageSize': 10,
}


# response = requests.post('http://pre.dp.jd.com/jbdpEdc/api/templateInChargeList', cookies=cookies, headers=headers, json=json_data)


class PreUser(HttpUser):
    host = 'http://pre.dp.jd.com'

    between(1, 2)

    def on_start(self):
        logger.info("开始测试！" + str(time.ctime()))

    def on_stop(self):
        logger.info("结束测试" + str(time.ctime()))

    @task
    def get_all(self):
        res = self.client.post("/jbdpEdc/api/templateInChargeList", cookies=cookies, headers=headers, json=json_data)
        logger.info(res.json)
        # print('--->' * 100)


"""
终端执行的headless模式:
locust -f locust_demo.py --headless  -u 5  -r 5 -t 5 --html report.html

#配置文件启动demo,要执行的文件:
locustfile = main.py
#测试host
host = 'http://pre.dp.jd.com'
#虚拟用户数
users = 100
#虚拟用户数增长率，例10个/s
spawn-rate = 10
# 持续运行的时间 together with –headless or –autostart. Defaults to run forever
run-time = 60s
#无webUI交互模式
headless = true
#当达到指定虚拟用户数时，重新进行统计
reset-stats = false
# 报告
--html = report.html


from locust import task, FastHttpUser

class MyUser(FastHttpUser):
    # 在Locust中，FastHttpUser类是用于替代HttpUser类的一种更高效的HTTP客户端实现。它使用geventhttpclient库代替requests库，以减少并发请求时的资源消耗，从而提高性能。
    host = 'www.baidu.com'
    @task
    def index(self):
        response = self.client.get('/')

"""
