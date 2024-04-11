import os
import dotenv

# 加载.env 文件
dotenv.load_dotenv()

# 访问环境变量
API_KEY = os.getenv("JSON_DEMO")

print(API_KEY)