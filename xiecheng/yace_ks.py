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
            print('Result:', result)
            # pass
    except Exception:
        # 捕获异常并打印出错堆栈
        print('Caught an exception in callback:')
        traceback.print_exc()


def run_test(i, req_data, q):
    print(f"第{i}次执行")
    headers = {
        "Cookie": req_data.get("cookies")
    }
    try:
        if req_data.get('req_method') in "GET":
            ret = requests.request(req_data.get('req_method'), req_data.get('request_path'),
                                   params=req_data.get('params'), headers=headers, verify=False)
        else:
            ret = requests.request(req_data.get('req_method'), req_data.get('request_path'),
                                   json=req_data.get('params'), headers=headers, verify=False)
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
        pool.apply_async(run_test, (i, test_data, q,), callback=callback)
    pool.close()
    pool.join()
    for i in range(0, q.qsize()):
        print(q.get())


if __name__ == "__main__":
    # 登录拉活
    test_data = {
        "times": 5,
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
            "appId": "dy678636172427043890"
        }
    }

    run_concurrency_api_test(test_data)
