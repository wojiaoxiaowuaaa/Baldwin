from sanic import Sanic
from sanic import response
import datetime
from loguru import logger

app = Sanic('my_app')

hello_requests_count = 0  # 全局变量 用于统计接口的请求次数


@app.get('/hello')
def handle_hello(request):
    time = str(datetime.datetime.now())[:-7]
    global hello_requests_count
    hello_requests_count += 1
    logger.info(f"接口的请求次数: {hello_requests_count}")
    return response.json({"hello time": time})


@app.get('/world')
def handle_world(request):
    time = str(datetime.datetime.now())[:-7]
    return response.json({"world time": time})


@app.post('/login')
def handle_login(request):
    time = str(datetime.datetime.now())[:-7]

    data = request.json
    logger.info(f"登录: {data}")
    if data:
        if data["username"] == "Tom" and data["password"] == "123456":
            return response.text("{} login success".format(data["username"]))
    else:
        return response.json({"login time": time})


@app.post('/logout')
def handle_logout(request):
    time = str(datetime.datetime.now())[:-7]
    data = request.json
    logger.info(f"登出: {data}")
    if data:
        if data["username"] == "Jim" and data["password"] == "456789":
            return response.text("{} logout success".format(data["username"]))
    else:
        return response.json({"logout time": time})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=7890, auto_reload=True)
