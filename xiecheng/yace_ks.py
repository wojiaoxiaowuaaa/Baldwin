import requests
import traceback
import multiprocessing


def callback(result):
    """
    该函数是用来打印多进程代码中如果出现错误的情况，traceback信息传递的
    :param result:
    :return:
    """
    try:
        # 获取进程返回的结果
        if result:
            print("Result:", result)
            # pass
    except Exception:
        # 捕获异常并打印出错堆栈
        print("Caught an exception in callback:")
        traceback.print_exc()


def run_test(i, req_data, q):
    print(f"第{i}次执行")
    headers = {"Cookie": req_data.get("cookies")}
    try:
        if req_data.get("req_method") in "GET":
            ret = requests.request(
                req_data.get("req_method"),
                req_data.get("request_path"),
                params=req_data.get("params"),
                headers=headers,
                verify=False,
            )
        else:
            ret = requests.request(
                req_data.get("req_method"),
                req_data.get("request_path"),
                json=req_data.get("params"),
                headers=headers,
                verify=False,
            )
    except Exception as e:
        print(e)
        ret = None
    if ret:
        q.put(ret.json())


def run_concurrency_api_test(test_data):
    pool = multiprocessing.Pool(processes=test_data.get("concurrency_times"))
    # 进程池中 需要用multiprocessing.Manager().Queue()， 非进程池使用queue = multiprocessing.Queue(队列长度)
    q = multiprocessing.Manager().Queue()
    for i in range(0, test_data.get("concurrency_times")):
        pool.apply_async(
            run_test,
            (
                i,
                test_data,
                q,
            ),
            callback=callback,
        )
    pool.close()
    pool.join()
    for i in range(0, q.qsize()):
        print(q.get())


if __name__ == "__main__":
    # 登录拉活
    test_data = {
        "times": 5,
        "concurrency_times": 5,
        "request_path": "https://test.com/activity/login",
        "req_method": "POST",
        "cookies": "",
        "content-type": "json",
        "params": {
            "mobile": "11099900093",
            "Code": "000093",
            "activityId": 12,
            "shareKey": "ChdpzxD4/LR8IKzZyfQFSC7vaoBruXbV=",
            "appIdString": "dy67863643890",
            "appId": "dy678636172427043890",
        },
    }

    run_concurrency_api_test(test_data)


def square_number(number, shared_queue):
    """
    计算给定数字的平方并将结果放入共享队列中。
    :param number: 要计算平方的数字。
    :param shared_queue: 用于进程间通信的共享队列。
    """
    result = number * number
    shared_queue.put(result)
    print(f"数字 {number} 的平方是 {result}")
    # print(shared_queue.get())


# if __name__ == "__main__":
#     # 创建一个管理器队列用于进程间通信
#     shared_queue = multiprocessing.Manager().Queue()
#
#     # 定义一组数字
#     numbers = [1, 2, 3, 4, 5]
#
#     # 创建一个进程池
#     pool = multiprocessing.Pool(processes=len(numbers))
#
#     # 启动多个进程，每个进程都执行 square_number 函数
#     for number in numbers:
#         pool.apply_async(square_number, args=(number, shared_queue))
#
#     # 关闭进程池，防止更多任务提交到池中
#     pool.close()
#
#     # 等待所有进程完成
#     pool.join()
#
#     # 从共享队列中获取并打印所有结果
#     while not shared_queue.empty():
#         print(f"队列中的结果：{shared_queue.get()}")
