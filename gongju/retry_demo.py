from tenacity import retry, stop_after_attempt, wait_fixed
from color_pr import color_print_green
from retry_decorator import retry_decorator


@retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
def my_function():
    # 重试三次  时间间隔为1秒
    color_print_green()
    raise Exception('error')


@retry_decorator(3, 1)
def wl_func():
    color_print_green()
    assert 1 == 2


# my_function()
# wl_func()