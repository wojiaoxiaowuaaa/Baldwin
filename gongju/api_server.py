import json
import flask
from flask import request
from loguru import logger

# 创建一个服务 把当前这个python文件当做一个服务
# __name__ 是一个特殊变量，在 Python 模块中，它的值取决于模块是被直接运行还是被导入。如果模块是被直接运行的（即作为主程序执行），__name__ 的值是 '__main__'。如果模块是被另一个模块导入的，__name__ 的值是模块的名字（即模块的文件名，不包括扩展名）。
app = flask.Flask(__name__)


# 通过flask提供的装饰器 可以将普通函数转变为服务. 登录接口的路径、请求方式.
@app.route("/login", methods=["get", "post"])
def login():
    # 获取通过url请求传参的数据
    # curl  http://172.23.224.120:9999/login?name=xiaowu&pwd=111
    username = request.values.get("name")
    # 获取url请求传的密码，明文.
    pwd = request.values.get("pwd")
    # logger.info(f"username: {username}, pwd: {pwd}")
    if username and pwd:
        if username == "xiaowu" and pwd == "111":
            resu = {"code": 200, "message": "登录成功"}
            # 将字典转换为json串, json是字符串.
            return json.dumps(resu, ensure_ascii=False)
        else:
            resu = {"code": -1, "message": "账号密码错误"}
            return json.dumps(resu, ensure_ascii=False)
    else:
        resu = {"code": 10001, "message": "参数不能为空！"}
        return json.dumps(resu, ensure_ascii=False)


if __name__ == "__main__":
    # 指定端口、host,0.0.0.0代表不管几个网卡，任何ip都可以访问
    app.run(debug=True, port=9999, host="0.0.0.0")

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
