# 在Python中,当你导入一个包时,Python会自动执行该包的__init__.py文件它的作用是初始化包,
# 它可以包含包的初始化代码,包括变量定义,类和函数的定义等.因此如果你执行from gongju import BANNER可以直接导入下面的BANNER变量.
# 当其在他代码中from gongju import WebRequest时，可以直接使用下面的 WebRequest 类.这种写法简化了导包的操作.
# 初始化包级别的变量,在其他代码片段中import gongju可以直接使用print(gongju.package_variable).
from .webRequest import WebRequest  # noqa: F401
from .jiaoji import get_arr  # noqa: F401
from .dir_file import replace_punctuation_in_file  # noqa: F401
from .color_pr import color_print_green, color_print_red, show_memory_info  # noqa: F401

ban = r"""
****************************************************************
*** ______  ********************* ______ *********** _  ********
*** | ___ \_ ******************** | ___ \ ********* | | ********
*** | |_/ / \__ __   __  _ __   _ | |_/ /___ * ___  | | ********
*** |  __/|  _// _ \ \ \/ /| | | ||  __// _ \ / _ \ | | ********
*** | |   | | | (_) | >  < \ |_| || |  | (_) | (_) || |___  ****
*** \_|   |_|  \___/ /_/\_\ \__  |\_|   \___/ \___/ \_____/ ****
****                       __ / /                          *****
************************* /___ / *******************************
*************************       ********************************
****************************************************************
"""

__version__ = 1.0

__author__ = "wl"

# dic_demo = {'status': 1000, 'message': '请求成功', 'data': [{'assetsId': 'H21241234411487', 'assetsType': 6, 'alias': '1自动化c5n', 'recentUpdateTime': 1698742683062, 'connectStatusDesc': '在线', 'connectStatus': 1,'useStatusDesc': '启用', 'useStatus': 1, 'availableQuantity': None, 'chargingQuantity': 0, 'emptyQuantity': 0, 'exceptionQuantity': None, 'isCanOperate': 1,'alertQuantity': 0}], 'success': True}

# 定义 __all__ 列表  all 是一个特殊的变量，用于定义模块在使用 from module import * 时，允许导出的名称列表。如果模块中定义了 all，只有 all 中列出的名称会被导出。如果没有定义 all，默认会导出所有不以下划线 _ 开头的全局变量、函数和类。通过定义 all，可以显式控制模块的公共 API，隐藏不希望被外部访问的实现细节。
# __all__ = ["WebRequest", "LogRegister", "qr_png"]
