import os

# 服务端口配置
SERVER_PORT = 9999

# MySQL配置  测试用表:user
MYSQL_HOST = "127.0.0.1"
MYSQL_PORT = 3306
MYSQL_USER = "root"
MYSQL_PASSWD = "123456"
MYSQL_DB = "flask_demo"

# Redis配置
REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
# token过期时间(单位：秒)
EXPIRE_TIME = 600

# MD5加密盐值
MD5_SALT = "wl2024#%*"

# 路径
desktop = '/Users/wl/Desktop'
winter_fell = '/Users/wl/Desktop/27149'
book = '/Users/wl/Documents/脂砚斋重评石头记.pdf'
image_path = '/Users/wl/Downloads/image.webp'


current_directory = os.path.abspath(os.path.dirname(__file__))  # 获取当前脚本所在目录的绝对路径
parent_directory = os.path.abspath(os.path.join(current_directory, '..'))  # 获取上级目录的绝对路径
net = parent_directory + '/doc/带宽.md'  # 拼接获取指定文件的绝对路径
mv_file = '/Users/wl/Documents/中国4K视觉之旅.mkv'
# 文本
files_text = '''
文本排序统计文本中的字符并降序排序:
软件测试工程师（Software Testing Engineer）指理解产品的功能要求，并对其进行测试，检查软件有没有缺陷（Bug），
测试软件是否具有稳定性（Robustness）、安全性、易操作性等性能，写出相应的测试规范和测试用例的专门工作人员。
简而言之，软件测试工程师在一家软件企业中担当的是“质量管理”角色，及时发现软件问题并及时督促更正，确保产品的正常运作。
按其级别和职位的不同，分为三类。
'''
