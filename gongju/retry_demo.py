from tenacity import retry, stop_after_attempt, wait_fixed


@retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
def my_function():
    print('ing......')  # 重试三次  时间间隔为1秒
    assert 1 == 2


my_function()
