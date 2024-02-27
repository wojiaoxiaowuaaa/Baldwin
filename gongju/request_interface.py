import requests

headers = {
    "Content-Type": "application/json",
}


def register():
    url = 'http://127.0.0.1:9999/register'

    data = {"username": "wintest3", "password": "123456", "sex": "0", "telephone": "18708923490", "address": "美国德州"}

    response = requests.post(url=url, headers=headers, json=data)

    print("Status Code:", response.status_code, '\n\n', "Response Content:", response.json())


register()

"""
res = requests.post(url=url, headers=headers, json=data)
res = requests.post(url=url, headers=headers, data=data)

这两种写法涉及到`requests`库中的两种不同的请求体传递方式：`json` 和 `data`。

1. **`json=data`：**
   - 这种方式用于发送JSON格式的请求体，`requests`库会自动将Python对象（通常是字典）转换为JSON格式，并设置请求头的`Content-Type`为`application/json`。
   - 这样，服务器端通常会解析JSON数据，你可以在请求中直接传递Python字典，而无需手动将其转换为JSON字符串。

2. **`data=data`：**
   - 这种方式用于发送表单数据（`application/x-www-form-urlencoded`格式）。
   - 你需要手动将Python字典转换为表单数据格式（通常使用`urllib.parse.urlencode()`函数）并设置请求头的`Content-Type`为`application/x-www-form-urlencoded`。

```python
import requests
from urllib.parse import urlencode

url = "https://example.com/api"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
data = {"key1": "value1", "key2": "value2"}

res = requests.post(url=url, headers=headers, data=urlencode(data))
```

选择使用哪种方式取决于你要与服务器交互的方式。如果你需要发送JSON数据，使用`json=data`方式更为简便，而如果需要发送表单数据，使用`data=data`方式是常见的做法。
"""
