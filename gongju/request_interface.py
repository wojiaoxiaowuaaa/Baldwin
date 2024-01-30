import requests

headers = {
    "Content-Type": "application/json",
}


def login():
    url = "http://127.0.0.1:9999/login?username=wintest3&password=123456"

    response = requests.post(url=url, headers=headers)

    print("Status Code:", response.status_code, '\n\n', "Response Content:", response.json())


def register():
    url = 'http://127.0.0.1:9999/register'

    data = {"username": "wintest3", "password": "123456", "sex": "0", "telephone": "18708923490", "address": "美国德州"}

    response = requests.post(url=url, headers=headers, json=data)

    print("Status Code:", response.status_code, '\n\n', "Response Content:", response.json())


login()
register()