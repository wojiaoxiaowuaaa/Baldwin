import logging
from logging.handlers import RotatingFileHandler
from typing import Optional


class EnhancedColoredFormatter(logging.Formatter):
    """带颜色格式化器 为日志消息添加颜色和其他额外自定义信息"""

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
        super(EnhancedColoredFormatter, self).__init__(fmt, datefmt)

    def format(self, record: logging.LogRecord) -> str:
        # 调用父类(即 logging.Formatter)的 format 方法来格式化日志记录 record
        super(EnhancedColoredFormatter, self).format(record)

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
    """全局日志管理器GlobalLogger是一个功能强大的全局日志管理器，支持单例模式、控制台和文件日志输出、日志轮转、带颜色的日志输出等功能。
    它的设计简化了日志的使用，提供了统一的日志管理接口，非常适合在中大型项目中使用"""

    _instance = None  # print(GlobalLogger._instance.__dict__)  {'_initialized': True, 'logger': <Logger GlobalEnhancedLogger (DEBUG)>}

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
            cls._instance = super(GlobalLogger, cls).__new__(cls)
            cls._instance._initialized = False  # 在这里动态添加 _initialized 属性.这个属性不需要预先在类中定义,Python 允许我们动态地添加它.
        return cls._instance

    def __init__(
            self,
            # 全是局部变量 不是实例属性。它们用完后通过 self.logger.addHandler(...) 挂到了 logger 对象内部,本身不会留在 _instance 上。
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

        # 创建主logger 实例属性 GlobalLogger._instance.logger
        # 这里给实例动态绑定了一个名为 logger 的属性(就是标准库的 logging.Logger 对象)。Python 是动态语言,实例属性不需要在类里预先声明,赋值即创建
        self.logger = logging.getLogger("GlobalEnhancedLogger")
        self.logger.setLevel(level)
        self.logger.handlers.clear()

        # 控制台处理器
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
        """初始化配置(程序启动时调用)cls(...) 等价于 GlobalLogger(...)即实例化一次"""
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
            GlobalLogger.initialize()  # 触发 __new__ + __init__
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
