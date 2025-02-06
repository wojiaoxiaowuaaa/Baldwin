import uuid
from log_util import logger
from pathlib import Path
from tool import WebRequest
from tool import replace_punctuation_in_file
from tool.secrets_str import main
from dotenv import load_dotenv
import os
import toml

only_name = str(uuid.uuid4()).replace("-", "")

wl_dir = Path(__file__).resolve().parents[2]

zsh_file = f"{wl_dir}/.zshrc"

# def get_env():
#     load_dotenv()
#     return os.getenv("baldwin")

# def web():
#     """网络请求封装"""
#     url = "https://github.com/jhao104/proxy_pool/blob/master/util/webRequest.py"
#     web_req = WebRequest().get(url).json
#     return web_req

# replace_punctuation_in_file("")  # 文件标点替换

# with open('config/config.toml', 'r') as f: config = toml.load(f)
