from gongju import WebRequest, LogRegister, qr_png
from gongju.pic_download import download_images_from_file
from gongju import system_monitor
from gongju.system_monitor import SystemMonitor
import uuid
import asyncio

only_name = str(uuid.uuid4()).replace('-', '')


def mo():
    asyncio.run(SystemMonitor().monitor())  # 运行监控程序

