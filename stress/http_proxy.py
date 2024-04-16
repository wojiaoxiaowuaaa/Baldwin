import requests

proxies = {
    # 该代理服务器在免费代理网站上得到的，这样的网站有很多 ，可以自己搜索
    'http://': 'http://114.104.134.200',
    'http://': 'http://27.158.8.11'
}

try:
    response = requests.get('http://httpbin.org/get', proxies=proxies)
    print(response.json())  # <class 'dict'>
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)
