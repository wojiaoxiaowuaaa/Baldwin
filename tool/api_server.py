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

---------------------------------------------------------------------------------------
from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    '''文件上传服务器'''
    file = request.files['file']
    from loguru import logger
    logger.info(file)
    if file:
        file.save('./uploads/' + file.filename)
        return '文件上传成功'
    else:
        return '未找到文件'

if __name__ == '__main__':
    app.run()

---------------------------------------------------------------------------------------
import os
import requests


def upload_file(url, pwd):
    with open(pwd, "rb") as f:  # 以二进制模式 ('rb') 打开文件,确保文件以字节流的形式读取,这对于上传文件是必要的.f是一个文件对象<_io.BufferedReader name='/Users/wl/Desktop/stork.py'>
        res = requests.post(url, files={"file": f})  # requests上传文件.files 参数用于上传文件,{"file": f} 创建了字典,其中键 "file" 是上传文件的字段名,值 f 是文件对象.
    return res.text

---------------------------------------------------------------------------------------
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

---------------------------------------------------------------------------------------
# 上传文件脚本
import requests
from pathlib import Path

files = {"file": open(Path(__file__), 'rb')}  # os.path.abspath(__file__)也能代表当前文件路径
# print(files)  # {'file': <_io.BufferedReader name='/Users/wl/stork.py'>}
res = requests.post("http://127.0.0.1:5000/upload", files=files)
print(res.text)

#  request对象中包含的属性
['__annotations__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_cached_json', '_get_file_stream', '_get_stream_for_parsing', '_load_form_data', '_parse_content_type', '_parsed_content_type', 'accept_charsets', 'accept_encodings', 'accept_languages', 'accept_mimetypes', 'access_control_request_headers', 'access_control_request_method', 'access_route', 'application', 'args', 'authorization', 'base_url', 'blueprint', 'blueprints', 'cache_control', 'close', 'content_encoding', 'content_length', 'content_md5', 'content_type', 'cookies', 'data', 'date', 'dict_storage_class', 'endpoint', 'environ', 'files', 'form', 'form_data_parser_class', 'from_values', 'full_path', 'get_data', 'get_json', 'headers', 'host', 'host_url', 'if_match', 'if_modified_since', 'if_none_match', 'if_range', 'if_unmodified_since', 'input_stream', 'is_json', 'is_multiprocess', 'is_multithread', 'is_run_once', 'is_secure', 'json', 'json_module', 'list_storage_class', 'make_form_data_parser', 'max_content_length', 'max_form_memory_size', 'max_form_parts', 'max_forwards', 'method', 'mimetype', 'mimetype_params', 'on_json_loading_failed', 'origin', 'parameter_storage_class', 'path', 'pragma', 'query_string', 'range', 'referrer', 'remote_addr', 'remote_user', 'root_path', 'root_url', 'routing_exception', 'scheme', 'script_root', 'server', 'shallow', 'stream', 'trusted_hosts', 'url', 'url_root', 'url_rule', 'user_agent', 'user_agent_class', 'values', 'view_args', 'want_form_data_parsed']
"""

from flask import Flask, request, redirect, url_for, send_from_directory, render_template_string
from loguru import logger
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER): os.makedirs(UPLOAD_FOLDER)


def allowed_file(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template_string('''<!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>''')


@app.route('/', methods=['POST'])
def upload_file():
    # logger.info(request.files)  # ImmutableMultiDict([('file', <FileStorage: '02取换电派单格口.txt' ('text/plain')>)])
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    # logger.info(file)  # <FileStorage: '02取换电派单格口.txt' ('text/plain')>
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file', filename=filename))
    return redirect(request.url)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(debug=True)
