from gongju import qr_png
from gongju import LogRegister
from gongju import WebRequest
from gongju.pic_download import download_images_from_file
from gongju import system_monitor
from gongju.system_monitor import SystemMonitor
from gongju.trans_geshi import replace_punctuation_in_dir, replace_punctuation_in_file
import uuid
from loguru import logger
import asyncio

only_name = str(uuid.uuid4()).replace('-', '')


def mo():
    asyncio.run(SystemMonitor().monitor())  # 运行监控程序


def tran():
    replace_punctuation_in_dir("", [])
    replace_punctuation_in_file("/Users/wl/Downloads/Baldwin/xiecheng/async_pro.py")


def web():
    url = "https://github.com/jhao104/proxy_pool/blob/master/util/webRequest.py"
    web_req = WebRequest().get(url).text
    print(web_req)


if __name__ == '__main__':
    ...
    tran()