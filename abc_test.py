import asyncio


async def read_file_async(filename):
    """异步读取文件的操作"""
    await asyncio.sleep(1)  # 模拟异步操作

    try:
        with open(filename, "r") as f:
            data = f.read()
    except Exception as e:
        return None, e

    return data, None


# 回调函数用于处理异步操作的结果
def on_file_read_complete(error, data):
    if error:
        print(f"发生错误：{error}")
    else:
        print(f"文件内容：{data}")


# 使用异步函数进行文件读取操作
async def main():
    filename = "/Users/wl/z-interface.txt"
    data, error = await read_file_async(filename)
    on_file_read_complete(error, data)


# 执行异步函数
asyncio.run(main())
