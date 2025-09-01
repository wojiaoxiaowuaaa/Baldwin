import socket
import threading
import logging
from typing import Dict, Tuple, Optional

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SimpleRedisServer:
    def __init__(self, host: str = '127.0.0.1', port: int = 6379):
        self.host = host
        self.port = port
        self.data_store: Dict[str, bytes] = {}  # 存储键值对
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.running = False

    def start(self):
        """启动服务器"""
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)  # 最多同时处理5个连接
            self.running = True
            logger.info(f"Redis服务器启动，监听 {self.host}:{self.port}")
            
            while self.running:
                client_socket, client_address = self.server_socket.accept()
                logger.info(f"新连接: {client_address}")
                
                # 为每个客户端创建一个新线程处理
                client_handler = threading.Thread(
                    target=self.handle_client,
                    args=(client_socket, client_address),
                    daemon=True
                )
                client_handler.start()
                
        except Exception as e:
            logger.error(f"服务器错误: {e}")
        finally:
            self.stop()

    def stop(self):
        """停止服务器"""
        self.running = False
        if self.server_socket:
            self.server_socket.close()
        logger.info("服务器已停止")

    def handle_client(self, client_socket: socket.socket, client_address):
        """处理客户端连接"""
        try:
            while True:
                # 读取客户端发送的数据
                data = client_socket.recv(1024)
                if not data:
                    logger.info(f"客户端断开连接: {client_address}")
                    break
                
                # 解析RESP协议格式的命令
                command, args = self.parse_resp(data)
                if not command:
                    response = self.encode_resp_error("无效的命令格式")
                    client_socket.sendall(response)
                    continue
                
                # 处理命令
                response = self.process_command(command, args)
                client_socket.sendall(response)
                
        except Exception as e:
            logger.error(f"处理客户端 {client_address} 时出错: {e}")
        finally:
            client_socket.close()

    def parse_resp(self, data: bytes) -> Tuple[Optional[str], list]:
        """解析RESP协议格式的数据"""
        try:
            # RESP协议中，数组以*开头
            if data.startswith(b'*'):
                # 提取数组长度
                parts = data.split(b'\r\n')
                if len(parts) < 3:
                    return None, []
                    
                # 第一个元素是数组长度，如*2\r\n$3\r\nGET\r\n$3\r\nkey\r\n
                array_length = int(parts[0][1:])  # 去掉*号
                command_parts = []
                
                # 提取命令和参数
                for i in range(array_length):
                    # 每个元素以$开头，后跟长度
                    if i*2 + 1 >= len(parts):
                        return None, []
                        
                    length_part = parts[i*2 + 1]
                    if not length_part.startswith(b'$'):
                        return None, []
                        
                    length = int(length_part[1:])  # 去掉$号
                    value_part = parts[i*2 + 2]
                    
                    if len(value_part) != length:
                        return None, []
                        
                    command_parts.append(value_part.decode('utf-8'))
                
                if command_parts:
                    return command_parts[0].upper(), command_parts[1:]
                
            return None, []
            
        except Exception as e:
            logger.error(f"解析RESP数据出错: {e}")
            return None, []

    def encode_resp_simple_string(self, value: str) -> bytes:
        """编码为RESP简单字符串格式"""
        return f"+{value}\r\n".encode('utf-8')

    def encode_resp_bulk_string(self, value: Optional[bytes]) -> bytes:
        """编码为RESP批量字符串格式"""
        if value is None:
            return b"$-1\r\n"  # 表示空值
        return f"${len(value)}\r\n{value.decode('utf-8')}\r\n".encode('utf-8')

    def encode_resp_error(self, message: str) -> bytes:
        """编码为RESP错误格式"""
        return f"-{message}\r\n".encode('utf-8')

    def encode_resp_integer(self, value: int) -> bytes:
        """编码为RESP整数格式"""
        return f":{value}\r\n".encode('utf-8')

    def process_command(self, command: str, args: list) -> bytes:
        """处理命令并返回响应"""
        logger.info(f"处理命令: {command} {args}")
        
        if command == 'SET' and len(args) >= 1:
            key = args[0]
            value = args[1].encode('utf-8') if len(args) > 1 else b''
            self.data_store[key] = value
            return self.encode_resp_simple_string("OK")
            
        elif command == 'GET' and len(args) == 1:
            key = args[0]
            value = self.data_store.get(key)
            return self.encode_resp_bulk_string(value)
            
        elif command == 'PING':
            if args:
                return self.encode_resp_simple_string(args[0])
            return self.encode_resp_simple_string("PONG")
            
        elif command == 'DEL' and len(args) >= 1:
            count = 0
            for key in args:
                if key in self.data_store:
                    del self.data_store[key]
                    count += 1
            return self.encode_resp_integer(count)
            
        elif command == 'EXISTS' and len(args) >= 1:
            count = sum(1 for key in args if key in self.data_store)
            return self.encode_resp_integer(count)
            
        else:
            return self.encode_resp_error(f"未知命令: {command}")

if __name__ == "__main__":
    server = SimpleRedisServer()
    try:
        server.start()
    except KeyboardInterrupt:
        logger.info("接收到停止信号")
        server.stop()
