import requests

# 代理服务器的配置
proxy_host = "114.104.134.200"
proxy_port = ""


# 定义请求函数
def send_request(url):
    # 设置代理
    session = requests.session()
    session.proxies = {
        "http": f"http://{proxy_host}:{proxy_port}",
        "https": f"http://{proxy_host}:{proxy_port}"
    }

    response = session.get(url)
    return response


# 示例调用
response = send_request("https://www.baidu.com")
print(response.text)
