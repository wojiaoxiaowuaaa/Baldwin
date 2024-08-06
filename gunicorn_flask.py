from flask import Flask
from gunicorn.app.base import BaseApplication


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


class FlaskApplication(BaseApplication):
    """使用Gunicorn作为WSGI服务器来部署一个Flask应用.构造函数接收一个Flask应用实例和一个可选的配置字典. super()调用父类的构造函数,初始化基类."""

    def __init__(self, app, options=None):
        self.application = app
        self.options = options or {}
        super().__init__()

    def load_config(self):
        """子类重写父类的抽象方法 load_config方法负责从options字典中加载Gunicorn的配置.它遍历字典,只选取那些在self.cfg.settings中存在的键,并且值不为None的项,然后将它们设置到Gunicorn的配置中."""
        config = {
            key: value
            for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        """子类重写父类的抽象方法 load方法返回Flask应用实例 Gunicorn 将使用这个实例来处理HTTP请求"""
        return self.application


if __name__ == "__main__":
    """定义Gunicorn的配置字典options,指定了服务器应该绑定的地址和端口以及工作进程的数量.然后创建一个FlaskApplication实例,并调用run方法来启动Gunicorn服务器.这种方式允许你以编程的方式控制Gunicorn的启动,这对于自动化部署和脚本化管理非常有用."""
    options = {
        "bind": "0.0.0.0:8000",  # 绑定的地址和端口号
        "workers": 4,  # 工作进程数量
    }
    FlaskApplication(app, options).run()
