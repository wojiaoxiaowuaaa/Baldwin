import requests


class Send:
    # 初始化时创建session对象
    # 登录状态维持: 通过 requests.Session，代码能够维持登录状态，因为会话 cookie 会被自动管理。
    # 后续请求: 只要在同一个 Session 对象中发送请求，就可以保持登录状态，访问需要认证的资源。
    def __init__(self):
        self.session = requests.Session()

    # 登录方法
    def login(self, login_url, username, password, **kwargs):
        # 准备登录数据，这取决于具体网站的要求，这里仅为示例
        login_data = {"username": username, "password": password}
        # 发送登录请求
        response = self.session.post(login_url, data=login_data, **kwargs)
        # 检查登录是否成功，这里可以根据实际情况调整检查逻辑，比如检查响应状态码或返回的内容
        if response.status_code == 200:
            print("登录成功")
        else:
            print(f"登录失败，状态码：{response.status_code}")
            return False
        return True

    # 发送请求的方法，现在可以利用已登录的session
    def send_request(self, url="", method="get", **kwargs):
        response = self.session.request(method, url, **kwargs)
        print(f"状态码:{response.status_code}")
        return response


if __name__ == "__main__":
    # 实例化Send类
    sender = Send()

    # 尝试登录
    if sender.login("https://example.com/login", "your_username", "your_password"):
        # 登录成功后发送请求，这里以访问百度为例
        res = sender.send_request("https://www.baidu.com")
        print("登录后访问百度的响应内容:", res.text)
    else:
        print("无法继续，因登录失败。")
