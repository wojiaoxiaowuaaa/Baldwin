import os
from dotenv import load_dotenv

# 加载.env文件
load_dotenv()

# 访问
# secret_key = os.environ.get('SECRET_KEY')
contract_address = os.getenv("contract_address")
print(contract_address)
# 使用这些变量
# logger.info(f"环境变量: {os.environ}")
# logger.info(json_demo)
# logger.info(type(json_demo))  # <class 'str'>

# with open(json_demo) as f:
#     data = f.read()
#     # logger.info(type(data))
#     logger.info(data)
