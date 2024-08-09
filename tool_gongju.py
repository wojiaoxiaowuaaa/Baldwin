from gongju import WebRequest, LogRegister, qr_png
from gongju.pic_download import download_images_from_file
from gongju import system_monitor
from gongju.system_monitor import SystemMonitor
from gongju.trans_geshi import replace_punctuation_in_dir, replace_punctuation_in_file
import uuid
import asyncio

only_name = str(uuid.uuid4()).replace('-', '')


def mo():
    asyncio.run(SystemMonitor().monitor())  # 运行监控程序


def trans():
    replace_punctuation_in_dir("", [])
    replace_punctuation_in_file("")