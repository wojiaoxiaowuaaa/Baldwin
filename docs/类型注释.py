from typing import Union

def fetch_data(url: str) -> Union[Response, None, bytes, dict]:    # noqa: F821
    try:
        response = requests.get(url)    # noqa: F821
        if response.status_code == 200:
            # 根据内容类型返回不同的结果
            if response.headers['Content-Type'] == 'application/json':
                return response.json()  # 返回字典
            elif response.headers['Content-Type'] == 'application/octet-stream':
                return response.content  # 返回字节序列
            else:
                return response  # 返回Response对象
        else:
            return None  # 返回None表示请求失败
    except Exception as e:
        print(f"An error occurred: {e}")
        return None  # 返回None表示发生异常

