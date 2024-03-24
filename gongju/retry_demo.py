from tenacity import retry, stop_after_attempt, wait_fixed
from retry_decorator import retry_


@retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
def my_function():
    print('ing......')  # 重试三次  时间间隔为1秒
    # assert 1 == 2
    # raise Exception('error')


@retry_(5, 5)
def test_func():
    print('test_func is called')
    assert 1 == 1


# my_function()
test_func()
