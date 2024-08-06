"""
curl -X POST "http://127.0.0.1:5000/platform" -H "Content-Type: application/json" -d '{"name": "Sample Item", "description": "This is a sample item", "price": 10.5, "platform": "iOS"}'

request对象是来自于flask,是一个请求上下文对象,具有较高的隔离性,flask的请求数据通过 request 对象来获取,request对象中保存了一次HTTP请求的一切信息.使得开发者可以方便地访问客户端发送过来的数据.以下是request对象的一些关键属性和方法:
属性
form:一个字典,包含了POST请求中的表单数据(或者PUT、PATCH请求体中编码为application/x-www-form-urlencoded或multipart/form-data的数据).例如,如果用户提交了一个表单,你可以通过request.form['username']来获取表单中的用户名字段.
args:一个字典,包含了URL中的查询参数.例如,对于URL http://example.com/search?q=query+string,可以通过request.args.get('q')获取到query string.
json:如果请求包含了JSON数据(Content-Type为application/json),这个属性会提供一个字典,内容为JSON解码后的数据.如果请求没有JSON数据或Content-Type不匹配,访问这个属性会引发一个异常.
data:原始请求体数据,对于非表单的POST请求很有用,如上传文件或自定义格式的数据.
files:一个字典,包含了上传的文件.键是表单字段名,值是FileStorage对象.
method:一个字符串,表示HTTP请求方法(如GET、POST等).
headers:一个EnvironHeaders对象,提供了访问请求头的方法,如request.headers['User-Agent'].
cookies:一个字典,包含了请求中的cookies.
url:请求的完整URL.
base_url:没有查询字符串的URL基础部分.
path:请求的路径部分,不包括查询字符串.

方法
get_json(force=False, silent=False):尝试从请求中解析JSON数据.如果force=True,即使Content-Type不是application/json也会尝试解析.silent=True时,解析失败时不抛出异常,而是返回None.
get_data(cache=True, as_text=False):获取请求的数据.cache=True时,数据只被读取一次并缓存.as_text=True时,如果数据是字节流,则尝试解码为UTF-8字符串返回.
"""

from flask import Flask, request, jsonify, make_response
from loguru import logger

app = Flask(__name__)


@app.route("/platform", methods=["POST"])
def get_platform():
    # 从请求入参的JSON数据中获取platform字段,并去除首尾空格.如果请求的入参中不包含platform字段,则默认返回空字符串
    platform = request.json.get("platform", "").strip()

    logger.info(request.headers)

    return make_response(
        {"message": "This is a complex response", "platform": platform}, 200
    )


if __name__ == "__main__":
    app.run(debug=True)  # app.run('0.0.0.0', port=8080, debug=True)

# 获取请求的基础数据
# print(request.url)  # 请求的URL
# print(request.method)  # 本次请求的请求方式
# print(request.headers)  # 获取请求头信息  类字典对象

# print(request.headers['Host'])
# print(request.headers.get('Host'))  # 建议使用get方法, 键不存在不报错

# 请求传递数据 1> URL路径 -> 路由变量  2> 查询字符串 get  3> 请求体  post  4> 请求头 -> request.headers

# 获取查询字符串 -> request.args  xx?name=zs&age=20  类字典对象
# print(request.args.get('name'))
# print(request.args.get('age'))

# 请求体:键值对(表单)   文本(json/xml)  文件(27149/音频)

# 获取post键值对 -> request.form  类字典对象
# print(request.form.get('name'))

# 获取post文本数据 -> request.data / request.json
# print(request.data)  # 返回bytes类型
# print(request.json.get('age'))  # request.json直接将json字符串转为字典

# 获取post文件 -> request.files  类字典对象
# file = request.files.get("avatar")  # type: FileStorage
# print(type(file))  # 返回 FileStorage文件对象
# 将文件保存到本地
# file.save('123.jpg')

# 获取文件的二进制数据
# img_bytes = file.read()
# print(img_bytes)

# data = request.get_json()
# name = data.get('name')
# age = data.get('age')
# print(f'Name: {name}, Age: {age}')

# 获取原始请求实数
# data = request.data


# @app.route("/upload", methods=["POST", "GET"])
# def upload():
#     if request.method == "GET":
#         return render_template("upload.html")
#     elif request.method == "POST":
#         files = request.files
#         if "file" not in files:
#             return json.dumps({"code": 1, "msg": "上传失败"})
#         file = files.get("file")
#         file.save("./static/upload/" + file.filename)
#         return json.dumps({"code": 0, "msg": "上传成功"})
