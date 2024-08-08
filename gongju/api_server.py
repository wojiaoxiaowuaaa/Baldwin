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

---------------------------------------------------------------------------------------
from sanic import Sanic, json
from time import ctime
# 创建 Sanic 应用程序
app = Sanic("CodeToAPI")


@app.route('/')
async def index(request):
    data = {'current time': f'{ctime()}'}
    return json(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

---------------------------------------------------------------------------------------
import os
import requests

# 上传文件
def upload_file(url, pwd):
    with open(pwd, "rb") as f:  # 以二进制模式 ('rb') 打开文件,确保文件以字节流的形式读取,这对于上传文件是必要的.f是一个文件对象<_io.BufferedReader name='/Users/wl/Desktop/stork.py'>
        res = requests.post(url, files={"file": f})  # requests上传文件.files 参数用于上传文件,{"file": f} 创建了字典,其中键 "file" 是上传文件的字段名,值 f 是文件对象.
    return res.text


# 上传文件时,服务器必须支持文件上传,并正确处理 multipart/form-data 类型的请求.
# print(upload_file('http://httpbin.org/post', os.path.abspath(__file__)))
print(upload_file("http://127.0.0.1:5000/upload", os.path.abspath(__file__)))


---------------------------------------------------------------------------------------
from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    '''文件上传服务器'''
    file = request.files['file']
    from loguru import logger
    logger.info(file)
    logger.info(dir(file))
    if file:
        file.save('./uploads/' + file.filename)
        return '文件上传成功'
    else:
        return '未找到文件'

if __name__ == '__main__':
    app.run()

"""

import json
import flask
from flask import request
from loguru import logger

# 创建一个服务 把当前这个python文件当做一个服务
# __name__ 是一个特殊变量,在 Python 模块中,它的值取决于模块是被直接运行还是被导入.如果模块是被直接运行的(即作为主程序执行),__name__ 的值是 '__main__'.如果模块是被另一个模块导入的,__name__ 的值是模块的名字(即模块的文件名,不包括扩展名).
app = flask.Flask(__name__)


# 通过flask提供的装饰器 可以将普通函数转变为服务
@app.route("/login", methods=["get", "post"])
def login():
    # 获取通过url请求传参的数据
    # curl  http://172.23.224.120:9999/login?name=xiaowu&pwd=111
    username = request.values.get("name")
    # 获取url请求传的密码,明文.
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
        resu = {"code": 10001, "message": "参数不能为空!"}
        return json.dumps(resu, ensure_ascii=False)


if __name__ == "__main__":
    # 指定端口、host,0.0.0.0代表不管几个网卡,任何ip都可以访问
    app.run(debug=True, port=9999, host="0.0.0.0")
