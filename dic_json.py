import json
from loguru import logger


def dic_json(d_dic):
    res = json.dumps(d_dic)  # 将字典转换成json   可以在json工具中序列化查看或者用于网络请求
    # logger.info(type(res))
    return res


d = {}
dic_json(d)
