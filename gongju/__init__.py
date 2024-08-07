# 在Python中,当你导入一个包时,Python会自动执行该包的__init__.py文件它的作用是初始化包,
# 它可以包含包的初始化代码,包括变量定义,类和函数的定义等.因此如果你执行from gongju import BANNER可以直接导入下面的BANNER变量.
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
# 当其在他代码中from gongju import WebRequest时，可以直接使用下面的 WebRequest 类.这种写法简化了导包的操作.
from .webRequest import WebRequest
from .log_register import LogRegister
from .qr_png import qr_png

# 初始化包级别的变量,在其他代码片段中import gongju可以直接使用print(gongju.package_variable).
package_variable = "This is a package variable"

__version__ = 1.0

__author__ = "wl"

# 定义 __all__ 列表
# __all__ = ["WebRequest", "LogRegister", "qr_png"]
