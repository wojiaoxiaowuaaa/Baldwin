import json
import requests


def func(city):
    url = f"http://openapi.xiaoxinhuan.com/Open/WeatherCityName?CityName={city}"

    headers = {
        "Content-Type": "application/json",
        "AppToken": "bd481f06d2e19accab48965ada3b8f14d66d02b78b345d67908e4dc8f9d8860aefe0ad391d8963586632c4cba89bf64a",
    }

    res = requests.post(url, headers=headers)

    print(res.text)  # 这里拿到的就是json字符串  如果使用res.json()则拿到的是Python字典

    with open("demo.json", "w") as f:
        # 这里必须写入字符串格式内容,尝试写入字典会报错 TypeError: write() argument must be str, not dict
        f.write(res.text)


if __name__ == "__main__":
    func("北京")
