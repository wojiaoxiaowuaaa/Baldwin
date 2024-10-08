# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     log_register.py
   Description:   日志操作模块
   Author:        JHao
   date:          2017/3/6
-------------------------------------------------
"""
import os
import logging
import platform
from typing import Optional, Union
from logging.handlers import TimedRotatingFileHandler

# 日志级别
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

CURRENT_PATH: str = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH: str = os.path.join(CURRENT_PATH, os.pardir)
LOG_PATH: str = os.path.join(ROOT_PATH, "config/log")

if not os.path.exists(LOG_PATH):
    """
    当你在其他脚本中导入并实例化LogRegister对象时,if代码块会触发,但这种触发发生在首次导入模块时,而不是在每次创建LogRegister实例时.这是因为Python模块的导入机制.当一个模块首次被导入时.模块内的所有顶层代码(即不在任何函数或类定义内部的代码)都会被执行一次.sys.modules全局字典缓存.
    当你在另一个脚本中通过import log_register或from log_register import LogRegister导入LogRegister时if语句将会执行,创建LOG_PATH目录(如果它还不存在的话)之后,无论你在这个脚本中创建多少个LogRegister实例,if语句中的代码都不会再次执行,因为模块已经加载完毕,其顶层代码只会被执行一次.
    因此日志目录创建的逻辑放在模块的顶层,可以确保在任何LogRegister实例被创建之前,日志目录已经被创建好了,这有助于避免在日志记录过程中遇到目录不存在的错误.同时,这也避免了每次实例化LogRegister时都重复执行目录创建逻辑提高了效率.
    """
    try:
        os.mkdir(LOG_PATH)
    except FileExistsError:
        pass


class LogRegister(logging.Logger):
    """
    日志记录类
    params:
        name(str): 日志文件名称
        level(int): 日志级别,默认为logging.DEBUG
        stream(bool): 屏幕输出/文件输出 可选(默认屏幕和文件均输出)
        file (bool): 是否启用文件输出,默认True.
    return:
        返回一个Logger类对象
    """

    def __init__(
        self,
        name: str,
        level: Union[str, int] = DEBUG,
        stream: bool = True,
        file: bool = True,
    ):
        self.name = name
        self.level = level
        logging.Logger.__init__(self, self.name, level=level)
        if stream:
            self.__setStreamHandler__()
        if file:
            if platform.system() != "Windows":
                self.__setFileHandler__()

    def __setFileHandler__(self, level: Optional[int] = None) -> None:
        file_name = os.path.join(LOG_PATH, "{name}.log".format(name=self.name))
        # 设置日志回滚, 保存在log目录, 一天保存一个文件, 保留15天
        file_handler = TimedRotatingFileHandler(
            filename=file_name, when="D", interval=1, backupCount=15
        )
        file_handler.suffix = "%Y%m%d.log"
        if not level:
            file_handler.setLevel(self.level)
        else:
            file_handler.setLevel(level)
        formatter = logging.Formatter(
            "%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s"
        )

        file_handler.setFormatter(formatter)
        self.file_handler = file_handler
        self.addHandler(file_handler)

    def __setStreamHandler__(self, level: Optional[int] = None) -> None:
        stream_handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s"
        )
        stream_handler.setFormatter(formatter)
        if not level:
            stream_handler.setLevel(self.level)
        else:
            stream_handler.setLevel(level)
        self.addHandler(stream_handler)


if __name__ == "__main__":
    log = LogRegister("test")
    log.info("this is a test msg")
