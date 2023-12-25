import requests

url = " http://127.0.0.1:9999/login?name=xiaowu&pwd=111"

payload = {}
files = {}
headers = {"User-Agent": "Apifox/1.0.0 (https://apifox.com)"}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
