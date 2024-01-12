import json
import flask
from flask import request

"""
flask:web框架,通过flask提供的装饰器@server.route()将普通函数转换为服务
"""
# 创建一个服务，把当前这个python文件当做一个服务
server = flask.Flask(__name__)


# @server.route()可以将普通函数转变为服务. 登录接口的路径、请求方式.
@server.route("/login", methods=["get", "post"])
def login():
    # 获取通过url请求传参的数据
    username = request.values.get("name")
    # 获取url请求传的密码，明文.
    pwd = request.values.get("pwd")
    # 判断用户名、密码都不为空，如果不传用户名、密码则username和pwd为None
    if username and pwd:
        if username == "xiaowu" and pwd == "111":
            resu = {"code": 200, "message": "登录成功"}
            # 将字典转换为json串, json是字符串
            return json.dumps(resu, ensure_ascii=False)
        else:
            resu = {"code": -1, "message": "账号密码错误"}
            return json.dumps(resu, ensure_ascii=False)
    else:
        resu = {"code": 10001, "message": "参数不能为空！"}
        return json.dumps(resu, ensure_ascii=False)


if __name__ == "__main__":
    # 指定端口、host,0.0.0.0代表不管几个网卡，任何ip都可以访问
    server.run(debug=True, port=9999, host="0.0.0.0")

"""
import requests


def func(uri):
    data = {
        'name': 'xiaowu',
        'pwd': '111'
    }
    res = requests.get(uri, data)
    print(res.json())  # {'code': 200, 'message': '登录成功'}


url = 'http://127.0.0.1:9999/login'
func(url)

"""
