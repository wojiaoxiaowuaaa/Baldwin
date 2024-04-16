# -*- coding:utf-8 -*-
from typing import Optional, Awaitable
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import tornado.ioloop
import random
from tornado import gen


# 起一个本地服务
class Index(RequestHandler):
    @gen.coroutine
    def get(self):
        yield gen.sleep(random.random() / 10)
        self.write("is xiawowu not xiaowu")


class About(RequestHandler):
    @gen.coroutine
    def get(self):
        yield gen.sleep(random.random() / 10 * 2)
        self.write("是小舞不是小武")


if __name__ == '__main__':
    """
     curl  http://0.0.0.0:9876/about
     curl  http://0.0.0.0:9876/index
    """
    app = tornado.web.Application([
        (r'/index', Index),
        (r'/about', About),
    ])
    app.listen(9876)
    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.current().stop()