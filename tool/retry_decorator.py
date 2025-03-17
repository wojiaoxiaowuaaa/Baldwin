import time
from functools import wraps
from typing import Callable, Any
from loguru import logger
from time import sleep
from tenacity import retry, stop_after_attempt, wait_fixed
from color_pr import color_print_green


# sys.path.insert(0, "../")


def retry_decorator(retries: int = 3, delay: float = 1) -> Callable:
    """
    Attempt to call a function, if it fails, try again with a specified delay.
    :param retries: The max amount of retries you want for the function call
    :param delay: The delay (in seconds) between each function retry
    :return:
    """

    # Don't let the user use this decorator if they are high
    if retries < 1 or delay <= 0:
        raise ValueError("Are you high, mate?")

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for i in range(1, retries + 1):  # 1 to retries + 1 since upper bound is exclusive
                try:
                    logger.info(f"Running ({i}): {func.__name__}()...")
                    return func(*args, **kwargs)
                except Exception as e:
                    # Break out of the loop if the max amount of retries is exceeded
                    if i == retries:
                        logger.info(f"Error: {repr(e)}.")
                        logger.info(f'"{func.__name__}()" failed after {retries} retries.')
                        break
                    else:
                        logger.info(f"Error: {repr(e)}")
                        sleep(delay)  # Add a delay before running the next iteration

        return wrapper

    return decorator


# 使用示例
@retry_decorator(delay=3)
def connect() -> None:
    time.sleep(1)
    raise Exception("Could not connect to internet")


def main(): connect()


@retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
def my_function():
    # 重试三次  时间间隔为1秒
    color_print_green()
    raise Exception("error")


@retry_decorator(3, 1)
def wl_func():
    color_print_green()
    assert 1 == 2


if __name__ == "__main__":
    # main()
    # my_function()
    wl_func()
