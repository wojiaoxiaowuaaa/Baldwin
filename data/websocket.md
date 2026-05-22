## WebSocket简介
WebSocket 是一种在单个 TCP 连接上进行全双工通信的协议，它允许客户端和服务器之间进行实时的双向通信。与传统的 HTTP 请求-响应模型不同，WebSocket 允许服务器主动向客户端推送数据，而不需要客户端发起请求。

以下是 WebSocket 的一些关键特点和优点：

1. **全双工通信：** WebSocket 允许客户端和服务器之间同时进行双向通信，可以在不同方向上发送和接收数据。这种实时的双向通信模型非常适合于实时性要求较高的应用，如在线游戏、实时聊天、股票交易等。

2. **基于 TCP：** WebSocket 建立在 TCP 连接之上，与 HTTP 不同，它不需要在每次通信时建立新的连接，从而减少了通信的开销和延迟，提高了通信效率。

3. **低延迟：** 由于 WebSocket 是长连接，它可以保持连接状态，避免了频繁的握手和连接建立，从而降低了通信的延迟，使得实时性更强。

4. **节省带宽：** WebSocket 使用的是二进制数据格式，相比于 HTTP 的文本数据格式，它可以更高效地传输数据，节省了带宽和网络资源。

5. **跨域支持：** WebSocket 支持跨域通信，可以在不同的域名下进行通信，从而实现跨域数据传输。

6. **安全性：** WebSocket 支持加密通信，可以使用 TLS/SSL 加密协议来保障通信的安全性，防止数据被窃取或篡改。

7. **原生支持：** 现代的 Web 浏览器和服务器都原生支持 WebSocket 协议，无需额外的插件或库，开发者可以直接使用浏览器提供的 WebSocket API 来进行开发。

总的来说，WebSocket 是一种高效、实时、安全的通信协议，适用于需要实时双向通信的 Web 应用，它在实时性要求较高的应用场景中有着广泛的应用前景。
## Tornado 脚本示例，演示了如何使用 Tornado 支持 WebSocket：

```python
import tornado.ioloop
import tornado.web
import tornado.websocket

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket连接已建立")

    def on_message(self, message):
        print("接收到消息:", message)
        self.write_message("你发送的消息是：" + message)

    def on_close(self):
        print("WebSocket连接已关闭")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("WebSocket 示例")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/websocket", WebSocketHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("服务器已启动，端口：8888")
    tornado.ioloop.IOLoop.current().start()
```

这个示例中，我们创建了一个简单的 WebSocket 服务器。当客户端连接到 `/websocket` 路径时，`WebSocketHandler` 类将处理 WebSocket 连接。在 `open` 方法中，我们打印出连接建立的消息，在 `on_message` 方法中，我们接收客户端发送的消息，并回复相同的消息，最后在 `on_close` 方法中打印出连接关闭的消息。

同时，我们也创建了一个普通的 HTTP 请求处理器 `MainHandler`，用于处理根路径 `/` 的请求，返回一个简单的文本响应。

要运行这个示例，只需在终端中运行该脚本，然后使用 WebSocket 客户端连接到 `ws://localhost:8888/websocket` 即可。可以使用浏览器中的开发者工具或者专门的 WebSocket 客户端工具进行测试。

示例用法：
1. 运行脚本 `python script_name.py`
2. 使用 WebSocket 客户端连接到 `ws://localhost:8888/websocket`。
3. 在连接成功后，客户端可以发送消息，服务器会回复相同的消息。
4. 可以在服务器端的终端中查看连接状态和收发的消息。


## 使用脚本连接到WebSocket服务器
```python
import websocket

def on_message(ws, message):
    print("接收到消息:", message)

def on_error(ws, error):
    print("发生错误:", error)

def on_close(ws):
    print("连接已关闭")

def on_open(ws):
    print("连接已建立")
    ws.send("Hello, WebSocket Server!")

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:8888/websocket",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()

```

