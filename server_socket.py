import socket

# 创建 socket 对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
# host = socket.gethostname()
host = 'localhost'
port = 12345  # 设置端口号


# 绑定端口号
server_socket.bind((host, port))

# 设置最大连接数，超过后排队
server_socket.listen(5)

while True:
    # 建立客户端连接  这里addr会展示动态分配的端口号  每次链接都不同
    client_socket, addr = server_socket.accept()
    print('连接地址:', addr)

    # 发送消息给客户端
    message = '你好啊  海绵宝宝！'
    client_socket.send(message.encode('utf-8'))

    # 接收客户端消息
    data = client_socket.recv(1024).decode('utf-8')
    print('客户端消息:', data)

    # 关闭连接
    client_socket.close()




