import json
import requests


def func(city):
    url = f"http://openapi.xiaoxinhuan.com/Open/WeatherCityName?CityName={city}"
    headers = {
        "Content-Type": "application/json",
        "AppToken": "bd481f06d2e19accab48965ada3b8f14d66d02b78b345d67908e4dc8f9d8860aefe0ad391d8963586632c4cba89bf64a",
    }
    res = requests.post(url, headers=headers)
    res = json.dumps(res.json())  # 将Python字典转换为json字符串

    with open("./doc/demo.json", "w") as f:
        f.write(res)


if __name__ == "__main__":
    func("信阳")
