import time
from functools import wraps
from typing import Callable, Any
from loguru import logger
from loguru import logger


def get_time(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start_time: float = time.perf_counter()
        result: Any = func(*args, **kwargs)
        end_time: float = time.perf_counter()
        print(
            f'"{func.__name__}()" took {end_time - start_time:.3f} seconds to execute'
        )
        return result

    return wrapper


def timer(func):
    """用于函数执行耗时统计的装饰器 decorator"""

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(
            f"{func.__name__} took {end_time - start_time:.2f} seconds to execute."
        )
        return result

    return wrapper


def calculate_execution_time(func):
    def wrapper_er(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        logger.info(f"函数{func.__name__}的执行时间为:{execution_time}秒")
        return result

    return wrapper_er


def logger_func(f):
    """日志记录装饰器"""

    @wraps(f)
    def logger_wrapper(*args, **kwargs):
        print(
            (
                f.__name__
                + " function was called with args: "
                + str(args)
                + "  "
                + str(kwargs)
                + "  code explain: "
                + f.__doc__
            )
        )
        return f(*args, **kwargs)

    return logger_wrapper


# @logger_func
# def add(a, b):
#     """adds two numbers"""
#     return a + b
#
#
# print(add(1, 2))


# @get_time
# def fifty_million_loops() -> None:
#     fifty_million: int = int(5e7)
#     print('Looping...')
#     for _ in range(fifty_million):
#         pass
#     print('Done looping!')
#
#
# def main() -> None:
#     fifty_million_loops()
#
#
# if __name__ == '__main__':
#     main()
