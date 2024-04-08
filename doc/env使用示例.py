import os
from loguru import logger
from dotenv import load_dotenv

# 加载.env文件
load_dotenv()

# 访问环境变量
db_host = os.environ.get('DB_HOST')
db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')
secret_key = os.environ.get('SECRET_KEY')

# 使用这些变量
logger.info(f"数据库连接信息: {db_host}, {db_user}, {db_pass}")
logger.info(f"秘密密钥: {secret_key}")