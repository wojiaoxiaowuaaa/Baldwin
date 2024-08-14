import sys
import asyncio
import uuid
import asyncio
from loguru import logger

# sys.path.insert(0, '/Users/wl/Downloads/Baldwin')
from gongju import qr_png
from gongju import LogRegister
from gongju import WebRequest
from gongju.system_monitor import SystemMonitor
from gongju.dir_file import replace_punctuation_in_dir, replace_punctuation_in_file
from gongju.secrets_str import secrets_str

only_name = str(uuid.uuid4()).replace('-', '')


def mo():
    """运行监控程序"""
    asyncio.run(SystemMonitor().monitor())


def tran():
    """中英文标点转换 文件或者目录维度"""
    replace_punctuation_in_dir("", [])
    replace_punctuation_in_file("/Users/wl/Downloads/Baldwin/basic_skill.py")


def web():
    """网络请求封装"""
    url = "https://github.com/jhao104/proxy_pool/blob/master/util/webRequest.py"
    web_req = WebRequest().get(url).text
    print(web_req)


async def main():
    """异步生成随机秘钥"""
    s = await secrets_str()
    print(s)


if __name__ == '__main__':
    ...
    # mo()
    # web()
    # asyncio.run(main())
    tran()
