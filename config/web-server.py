#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#
#   Author  :   XueWeiHan
#   E-mail  :   595666367@qq.com
#   Date    :   2022-03-29 16:56
#   Desc    :   迷你 Web 服务器
import sys
import socket
import selectors
import datetime
import time
import html

# 默认错误信息 HTML 模版
DEFAULT_ERROR_MESSAGE = """\
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
        "http://www.w3.org/TR/html4/strict.dtd">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
        <title>Error response</title>
    </head>
    <body>
        <h1>Error response</h1>
        <p>Error code: %(code)d</p>
        <p>Message: %(message)s.</p>
        <p>Error code explanation: %(code)s - %(explain)s.</p>
    </body>
</html>
"""


# 处理连接 进行数据通信
class HTTPServer(object):
    def __init__(self, server_address, RequestHandlerClass):
        self.server_address = server_address
        self.RequestHandlerClass = RequestHandlerClass
        self.request_queue_size = 5
        self.__shutdown_request = False
        # 创建 TCP Socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            # 绑定 socket 和端口
            self.server_bind()
            # 开始监听端口
            self.server_activate()
        except:
            #  关闭 socket
            #  解释器会在执行 __init__() 方法时，根据函数名查找该方法的定义，并在运行时动态调用。因此，即使 server_close() 方法的定义在 __init__() 方法的后面，也不会影响在 __init__() 方法中对其的调用。
            self.server_close()
            raise

    def server_bind(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定端口
        self.socket.bind(self.server_address)

    def server_activate(self):
        # 监听端口
        self.socket.listen(self.request_queue_size)

    def server_close(self):
        # 关闭socket
        self.socket.close()

    def fileno(self):
        """
        返回 socket 文件号
        用于 select 监控文件句柄状态
        """
        return self.socket.fileno()

    def serve_forever(self, poll_interval=0.5):
        """
        服务器启动入口
        """

        with selectors.SelectSelector() as selector:
            # 基于 select 轮询获取已准备好的可读句柄
            selector.register(self, selectors.EVENT_READ)
            while True:
                ready = selector.select(poll_interval)
                if ready:
                    # 有准备好的可读文件句柄，则与客户端的链接建立完毕 可以进行下一步
                    self._handle_request_noblock()

    def _handle_request_noblock(self):
        """
        处理请求
        """
        try:
            # 接收来自客户端的请求：request 对象
            request, client_address = self.get_request()
        except socket.error:
            return
        try:
            # 开始处理请求
            self.process_request(request, client_address)
        except:
            self.handle_error(client_address)
            self.shutdown_request(request)

    def get_request(self):
        # 接收请求
        return self.socket.accept()

    def process_request(self, request, client_address):
        # 处理请求
        self.finish_request(request, client_address)
        self.shutdown_request(request)

    def finish_request(self, request, client_address):
        # 调用处理请求的类
        self.RequestHandlerClass(request, client_address, self)

    def shutdown_request(self, request):
        try:
            # 后续不允许发送和接收
            request.shutdown(socket.SHUT_WR)
        except socket.error:
            pass  # some platforms may raise ENOTCONN here
        # 结束请求
        request.close()

    def handle_error(self, client_address):
        print('-' * 40, file=sys.stderr)
        print('Exception occurred during processing of request from', client_address, file=sys.stderr)
        import traceback
        traceback.print_exc()
        print('-' * 40, file=sys.stderr)


# 处理请求
class HTTPRequestHandler(object):
    responses = {
        100: ('Continue', 'Request received, please continue'),
        101: ('Switching Protocols',
              'Switching to new protocol; obey Upgrade header'),

        200: ('OK', 'Request fulfilled, document follows'),
        201: ('Created', 'Document created, URL follows'),
        202: ('Accepted',
              'Request accepted, processing continues off-line'),
        203: ('Non-Authoritative Information', 'Request fulfilled from cache'),
        204: ('No Content', 'Request fulfilled, nothing follows'),
        205: ('Reset Content', 'Clear input form for further input.'),
        206: ('Partial Content', 'Partial content follows.'),

        300: ('Multiple Choices',
              'Object has several resources -- see URI list'),
        301: ('Moved Permanently', 'Object moved permanently -- see URI list'),
        302: ('Found', 'Object moved temporarily -- see URI list'),
        303: ('See Other', 'Object moved -- see Method and URL list'),
        304: ('Not Modified',
              'Document has not changed since given time'),
        305: ('Use Proxy',
              'You must use proxy specified in Location to access this '
              'resource.'),
        307: ('Temporary Redirect',
              'Object moved temporarily -- see URI list'),

        400: ('Bad Request',
              'Bad request syntax or unsupported method'),
        401: ('Unauthorized',
              'No permission -- see authorization schemes'),
        402: ('Payment Required',
              'No payment -- see charging schemes'),
        403: ('Forbidden',
              'Request forbidden -- authorization will not help'),
        404: ('Not Found', 'Nothing matches the given URI'),
        405: ('Method Not Allowed',
              'Specified method is invalid for this resource.'),
        406: ('Not Acceptable', 'URI not available in preferred format.'),
        407: ('Proxy Authentication Required', 'You must authenticate with '
                                               'this proxy before proceeding.'),
        408: ('Request Timeout', 'Request timed out; try again later.'),
        409: ('Conflict', 'Request conflict.'),
        410: ('Gone',
              'URI no longer exists and has been permanently removed.'),
        411: ('Length Required', 'Client must specify Content-Length.'),
        412: ('Precondition Failed', 'Precondition in headers is false.'),
        413: ('Request Entity Too Large', 'Entity is too large.'),
        414: ('Request-URI Too Long', 'URI is too long.'),
        415: ('Unsupported Media Type', 'Entity body in unsupported format.'),
        416: ('Requested Range Not Satisfiable',
              'Cannot satisfy request range.'),
        417: ('Expectation Failed',
              'Expect condition could not be satisfied.'),

        500: ('Internal Server Error', 'Server got itself in trouble'),
        501: ('Not Implemented',
              'Server does not support this operation'),
        502: ('Bad Gateway', 'Invalid responses from another server/proxy.'),
        503: ('Service Unavailable',
              'The server cannot process the request due to a high load'),
        504: ('Gateway Timeout',
              'The gateway server did not receive a timely response'),
        505: ('HTTP Version Not Supported', 'Cannot fulfill request.'),
    }

    def __init__(self, request, client_address, server):
        self.request = request
        self.client_address = client_address
        self.server = server
        self.protocol_version = "HTTP/1.0"
        self.setup()
        try:
            self.handle()
        finally:
            self.finish()

    def setup(self):
        self.connection = self.request
        # 初始化请求和响应的文件句柄
        self.rfile = self.connection.makefile('rb', -1)
        self.wfile = self.connection.makefile('wb', 0)

    def handle(self):
        try:
            # 设置请求体限制：65536
            self.raw_requestline = self.rfile.readline(65537)
            # 如果超过限制则返回 414 HTTP code
            if len(self.raw_requestline) > 65536:
                self.requestline = ''
                self.request_version = ''
                self.command = ''
                self.send_error(414)
                return
            # 解析 HTTP 请求，并把值通过 self 属性传递
            if not self.parse_request():
                return
            # 具体处理请求的方法 do_方法，比如：do_get、do_post
            mname = ('do_' + self.command).lower()
            if not hasattr(self, mname):
                self.send_error(501, "Unsupported method (%r)" % self.command)
                return
            method = getattr(self, mname)
            # 对应到具体的处理 HTTP method 的方法
            method()
            # 返回响应
            self.wfile.flush()
        except socket.timeout as e:
            self.log_error("Request timed out: %r", e)
            return

    def finish(self):
        if not self.wfile.closed:
            try:
                self.wfile.flush()
            except socket.error:
                pass
        # 关闭请求和响应的句柄
        self.wfile.close()
        self.rfile.close()

    def parse_request(self):
        """
        解析 HTTP 请求
        """
        self.command = None  # set in case of error on the first line
        self.request_version = version = "HTTP/1.0"
        # 开始解析 HTTP 请求，数据格式如下：
        """
        {HTTP method} {PATH} {HTTP version}\r\n
        {header field name}:{field value}\r\n
        ...
        \r\n
        {request body}
        """
        # 解析请求头
        requestline = str(self.raw_requestline, 'iso-8859-1')
        requestline = requestline.rstrip('\r\n')
        self.requestline = requestline
        words = requestline.split()
        if len(words) == 3:
            # HTTP method, PATH, HTTP version
            command, path, version = words
            if version[:5] != 'HTTP/':
                self.send_error(400, "Bad request version (%r)" % version)
                return False
            # 检查 HTTP version 正确性
            try:
                base_version_number = version.split('/', 1)[1]
                version_number = base_version_number.split(".")
                if len(version_number) != 2:
                    raise ValueError
                version_number = int(version_number[0]), int(version_number[1])
                if version_number >= (2, 0):
                    self.send_error(
                        505, "Invalid HTTP Version (%s)" % base_version_number)
                    return False
            except (ValueError, IndexError):
                self.send_error(400, "Bad request version (%r)" % version)
                return False

        elif len(words) == 2:
            # 如果没有 HTTP version 则使用默认版本即：HTTP/1.0
            command, path = words
        elif not words:
            return False
        else:
            self.send_error(400, "Bad request syntax (%r)" % requestline)
            return False

        self.command, self.path, self.request_version = command, path, version

        # 解析 header，仅做解析
        self.headers = self.parse_headers()
        return True

    def parse_headers(self):
        headers = {}
        while True:
            line = self.rfile.readline()
            if line in (b'\r\n', b'\n', b''):
                break
            line_str = str(line, 'utf-8')
            key, value = line_str.split(': ')
            headers[key] = value.strip()
        return headers

    def log_message(self, format, *args):
        log_data_time_string = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        sys.stderr.write("%s - - [%s] %s\n" %
                         (self.client_address[0],
                          log_data_time_string,
                          format % args))

    def log_request(self, code='-', size='-'):
        self.log_message('"%s" %s %s',
                         self.requestline, str(code), str(size))

    def log_error(self, format, *args):
        self.log_message(format, *args)

    def send_error(self, code, message=None):
        """
        返回异常响应 code+message
        """
        try:
            short, long = self.responses[code]
        except KeyError:
            short, long = '???', '???'
        if message is None:
            message = short
        explain = long
        self.log_error("code %d, message %s", code, message)
        self.send_response(code, message)

        content = None
        # 状态码大于 200，并且不是 204、205、304 为异常
        if code > 200 and code not in (204, 205, 304):
            content = (DEFAULT_ERROR_MESSAGE % {
                'code': code,
                'message': html.escape(message),
                'explain': explain
            })
            self.send_header("Content-Type", "text/html;charset=utf-8")
        self.end_headers()
        body = content.encode('UTF-8', 'replace')
        if self.command != 'HEAD' and content:
            # 返回响应
            self.wfile.write(body)

    def send_response(self, code, message=None):
        self.log_request(code)
        if message is None:
            if code in self.responses:
                message = self.responses[code][0]
            else:
                message = ''
        # 响应体格式
        """
        {HTTP version} {status code} {status phrase}\r\n
        {header field name}:{field value}\r\n
        ...
        \r\n
        {response body}
        """
        # 写响应头
        self.wfile.write(("%s %d %s\r\n" %
                          (self.protocol_version, code, message)).encode(
            'latin-1', 'strict'))
        self.send_header('Server', "HG/Python " + sys.version.split()[0])
        # 写响应 header
        self.send_header('Date', self.date_time_string())

    def send_header(self, keyword, value):
        self.wfile.write(("%s: %s\r\n" % (keyword, value)).encode('latin-1', 'strict'))

    def end_headers(self):
        # header 结束的标识符
        self.wfile.write(b"\r\n")

    @staticmethod
    def date_time_string(timestamp=None):
        weekdayname = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

        monthname = [None, 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
                     'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        if timestamp is None:
            timestamp = time.time()
        year, month, day, hh, mm, ss, wd, y, z = time.gmtime(timestamp)
        s = "%s, %02d %3s %4d %02d:%02d:%02d GMT" % (
            weekdayname[wd],
            day, monthname[month],
            year, hh, mm, ss)
        return s


# 请求具体的处理方式
class RequestHandler(HTTPRequestHandler):
    def handle_index(self):
        page = '''
        <html>
        <body>
        <p>你好, HG Web Server!</p>
        </body>
        </html>
        '''
        self.send_response(200)  # status code
        # 试试删除这行
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(page)))
        self.end_headers()
        self.wfile.write(page.encode('utf-8'))

    def handle_favicon(self):
        page = '''
        <html>
        <body>
        <p>这里还未开发</p>
        </body>
        </html>
        '''
        self.send_response(200)  # status code
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(page)))
        self.end_headers()
        self.wfile.write(page.encode('utf-8'))

    def handle_about(self):
        page = '''
        <html>
        <body>
        <p>This is the about page!</p>
        </body>
        </html>
        '''
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(page)))
        self.end_headers()
        self.wfile.write(page.encode('utf-8'))

    # 处理 GET 请求
    def do_get(self):
        # 根据 path 对应到具体的处理方法
        if self.path == '/':
            self.handle_index()
        elif self.path.startswith('/favicon'):
            self.handle_favicon()
        elif self.path == '/handle_about':
            self.handle_about()
        else:
            self.send_error(404)


