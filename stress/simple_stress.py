#!/usr/bin/python3
# ! --*-- coding: utf-8 --*--
import time
import threading
import requests
from loguru import logger

NQ = 1
COUNT = 3000
api = "http://127.0.0.1:7890/hello"


def qps_tc():
    start = time.time()
    req = requests.get(api)
    # logger.info(req.text)
    assert req.status_code == 200
    end = time.time() - start


if __name__ == "__main__":
    # single thread
    # logger.info(f'Single thread perform search action one by one {COUNT} --- {NQ}')
    # time_start = time.time()
    # for k in range(COUNT):
    #     qps_tc()
    # time_cost = time.time() - time_start
    # logger.info(f'Totally time cost{time_cost}')
    # logger.info(f'QPS{ COUNT / time_cost}')

    # multi thread
    logger.info(f'Multi-thread perform search action parallelly {COUNT}  {NQ}')
    threads = []
    time_start = time.time()
    for k in range(COUNT):
        x = threading.Thread(target=qps_tc, args=())
        threads.append(x)
        x.start()
    for th in threads:
        th.join()
    time_cost = time.time() - time_start
    logger.info(f'Totally time cost {time_cost}  sec')
    logger.info(f'QPS: {COUNT / time_cost}')
