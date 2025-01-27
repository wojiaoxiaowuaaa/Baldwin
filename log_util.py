import logging
from typing import Optional
from logging.handlers import RotatingFileHandler
import os
import sys


class EnhancedColoredFormatter(logging.Formatter):
    """带颜色格式化器 为日志消息添加颜色"""

    COLORS = {
        logging.DEBUG: "\033[36m",
        logging.INFO: "\033[32m",
        logging.WARNING: "\033[33m",
        logging.ERROR: "\033[31m",
        logging.CRITICAL: "\033[31;1m",
    }
    RESET = "\033[0m"
    GREY = "\033[90m"

    def __init__(self, fmt: Optional[str] = None, datefmt: Optional[str] = None):
        # 设置默认格式
        default_fmt = (
            "[%(asctime)s] "
            "[PID:%(process)d|TID:%(thread)d] "
            "[%(levelname)-8s] "
            "%(filename)s:%(lineno)d - "
            "%(message)s"
        )
        fmt = fmt or default_fmt
        super().__init__(fmt, datefmt)

    def format(self, record: logging.LogRecord) -> str:
        # 调用父类(即 logging.Formatter)的 format 方法来格式化日志记录 record,并将格式化后的结果赋值给变量 message.
        message = super().format(record)
        # 添加颜色修饰
        color = self.COLORS.get(record.levelno, "")
        colored_message = (
            f"{self.GREY}[{record.asctime}]{self.RESET} "
            f"{self.GREY}[PID:{record.process}|TID:{record.thread}]{self.RESET} "
            f"{color}[{record.levelname:<8}]{self.RESET} "
            f"{self.GREY}{record.filename}:{record.lineno}{self.RESET} - "
            f"{color}{record.message}{self.RESET}"
        )
        # 返回一个包含了所有这些颜色修饰的字符串,它将被返回并用于在控制台输出带颜色的日志消息.
        return colored_message


class GlobalLogger:
    """全局日志管理器(单例模式)"""

    _instance = None
    DEFAULT_FORMAT = (
        "[%(asctime)s] "
        "[PID:%(process)d|TID:%(thread)d] "
        "[%(levelname)-8s] "
        "%(filename)s:%(lineno)d "
        "- %(message)s"
    )
    DEFAULT_DATEFMT = "%Y-%m-%d %H:%M:%S"

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False  # 在这里动态添加 _initialized 属性.这个属性不需要预先在类中定义，Python 允许我们动态地添加它。
        return cls._instance

    def __init__(
        self,
        level: int = logging.DEBUG,
        fmt: str = DEFAULT_FORMAT,
        datefmt: str = DEFAULT_DATEFMT,
        use_color: bool = True,
        log_file: Optional[str] = None,
        max_bytes: int = 10 * 1024 * 1024,  # 默认10MB日志轮转
        backup_count: int = 5,
    ):
        if self._initialized:
            return
        self._initialized = True

        # 创建主logger
        self.logger = logging.getLogger("GlobalEnhancedLogger")
        self.logger.setLevel(level)
        self.logger.handlers.clear()

        # 控制台处理器
        # console_handler = logging.StreamHandler(sys.stdout)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        if use_color:
            # 根据 use_color 参数决定是否使用 EnhancedColoredFormatter.
            formatter = EnhancedColoredFormatter(fmt, datefmt)
        else:
            formatter = logging.Formatter(fmt, datefmt)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        # 文件处理器
        if log_file:
            file_handler = RotatingFileHandler(
                filename=log_file,
                maxBytes=max_bytes,
                backupCount=backup_count,
                encoding="utf-8",
            )
            file_formatter = logging.Formatter(
                fmt.replace("\033[", "")  # 去除颜色代码
                .replace("[0m", "")  # 避免文件日志含ANSI码
                .replace("[90m", ""),
                datefmt,
            )
            file_handler.setFormatter(file_formatter)
            self.logger.addHandler(file_handler)

    @classmethod
    def initialize(
        cls,
        level: int = logging.DEBUG,
        fmt: str = DEFAULT_FORMAT,
        datefmt: str = DEFAULT_DATEFMT,
        use_color: bool = True,
        log_file: Optional[str] = None,
        **kwargs,
    ):
        """初始化配置(程序启动时调用)"""
        cls(
            level=level,
            fmt=fmt,
            datefmt=datefmt,
            use_color=use_color,
            log_file=log_file,
            **kwargs,
        )

    @staticmethod
    def get_logger() -> logging.Logger:
        """获取日志实例"""
        if not GlobalLogger._instance:
            GlobalLogger.initialize()  # 默认初始化
        return GlobalLogger._instance.logger

    @staticmethod
    def debug(msg: str, *args, **kwargs):
        GlobalLogger.get_logger().debug(msg, stacklevel=3, *args, **kwargs)
        
    @staticmethod
    def info(msg: str, *args, **kwargs):
        GlobalLogger.get_logger().info(msg, stacklevel=3, *args, **kwargs)

    @staticmethod
    def warning(msg: str, *args, **kwargs):
        GlobalLogger.get_logger().warning(msg, stacklevel=3, *args, **kwargs)

    @staticmethod
    def error(msg: str, *args, **kwargs):
        GlobalLogger.get_logger().error(msg, stacklevel=3, *args, **kwargs)

    @staticmethod
    def critical(msg: str, *args, **kwargs):
        GlobalLogger.get_logger().critical(msg, stacklevel=3, *args, **kwargs)


# 默认导出接口
logger = GlobalLogger

# for i in dir(logger): logger.info(i)


"""
from log_util import Logger

# 创建两个集合
dict_set = set(Logger.__dict__.keys())
dir_set = set(dir(Logger))

# 计算交集
intersection = dict_set.intersection(dir_set)

# 计算并集
union = dict_set.union(dir_set)

# 打印结果
Logger.critical("交集:")
for item in sorted(intersection): Logger.critical(item)

Logger.critical("\n并集:")
for item in sorted(union): Logger.critical(item)

# 额外信息：只在 dir() 中出现的项
only_in_dir = dir_set - dict_set
Logger.critical("\n只在 dir() 中出现的项:")
for item in sorted(only_in_dir): Logger.critical(item)

# 额外信息：只在 __dict__ 中出现的项
only_in_dict = dict_set - dir_set
Logger.critical("\n只在 __dict__ 中出现的项:")
for item in sorted(only_in_dict): Logger.critical(item)
git
"""
