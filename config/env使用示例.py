import os
import json
from loguru import logger
from dotenv import  load_dotenv
# 加载.env文件
load_dotenv()

# 访问
# secret_key = os.environ.get('SECRET_KEY')
json_demo = os.getenv('JSON_DEMO')
# 使用这些变量
# logger.info(f"环境变量: {os.environ}")
# logger.info(json_demo)
# logger.info(type(json_demo))  # <class 'str'>

with open(json_demo) as f:
    data = f.read()
    # logger.info(type(data))
    logger.info(data)

