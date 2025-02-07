# echo $PATH命令在Mac终端(或任何Linux系统)中用于显示当前用户的环境变量PATH的内容.PATH环境变量包含了一系列的目录,这些目录被操作系统用来搜索可执行文件.

# 介绍下sys.path.append(os.path.abspath('.'))
# sys.path 是一个列表,它指定了 Python 在导入模块时会搜索的目录.当你尝试导入一个模块时,Python 会按照 sys.path 中的目录顺序依次查找模块文件
# sys.path.append(path) 是将指定的路径 path 添加到 sys.path 列表中.这通常用于确保 Python 解释器能够找到项目中的模块,特别是当项目的某个模块需要被其他模块导入时.类似的能力site.addsitedir('')亦可实现
# sys.path.insert 添加的路径在程序运行期间有效,程序退出后失效. 如: sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
# 将当前文件所在路径,添加到Python路径的最前面:  if (BASE_PATH := os.path.abspath(".")) not in sys.path: sys.path.insert(0, BASE_PATH)

# 通过设置 PYTHONPATH 环境变量,你可以指定 Python 解释器在查找模块和包时应该搜索的目录.这使得你能够在自定义目录中组织和管理你的 Python 模块和包,而不需要将它们复制到标准库路径或当前脚本目录中.
# export PYTHONPATH="/Users/wl/Downloads/Baldwin:$PYTHONPATH"
# 在其他目录下的脚本中导入项目根目录下的包示例:  from log_util import logger

# mac下的brew安装的解释器路径: /usr/local/Cellar/python@3.13/3.13.1/Frameworks/Python.framework/Versions/3.13/bin
