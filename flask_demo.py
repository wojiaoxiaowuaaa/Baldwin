from flask import Flask, request, jsonify

app = Flask(__name__)

"""request对象是来自于flask，是一个请求上下文对象,具有较高的隔离性,
flask的请求数据通过 request 对象来获取,
request对象中保存了一次HTTP请求的一切信息。

Request对象的重要属性如下所列：
form - 它是⼀个字典对象，包含表单参数及其值的键和值对。
args - 解析查询字符串的内容，它是浏览器问号"?"之后的URL的⼀部分。
"""


@app.route('/', methods=['get', 'post'])
def index(): pass


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

# 请求体:   键值对(表单)   文本(json/xml)  文件(图片/音频)

# 获取post键值对 -> request.form  类字典对象
# print(request.form.get('name'))

# 获取post文本数据 -> request.data / request.json
# print(request.data)  # 返回bytes类型
# print(request.json.get('age'))  # request.json直接将json字符串转为字典

# 获取post文件 -> request.files  类字典对象
# file = request.files.get("avatar")  # type: # FileStorage
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

# 获取原始的请求实数
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


if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)
