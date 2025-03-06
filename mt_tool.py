import uuid
from log_util import logger
from pathlib import Path
from tool import WebRequest
from tool.secrets_str import main
from tool import replace_punctuation_in_file
from config.config import JSON_BIG as js
import toml

# only_name = str(uuid.uuid4()).replace("-", "")

# wl_dir = Path(__file__).resolve().parents[2]

# zsh_file = f"{wl_dir}/.zshrc"
# def get_env():
#     """获取环境变量"""
#     import os
#     from dotenv import load_dotenv
#     load_dotenv()
#     return os.getenv("baldwin")

# with open('config/config.toml', 'r') as f: config = toml.load(f)

# def web():
#     """网络请求封装"""
#     url = "https://github.com/jhao104/proxy_pool/blob/master/util/webRequest.py"
#     web_req = WebRequest().get(url).json
#     return web_req

# replace_punctuation_in_file("/Users/wl/Downloads/Baldwin/config/yield_demo.py")  # 文件标点替换
