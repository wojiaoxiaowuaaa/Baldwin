from tenacity import retry, stop_after_attempt, wait_fixed
from retry_decorator import retry_decorator
from color_print import color_print_green


@retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
# 重试三次  时间间隔为1秒
def my_function():
    color_print_green()
    # raise Exception('error')


@retry_decorator(3, 1)
def test_func():
    color_print_green()
    assert 1 == 2

# my_function()
# test_func()
