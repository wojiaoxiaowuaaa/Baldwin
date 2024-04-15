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