if __name__ == '__main__':
    server = HTTPServer(('', 8080), RequestHandler)
    # 启动服务 curl http://172.23.224.120:8080/handle_about
    server.serve_forever()


"""
这里的服务与 Flask 后端服务之间有一些区别，主要包括实现原理、功能和复杂度等方面。让我们详细来看一下：
实现原理：
这个脚本中的服务器是基于底层的 socket 编程实现的，使用了 Python 的 socket 和 selectors 模块来手动管理连接和数据交换。
Flask 后端服务则是建立在 WSGI（Web Server Gateway Interface）规范之上的，它是一个高层次的 Web 框架，抽象了底层的网络通信细节，提供了简单易用的 API 来处理 HTTP 请求和响应。

功能：
这个脚本中的服务器实现了一个简单的 HTTP 服务器，能够接收客户端的连接请求，并根据请求的路径返回相应的内容。它是一个基础的服务器框架，需要自行实现请求的解析和处理逻辑。
Flask 后端服务提供了丰富的功能和扩展，包括路由、模板引擎、请求/响应处理、中间件、数据库集成等，可以快速构建复杂的 Web 应用。

复杂度：
这个脚本中的服务器相对于 Flask 后端服务来说，实现了基本的 HTTP 服务器功能，但是需要手动处理连接、请求解析、响应生成等细节，代码相对复杂。
Flask 后端服务提供了高度封装的 API 和简单易用的框架结构，可以用少量的代码快速构建一个功能完善的 Web 服务。它隐藏了底层的网络通信细节，让开发者能够专注于业务逻辑的实现。
综上所述，虽然这个脚本中的服务器和 Flask 后端服务都可以用来构建 Web 服务，但它们的实现原理、功能和复杂度有所不同。选择哪种方式取决于项目的需求和开发者的技术栈，如果需要快速搭建一个简单的服务，可以选择 Flask 后端服务；如果需要更底层的控制和定制化，可以选择手动实现一个基础的服务器框架"""