import requests

proxies = {
    # 该代理服务器在免费代理网站上得到的，这样的网站有很多  http://www.66ip.cn/
    'http': 'http://223.94.85.131:9091',
    'http': 'http://138.68.75.207:80'
}

try:
    response = requests.get('http://httpbin.org/get', proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)
