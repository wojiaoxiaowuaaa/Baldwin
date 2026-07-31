import asyncio

# 定义服务器监听的 IP 地址和端口号
# "0.0.0.0" 表示监听本机上所有的网络接口（IPv4），允许外部设备访问
HOST, PORT = "0.0.0.0", 9000


# 定义 UDP 协议回调处理类，必须继承自 asyncio.DatagramProtocol
class UDPServerProtocol(asyncio.DatagramProtocol):

    # 当接收到一个 UDP 数据报文时，底层的事件循环会自动触发并调用此方法
    def datagram_received(self, data, addr):
        # UDP 是无连接的协议，没有传统 TCP 的连接建立（三次握手）过程
        # data: 接收到的原始字节数据 (bytes 类型)
        # addr: 发送方的地址信息，通常是一个元组 (客户端 IP, 客户端源端口)

        # 打印收到的 UDP 数据。这里假设接收到的是 UTF-8 编码的文本，因此需要对其进行 decode 解码
        print("[udp]", addr, "\n", data.decode("utf8"))


# 定义主协程函数，用于初始化并维持服务器运行
async def main():
    # 获取当前所在线程的事件循环 (Event Loop)
    loop = asyncio.get_running_loop()

    # 创建并启动 UDP Endpoint（端点）
    # 返回值 transport: 代表底层传输接口，用于控制网络流（例如向外发数据 transport.sendto() 或关闭套接字）
    # 返回值 protocol: 返回具体的协议实例（即 UDPServerProtocol 的实例）
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: UDPServerProtocol(),  # 协议工厂函数：事件循环将调用此函数来创建处理该 Endpoint 的协议对象
        local_addr=(HOST, PORT)  # 指定要绑定的本地 IP 和监听端口
    )

    print("[+] udp server started", HOST, PORT)

    try:
        # loop.create_datagram_endpoint() 只是启动了监听，它本身是非阻塞的，瞬间就会执行完毕。
        # 如果这里不加阻塞，main() 函数会立刻结束，程序也就随之退出了。
        # 因此，这里通过 await 一个永远不会被标记为 done 的 asyncio.Future()，
        # 将当前协程永远挂起，从而让服务器保持在后台持续监听和运行状态。
        await asyncio.Future()
    finally:
        # 无论程序是正常退出还是被中断（例如用户按下了 Ctrl+C 抛出 KeyboardInterrupt 异常），
        # finally 块都能确保释放资源，调用 transport.close() 优雅地关闭底层 Socket。
        transport.close()


# 程序的入口点
if __name__ == "__main__":
    # asyncio.run 会自动为你创建一个新的事件循环，执行传入的协程 main()，并在执行完毕后安全地关闭循环
    asyncio.run(main())
