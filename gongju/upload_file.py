import os
import requests


def upload_file(url, pwd):
    with open(
        pwd, "rb"
    ) as f:  # 以二进制模式 ('rb') 打开文件,确保文件以字节流的形式读取,这对于上传文件是必要的.f是一个文件对象<_io.BufferedReader name='/Users/wl/Desktop/stork.py'>
        res = requests.post(
            url, files={"file": f}
        )  # requests上传文件.files 参数用于上传文件,{"file": f} 创建了字典,其中键 "file" 是上传文件的字段名,值 f 是文件对象.
    return res.text


# 上传文件时,服务器必须支持文件上传,并正确处理 multipart/form-data 类型的请求.
# print(upload_file('http://httpbin.org/post', os.path.abspath(__file__)))
print(upload_file("http://127.0.0.1:5000/upload", os.path.abspath(__file__)))


# from flask import Flask, request
#
# app = Flask(__name__)
#
# @app.route('/upload', methods=['POST'])
# def upload():
#     file = request.files['file']
#     from loguru import logger
#     logger.info(file)
#     logger.info(dir(file))
#     if file:
#         file.save('./uploads/' + file.filename)
#         return '文件上传成功'
#     else:
#         return '未找到文件'
#
# if __name__ == '__main__':
#     app.run()
