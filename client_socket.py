import socket

# 创建 socket 对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
# host = socket.gethostname()
host = 'localhost'
port = 12345  # 与服务端端口号相同


# 连接服务端
client_socket.connect((host, port))

# 接收服务端消息
data = client_socket.recv(1024).decode('utf-8')
print('服务端消息:', data)

# 发送消息给服务端
message = '你好，章鱼哥！'
client_socket.send(message.encode('utf-8'))

# 关闭连接
client_socket.close()

