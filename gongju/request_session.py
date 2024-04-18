import requests


class Send:
    # 后续的请求使用同一个会话对象 session，它会自动携带登录后的 Cookie，从而保持登录状态。通过使用会话对象，你可以在多个请求中保持登录状态，无需在每个请求中都重新登录。
    session = requests.session()

    def __init__(self):
        print(dir(Send.session))

    @staticmethod
    def send_request(url="", method="get", **kwargs):
        res = Send.session.request(method, url,  **kwargs)
        print(f"状态码:{res.status_code}")
        return res


if __name__ == '__main__':
    res = Send.send_request("https://www.baidu.com")
    # s = Send()
    # print(res.content)
